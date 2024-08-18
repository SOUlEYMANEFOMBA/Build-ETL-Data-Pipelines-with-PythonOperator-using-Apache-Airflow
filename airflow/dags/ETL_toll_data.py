from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 8, 18),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def simple_function():
    print("DAG execution started")

dag = DAG(
    dag_id="ETL_toll_DATA",
    default_args=default_args,
    schedule_interval='@daily',
    description='Apache Airflow',
)

start = PythonOperator(
    task_id='start',
    python_callable=simple_function,
    dag=dag,
)

start