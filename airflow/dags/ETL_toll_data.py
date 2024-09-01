from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from tasks.Download_task import  DownloadTask


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
# Initialisation de la classe avec l'URL
etl_task=DownloadTask(url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz")

# Chemin de destination pour le fichier tar téléchargé
destination_tar = "C:/Users/soule/Desktop/ETL/Build-ETL-Data-Pipelines-with-PythonOperator-using-Apache-Airflow/airflow/data_tar"
download_task = PythonOperator(
    task_id='download_dataset',
    python_callable=etl_task.download_dataset(destination_tar),
    dag=dag,
)

 # Chemin pour extraire le fichier tar
extract_folder = "C:/Users/soule/Desktop/ETL/Build-ETL-Data-Pipelines-with-PythonOperator-using-Apache-Airflow/airflow/extract_folder"
untar_task = PythonOperator(
    task_id='untar_dataset',
    python_callable=etl_task.untar_dataset(destination_tar,extract_folder),
    dag=dag,
)

download_task >> untar_task
