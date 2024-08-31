import unittest
from airflow.models import DagBag
from airflow.utils.db import initdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from airflow import settings

class TestExampleDag(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.engine =create_engine('sqlite:///:memory:') ## Crée une base de données SQLite temporaire qui est stockée en mémoire et non sur le disque. Utile pour les tests pour éviter les effets secondaires sur une base de données persistante
        cls.session = sessionmaker(cls.engine)
        settings.engine=cls.engine
        initdb()   ## Initialise la base de données Airflow avec les tables nécessaires pour exécuter les tests.
        # Configure DagBag pour rechercher les DAGs dans le répertoire correct
        cls.dagbag = DagBag(dag_folder="/workspace/airflow/dags", include_examples=False)
        print(f"DAGs chargés : {list(cls.dagbag.dags.keys())}")
        print(f"Erreurs de chargement des DAGs : {cls.dagbag.import_errors}")

        if not cls.dagbag.dags:
            raise Exception("Aucun DAG chargé")
        
    def test_etl_toll_data(self):
        dag = self.dagbag.get_dag(dag_id="ETL_toll_DATA")
        
        self.assertIsNotNone(dag)  # Vérifie que le DAG est chargé
        
        self.assertEqual(len(dag.tasks), 2)  # Vérifie que le DAG contient 2 tâches

if __name__=='__main__':
    unittest.main()
