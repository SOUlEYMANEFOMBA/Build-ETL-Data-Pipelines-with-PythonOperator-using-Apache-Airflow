from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 8, 18),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def download_dataset():
    pass

def untar_dataset():
    pass

def extract_data_from_csv():
    pass

def extract_data_from_tsv():
    pass

def extract_data_from_fixed_width():
    pass

def consolidate_data():
    pass

def transform_data():
    pass

dag = DAG(
    dag_id="ETL_toll_DATA",
    default_args=default_args,
    schedule_interval='@daily',
    description='Apache Airflow',
)

start = PythonOperator(
    task_id='start',
    python_callable=transform_data,
    dag=dag,
)

start