from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="yellow_taxi_pipeline",
    start_date=datetime(2026, 5, 1),
    schedule="20 7 4 5 *",
    catchup=False,
    tags=["yellow-taxi", "batch"],
) as dag:
    run_notebook = BashOperator(
        task_id="run_notebook",
        bash_command=(
            "jupyter nbconvert "
            "--to notebook "
            "--execute "
            "/opt/airflow/taxi_pipeline.ipynb "
        ),
    )
