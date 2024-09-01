import unittest
from unittest.mock import patch, MagicMock
from airflow.models import DagBag
from airflow.utils.db import initdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from airflow import settings
import requests
import tarfile
from  dags.ETL_toll_data import download_dataset, untar_dataset

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

    def test_etl_toll_data_dags_exist(self):
        dag = self.dagbag.get_dag(dag_id="ETL_toll_DATA")
        self.assertIsNotNone(dag)
        self.assertEqual(len(dag.tasks), 2)

    @patch('dags.ETL_toll_data.requests.get')  # Mock la requête réseau
    def test_download_dataset(self, mock_get):
        # Configure le mock pour renvoyer un faux objet de réponse
        mock_response = MagicMock()
        mock_response.content = b'Fake content'
        mock_get.return_value = mock_response

        # Appelle la fonction et vérifie qu'elle s'exécute sans erreur
        download_dataset()

        # Vérifie que la requête a bien été faite
        mock_get.assert_called_once_with("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz")

    @patch('dags.ETL_toll_data.tar.open')  # Mock l'ouverture du fichier tar
    def test_untar_dataset(self, mock_tar_open):
        # Configure le mock pour simuler une ouverture de tar
        mock_tar = MagicMock()
        mock_tar_open.return_value.__enter__.return_value = mock_tar

        # Appelle la fonction et vérifie qu'elle s'exécute sans erreur
        untar_dataset()

        # Vérifie que la méthode extractall a été appelée
        mock_tar.extractall.assert_called_once_with(path="C:/Users/soule/Desktop/ETL/Build-ETL-Data-Pipelines-with-PythonOperator-using-Apache-Airflow/airflow/extract_folder")

if __name__ == '__main__':
    unittest.main()
