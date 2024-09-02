import unittest
from airflow.models import DagBag
from airflow.utils.db import initdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from airflow import settings
from  airflows.tasks.Download_task import DownloadTask
from unittest.mock import patch, mock_open, MagicMock

class TestExampleDag(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        cls.session = sessionmaker(bind=cls.engine)()
        settings.engine = cls.engine
        initdb()

        cls.dagbag = DagBag(dag_folder="/workspace/airflow/dags", include_examples=False)
        print(f"DAGs chargés : {list(cls.dagbag.dags.keys())}")
        print(f"Erreurs de chargement des DAGs : {cls.dagbag.import_errors}")

        if not cls.dagbag.dags:
            raise Exception("Aucun DAG chargé")
        
    def SetUp(self):
        self.url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz"
        self.downloadTask=DownloadTask(self.url)
        
        # Chemin de destination pour le fichier tar téléchargé
        self.destination_tar ="/workspace/airflow/data_tar"
        # Chemin pour extraire le fichier tar
        self.extractfolder="/workspace/airflow/extract_folder"
    def test_etl_toll_data_dags_exist(self):
        dag = self.dagbag.get_dag(dag_id="ETL_toll_DATA")
        self.assertIsNotNone(dag)
        self.assertEqual(len(dag.tasks), 2)

    @patch('tasks.Download_task.requests.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_download_dataset(self, mock_open, mock_get):
        # Simuler une réponse de requête avec du contenu factice
        mock_get.return_value.content = b'This is a test file'
        
        # Appeler la méthode download_dataset
        self.downloadTask.download_dataset(self.destination_tar)
        
        # Vérifier que la requête a été effectuée
        mock_get.assert_called_once_with(self.url)
        
        # Vérifier que le fichier a été écrit avec le bon contenu
        mock_open().write.assert_called_once_with(b'This is a test file')
    
    @patch('tasks.Download_task.tar.open')
    @patch('os.path.exists')
    def test_untar_dataset(self, mock_tar_open, mock_exists):
        # Simuler l'existence du fichier tar et du dossier de destination
        mock_exists.side_effect = lambda x: x == self.destination_tar
        
        mock_file = MagicMock()
        mock_tar_open.return_value.__enter__.return_value = mock_file
        
        # Appeler la méthode untar_dataset
        self.downloadTask.untar_dataset(self.destination_tar, self.extractfolder)
        
        # Vérifier que tar.open a été appelé avec le bon fichier
        mock_tar_open.assert_called_once_with(self.destination_tar, "r:gz")
        
        # Vérifier que les fichiers ont été extraits
        mock_file.extractall.assert_called_once_with(path=self.extractfolder)

if __name__ == '__main__':
    unittest.main()
