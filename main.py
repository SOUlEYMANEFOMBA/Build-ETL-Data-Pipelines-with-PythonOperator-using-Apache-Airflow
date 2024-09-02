# pip install cryptography
from cryptography.fernet import Fernet
from airflows.tasks.Download_task import DownloadTask
def main():
    # # Génère une clé Fernet
    # key = Fernet.generate_key()
    # print(key.decode())  # Imprime la clé générée
    url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz"
    downloadTask=DownloadTask(url)
        
    # Chemin de destination pour le fichier tar téléchargé
    destination_tar ="/workspace/airflow/data_tar"
    # Chemin pour extraire le fichier tar
    destination ="/workspace/airflow/data_tar/tolldata.tgz"
    extractfolder="/workspace/airflow/extract_folder"
    downloadTask.download_dataset(destination_tar)
    downloadTask.untar_dataset(destination, extractfolder)

if __name__=="__main__" :
    main()