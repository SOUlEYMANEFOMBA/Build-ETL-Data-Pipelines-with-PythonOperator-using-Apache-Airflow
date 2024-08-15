from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
}

with DAG(dag_id='my_dag', default_args=default_args, schedule_interval='@daily') as dag:
    start = DummyOperator(task_id='start')

    start
