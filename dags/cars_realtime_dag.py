from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'retries': 0,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='cars_pipeline',
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule='*/5 * * * *',
    catchup=False,
) as dag:

    # Stap 1: Wacht tot er een CSV in de input folder staat
    wait_for_csv = FileSensor(
        task_id='wait_for_csv',
        filepath='/opt/airflow/dataset/*.csv',
        fs_conn_id='fs_default',
        poke_interval=30,       # elke 30 seconden checken
        timeout=60 * 10,        # max 10 minuten wachten
        mode='poke',
    )

    # Stap 2: Run de notebook zodra het bestand gevonden is
    run_notebook = BashOperator(
        task_id='run_notebook',
        bash_command=(
            'jupyter nbconvert --to notebook --execute '
            '/opt/airflow/cars_pipeline.ipynb'
        ),
    )

    # Stap 3: Verplaats het CSV naar archive zodat de sensor niet opnieuw triggert
    archive_csv = BashOperator(
        task_id='archive_csv',
        bash_command=(
            'mkdir -p /opt/airflow/dataset/archive && '
            'mv /opt/airflow/dataset/*.csv /opt/airflow/dataset/archive/'
        ),
    )

    wait_for_csv >> run_notebook >> archive_csv
