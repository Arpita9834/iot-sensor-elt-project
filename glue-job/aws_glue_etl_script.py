import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, to_timestamp, hour, to_date, avg
from pyspark.sql import functions as F

# Initialize Glue Context
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read raw CSV data from S3
datasource0 = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://iot-sensor-elt-data/raw/"]},
    format="csv",
    format_options={"withHeader": True}
)

# Convert DynamicFrame to DataFrame
df = datasource0.toDF()

# Data cleaning and transformation
df = df.withColumn("timestamp", to_timestamp(col("timestamp")))
df = df.withColumn("temperature", col("temperature").cast("double"))
df = df.filter((col("temperature") >= -50) & (col("temperature") <= 150))

# Calculate hourly average temperature
hourly_df = df.withColumn("hour", hour("timestamp")) \
              .groupBy("sensor_id", "hour") \
              .agg(avg("temperature").alias("avg_temperature"))

# Calculate daily average temperature
daily_df = df.withColumn("date", to_date("timestamp")) \
             .groupBy("sensor_id", "date") \
             .agg(avg("temperature").alias("avg_temperature"))

# Convert DataFrames back to DynamicFrames
hourly_dyf = glueContext.create_dynamic_frame.from_df(hourly_df, glueContext, "hourly_dyf")
daily_dyf = glueContext.create_dynamic_frame.from_df(daily_df, glueContext, "daily_dyf")

# Write hourly data to S3
glueContext.write_dynamic_frame.from_options(
    frame=hourly_dyf,
    connection_type="s3",
    connection_options={"path": "s3://iot-sensor-elt-data/processed/hourly/"},
    format="parquet"
)

# Write daily data to S3
glueContext.write_dynamic_frame.from_options(
    frame=daily_dyf,
    connection_type="s3",
    connection_options={"path": "s3://iot-sensor-elt-data/processed/daily/"},
    format="parquet"
)

job.commit()
