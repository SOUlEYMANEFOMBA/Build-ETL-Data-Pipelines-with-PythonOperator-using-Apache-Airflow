import tarfile as tar 
import requests

class DownloadTask():
    '''cette classe permet de télécharger les données et les dezipper'''
    def __init__(self, url):
        self.url = url
    
    def download_dataset(self, destination_tar):
        # Téléchargement du fichier tar
        response = requests.get(self.url)
        with open(destination_tar, "wb") as file:
            file.write(response.content)

    def untar_dataset(self,destination_tar,extract_folder):
        # Extraction du dataset
        with tar.open(destination_tar, "r:gz") as file:
            file.extractall(path=extract_folder)

