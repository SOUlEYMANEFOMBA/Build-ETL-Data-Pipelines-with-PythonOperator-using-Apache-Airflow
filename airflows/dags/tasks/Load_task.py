import psycopg2
import csv

class LoadTask():
    
    def load_in_postgres_tab(self,file):
        print("Loading started")
        conn=psycopg2.connect("host=postgres port=5432 dbname=airflow user=airflow password=airflow")
        ##On va créer une object cursor qui nous permettra de requeter notre base de donnée
        cur=conn.cursor()
        # Supprimer la table existante (si elle existe)
        cur.execute("DROP TABLE IF EXISTS final_database")
        cur.execute("""
            CREATE TABLE final_database (
                Rowid SERIAL PRIMARY KEY,
                Timestamp TIMESTAMP,
                "Anonymized Vehicle number" BIGINT,
                "Vehicle type" TEXT,
                "Number of axles" INTEGER,
                "Tollplaza id" TIMESTAMP,
                "Tollplaza code" TEXT,
                "Type of Payment code" TEXT,
                "Vehicle Code" TEXT
            )
        """)
        conn.commit()  ## Pour valider la création de la base de donnée au cas ou il y aurait des erreurs lors de l'insertion des données dans la base 
        
        # # easy way
        with open(file,'r') as infile:
            next(infile)
            cur.copy_from(infile,'final_database', sep=',',null='')
            
        conn.commit()
         # Récupérer et afficher les données insérées
        cur.execute('SELECT * FROM final_database')
        rows = cur.fetchall()  # Retourner toutes les lignes de la table
        print(f"Liste de chaque ligne du tableau: {rows}")
        print("Data load in postgres final_database")
       # Fermeture du curseur et de la connexion
        cur.close()
        conn.close()