# iot-sensor-elt-project
IoT ELT pipeline using AWS Glue, S3, and Athena
# 🚀 IoT Sensor Data ELT Pipeline using AWS Glue

### 👩‍💻 Role: AWS Glue Engineer  
This project showcases an end-to-end **ELT pipeline** for processing IoT sensor data using AWS Glue, S3, and Athena.

---

## 📁 Project Structure
iot-sensor-elt-data/
├── raw/                # Raw input CSV files
├── processed/
│   ├── hourly/         # Hourly average temperature (Parquet)
│   └── daily/          # Daily average temperature (Parquet)
├── scripts/
│   └── glue_job.py     # PySpark script for Glue Job
├── screenshots/        # AWS Console screenshots
└── README.md
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

## 🧠 Technologies Used

- AWS S3  
- AWS Glue (ETL)  
- PySpark  
- AWS Glue Data Catalog  
- AWS Athena  

---

## 🖼️ Screenshots

Include screenshots of:
- S3 bucket structure
- Glue job configuration
- Crawler and Data Catalog tables
- Athena query results

---

## ✅ Outcome

This project successfully automates the cleaning and transformation of raw IoT sensor data, stores the outputs in query-optimized formats, and allows for easy analysis via Athena. Ideal for production-scale IoT data pipelines.

---

## 📌 Credits

**Arpita Gaikwad**  
_19 y/o BCA student with a specialization in Cloud Computing & Cybersecurity_  
**Role**: AWS Glue Engineer

---
