import tarfile as tar 
import requests
import os 
class DownloadTask():
    '''cette classe permet de télécharger les données et les dezipper'''
    def __init__(self, url):
        self.url = url
    
    def download_dataset(self, destination_tar):
         # Assurez-vous que le répertoire de destination existe
        if not os.path.exists(destination_tar):
            os.makedirs(destination_tar)
        
        # Définir le nom du fichier à partir de l'URL
        filename = os.path.basename(self.url)
        destination_path = os.path.join(destination_tar, filename)
        
        # Téléchargement du fichier
        response = requests.get(self.url)
        response.raise_for_status()  # Assurez-vous de détecter les erreurs
        
        # Enregistrement du fichier
        with open(destination_path, "wb") as file:
            file.write(response.content)

    def untar_dataset(self,destination_tar,extract_folder):
        if not os.path.exists(extract_folder):
            os.makedirs(extract_folder)
        # Extraction du dataset
        
        with tar.open(destination_tar, "r:gz") as tar_file:
            tar_file.extractall(path=extract_folder)

