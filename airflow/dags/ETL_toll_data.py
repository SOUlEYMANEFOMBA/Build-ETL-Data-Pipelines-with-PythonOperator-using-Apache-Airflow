from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import tarfile as tar

def download_dataset():
    
    url =" https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz"
    
    ##Chemin de destination pour le fichier tar télecharger
    destination_tar="C:\Users\soule\Desktop\ETL\Build-ETL-Data-Pipelines-with-PythonOperator-using-Apache-Airflow\airflow\data_tar"
    
    #Télechargement du fichier tar 
    response=requests.get(url)
    
    with open(destination_tar,"wb") as file:
        file.write(response.content)
    
def untar_dataset():
    
    ##Chemin de destination pour le fichier tar télecharger
    destination_tar="C:\Users\soule\Desktop\ETL\Build-ETL-Data-Pipelines-with-PythonOperator-using-Apache-Airflow\airflow\data_tar"
    #chemin pour untar le fichier tar 
    extract_folder="C:\Users\soule\Desktop\ETL\Build-ETL-Data-Pipelines-with-PythonOperator-using-Apache-Airflow\airflow\extract_foder"
    
    ##untar dataset
    with open(destination_tar,'r') as file :
        tar.extractall(path=extract_folder)

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


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 8, 18),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

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