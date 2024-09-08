# pip install cryptography
from cryptography.fernet import Fernet
from airflows.dags.tasks.Download_task import DownloadTask
from airflows.dags.tasks.Extract_task import ExtractTask
from airflows.dags.tasks.Transform_task import TransformTask
from airflows.dags.tasks.Load_task import LoadTask
import secrets
def main():
    # # Génère une clé Fernet
    # key = Fernet.generate_key()
    # print(key.decode())  # Imprime la clé générée
    
    print(secrets.token_urlsafe(32))

    url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz"
    downloadTask=DownloadTask(url)
    extractTask=ExtractTask()
    transformTask=TransformTask()
    loadTask=LoadTask()
        
    # Chemin de destination pour le fichier tar téléchargé
    destination_tar ="/workspace/airflows/data_tar"
    # Chemin pour extraire le fichier tar
    destination ="/workspace/airflows/data_tar/tolldata.tgz"
    extractfolder="/workspace/airflows/extract_folder"
    csv_file = "/workspace/airflows/extract_folder/vehicle-data.csv"
    tsv_file="/workspace/airflows/extract_folder/tollplaza-data.tsv"
    fixed_dataset_file="/workspace/airflows/extract_folder/payment-data.txt"
    # op_args=["/workspace/airflows/extract_folder/csv_data.csv","/workspace/airflows/extract_folder/tsv_data.csv","/workspace/airflows/extract_folder/fixed_width_data.csv",extractfolder]
    downloadTask.download_dataset(destination_tar)
    downloadTask.untar_dataset(destination, extractfolder)
    # extractTask.extract_data_from_csv(csv_file,extractfolder)
    # extractTask.extract_data_from_tsv(tsv_file,extractfolder)
    # extractTask.extract_data_from_fixed_width(fixed_dataset_file,extractfolder)
    # extractTask.consolidate_data("/workspace/airflows/extract_folder/csv_data.csv","/workspace/airflows/extract_folder/tsv_data.csv","/workspace/airflows/extract_folder/fixed_width_data.csv",extractfolder)
    # transformTask.transform_data("/workspace/airflows/extract_folder/extracted_data.csv",extractfolder)
    # loadTask.load_in_postgres_tab("/workspace/airflows/extract_folder/transformed_data.csv")
if __name__=="__main__" :
    main()