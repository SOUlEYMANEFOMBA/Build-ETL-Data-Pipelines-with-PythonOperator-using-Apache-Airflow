from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
# import sys
# sys.path.append('/workspace/airflows/tasks')
from tasks.Download_task import  DownloadTask
from tasks.Extract_task import ExtractTask
from tasks.Transform_task import TransformTask
from tasks.Load_task import LoadTask


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 8, 18),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
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
destination_tar = "/opt/airflow/data_tar"
download_task = PythonOperator(
    task_id='download_dataset',
    python_callable=etl_task.download_dataset,
    op_args=[destination_tar],
    dag=dag,
)
#chemin pour retrouver le fichier tar
destination ="/opt/airflow/data_tar/tolldata.tgz"
# Chemin pour extraire le fichier tar
extract_folder = "/opt/airflow/extract_folder"
untar_task = PythonOperator(
    task_id='untar_dataset',
    python_callable=etl_task.untar_dataset,
    op_args=[destination,extract_folder],
    dag=dag,
)

extract_task=ExtractTask()
csv_file = "/opt/airflow/extract_folder/vehicle-data.csv"
extract_csv_task=PythonOperator(
    task_id='extrac_csv_dataset',
    python_callable=extract_task.extract_data_from_csv,
    op_args=[csv_file,extract_folder],
    dag=dag,
)
tsv_file="/opt/airflow/extract_folder/tollplaza-data.tsv"
extract_tsv_task=PythonOperator(
    task_id='extract_tsv_dataset',
    python_callable=extract_task.extract_data_from_tsv,
    op_args=[tsv_file,extract_folder],
    dag=dag,
)
fixed_dataset_file="/opt/airflow/extract_folder/payment-data.txt"
extract_fixed_dataset_task=PythonOperator(
    task_id='extract_fixed_dataset',
    python_callable=extract_task.extract_data_from_fixed_width,
    op_args=[fixed_dataset_file,extract_folder],
    dag=dag,
)
consolidate_task=PythonOperator(
    task_id='consolidate_dataset',
    python_callable=extract_task.consolidate_data,
    op_args=["/opt/airflow/extract_folder/csv_data.csv","/opt/airflow/extract_folder/tsv_data.csv","/opt/airflow/extract_folder/fixed_width_data.csv",extract_folder],
    dag=dag,
)

transfomed_task=TransformTask()
transfom_task=PythonOperator(
    task_id='transform_dataset',
    python_callable=transfomed_task.transform_data,
    op_args=["/opt/airflow/extract_folder/extracted_data.csv",extract_folder],
    dag=dag,
)

load_task=LoadTask()
loading_task=PythonOperator(
    task_id="londing_into_postgres_data_table",
    python_callable=load_task.load_in_postgres_tab,
    op_args=["/opt/airflow/extract_folder/transformed_data.csv"],
    dag=dag,
)
download_task >> untar_task >>[extract_csv_task,extract_tsv_task,extract_fixed_dataset_task]>> consolidate_task >> transfom_task >> loading_task