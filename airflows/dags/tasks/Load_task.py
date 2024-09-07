import psycopg2
import csv

class LoadTask():
    
    def load_in_postgres_tab(self,file):
        conn=psycopg2.connect("host=postgres,port=5432,dbname=airflow,user=airflow,password=airflow")
        ##On va créer une object cursor qui nous permettra de requeter notre base de donnée
        cur=conn.cursor()
        cur.execute("""
                     CREATE TABLE IF NOT EXISTS final_database (
                        Rowid SERIAL PRIMARY KEY,
                        Timestamp TIMESTAMP,
                        "Anonymized Vehicle number" TEXT,
                        "Vehicle type" TEXT,
                        "Number of axles" INTEGER,
                        "Tollplaza id" INTEGER,
                        "Tollplaza code" TEXT,
                        "Type of Payment code" TEXT,
                        "Vehicle Code" TEXT
                        )
            """ )
        conn.commit()  ## Pour valider la création de la base de donnée au cas ou il y aurait des erreurs lors de l'insertion des données dans la base 
        
        # with open(file,'r') as infile :
        #     reader=csv.reader(infile)
        #     next(reader) ##skip the header row
        #     for row in reader :
        #         cur.execute( 
        #                      """
        #                     INSERT INTO final_database (
        #                         Timestamp, "Anonymized Vehicle number", "Vehicle type", 
        #                         "Number of axles", "Tollplaza id", "Tollplaza code", 
        #                         "Type of Payment code", "Vehicle Code"
        #                     ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        #                     """,
        #                     row
        #    
        #)
        
        # easy way
        with open(file,'r') as infile:
            next(infile)
            cur.copy_from(infile,'final_database', sep=',',null='')
        conn.commit()
        # cur.execute('SELECT * FROM notes')
        one=cur.fetchone()  ##  retourne le résultat de la première ligne ou None 
        all=cur.fetchall()  ## retourne une liste de chaque ligne du tableau ou une liste vide [] s'il n'y a pas de lignes
        
        print(f"Voici la première ligne de notre base de données: {one}")
        print(f"Liste de chaque ligne du tableau: {all}")
       # Fermeture du curseur et de la connexion
        cur.close()
        conn.close()