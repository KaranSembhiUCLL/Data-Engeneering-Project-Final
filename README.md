# Data-Engeneering-Project

## Project by Nachat & Karan

This project contains two data pipelines orchestrated with Apache Airflow running in Docker:

- **Batch pipeline** (`taxi_pipeline.ipynb`) — processes NYC Yellow Taxi trip data
- **Real-time pipeline** (`cars_pipeline.ipynb`) — processes e-commerce orders on file detection

---

## Requirements

Before running either pipeline, make sure your `.env` file is present at the **root level** of the project with the following variables:

```env

AZURE_CONNECTION_STRING=your_connection_string_here

```

---

## Starting Docker

```bash
docker compose up -d
```

### Setting password for airflow

```
docker-compose exec airflow-webserver airflow users create \
 --username airflow \
 --password airflow \
 --firstname Admin \
 --lastname User \
 --role Admin \
 --email admin@example.com
```

---

## 1. Batch Pipeline (`taxi_pipeline.ipynb`)

### Setup

1. Download the dataset from the [NYC TLC Trip Record Data page](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
2. Place `yellow_tripdata_2025-01.parquet` inside the `/data` folder

### Running

You can trigger the pipeline in two ways:

- **Manually** — trigger it from the Airflow UI at `http://localhost:8082`
- **Scheduled** — change the `schedule` parameter in `dags/yellow_taxi_dag.py` to your desired cron expression. Airflow picks up DAG changes automatically — no Docker restart needed.

### Output

- A processed file `yellow_tripdata_processed_2025-01.parquet` is written to `/output`
- Running the pipeline multiple times always produces **1 file** (idempotent — no duplicates)
- If Azure is configured: the processed file is uploaded to the `yellow-taxi-output` container in Azure Blob Storage
- Logs are available in the Airflow UI under `dag_id=yellow_taxi_pipeline`

---

## 2. Real-Time Pipeline (`cars_pipeline.ipynb`)

### Setup

No additional setup needed beyond the `.env` file.

### Key files

| Path                        | Description                                     |
| --------------------------- | ----------------------------------------------- |
| `/dataset`                  | Drop your CSV file here to trigger the pipeline |
| `cars_pipeline.ipynb`       | Real-time pipeline notebook                     |
| `/output`                   | Processed output files                          |
| `dags/cars_realtime_dag.py` | Airflow DAG definition                          |

### Running

1. Place `cars_realtime_dag.csv` in the `/dataset` folder
2. The pipeline **automatically detects** the file and starts processing
3. Output is written to `/output` with a **date and time stamp** for clarity
4. If Azure is configured: output is also uploaded to Azure Blob Storage

---
