import unittest
from airflow.models import DagBag

class TestExampleDag(unittest.TestCase):
    
    def setUp(self):
        self.dagbag = DagBag()
        
    def test_etl_toll_data(self):
        dag = self.dagbag.get_dag(dag_id="etl_toll_data")
        
        self.assertIsNotNone(dag)  # Vérifie que le DAG est chargé
        
        self.assertEqual(len(dag.tasks), 2)  # Vérifie que le DAG contient 2 tâches
