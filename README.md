# iot-sensor-elt-project
IoT ELT pipeline using AWS Glue, S3, and Athena
#IoT Sensor Data ELT Pipeline using AWS Glue

### Role: AWS Glue Engineer  
This project showcases an end-to-end **ELT pipeline** for processing IoT sensor data using AWS Glue, S3, and Athena.

---

## 📁 Project Structure
s3://iot-sensor-elt-data/
│
├── raw/
│   └── sensor_data.csv
│
└── processed/
├── hourly/
│   └── hourly_avg_temp.parquet
└── daily/
└── daily_avg_temp.parquet
---

## 🔧 What I Did

- **Created S3 buckets** to store raw and processed sensor data.
- **Uploaded a sample raw CSV** file with sensor readings.
- **Developed an AWS Glue Job** using PySpark to:
  - Convert timestamps to standard datetime format
  - Remove invalid temperatures (less than -50 or more than 150)
  - Calculate **hourly and daily average** temperatures
- **Configured AWS Glue Crawlers** to catalog raw and transformed data
- **Stored transformed data** in **Parquet** format (efficient for querying)
- **Verified outputs using Athena** with SQL queries
- Captured all setup via **screenshots** for documentation

---

---

## 🧰 Technologies Used

- **Amazon S3** – Storage for raw and processed data  
- **AWS Glue** – Serverless ETL engine using PySpark  
- **AWS Glue Crawlers** – For automatic schema inference and Data Catalog population  
- **AWS Glue Data Catalog** – Central metadata repository  
- **Amazon Athena** – Query engine to run SQL on S3 data

---

## 🧪 Sample Data

✔️ Uploaded: `sensor_data.csv`

```csv
sensor_id,timestamp,temperature
101,2025-06-10T10:00:00Z,25
102,2025-06-10T10:10:00Z,30
103,2025-06-10T10:20:00Z,-60
104,2025-06-10T10:30:00Z,200
105,2025-06-10T11:00:00Z,28

---

## 🖼️ Screenshots

Include screenshots of:
- S3 bucket structure
- Glue job configuration
- Crawler and Data Catalog tables
- Athena query results

---
🔄 ETL Process (AWS Glue Job)

✔️ Uploaded: glue_etl_script.py

Transformation logic:
	•	Parse timestamps
	•	Filter out invalid temperatures (< -50 or > 150)
	•	Calculate:
	•	Hourly average temperature
	•	Daily average temperature
	•	Save results in Parquet format to S3
AWS Glue Crawlers

3 Crawlers created and run successfully:
	•	raw_sensor_data
	•	hourly_avg_temp
	•	daily_avg_temp

Tables registered in: iot_sensor_data_db (Glue Data Catalog)

## ✅ Outcome

This project successfully automates the cleaning and transformation of raw IoT sensor data, stores the outputs in query-optimized formats, and allows for easy analysis via Athena. Ideal for production-scale IoT data pipelines.

---

## 📌 Credits

**Arpita Gaikwad**  
_19 y/o BCA student with a specialization in Cloud Computing & Cybersecurity_  
**Role**: AWS Glue Engineer

---
