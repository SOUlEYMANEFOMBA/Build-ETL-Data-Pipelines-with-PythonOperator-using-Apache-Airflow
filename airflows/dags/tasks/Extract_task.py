import os
import pandas as pd 
import csv

class ExtractTask():
    
    def extract_data_from_csv(self,csv_file,extract_folder):
                print("begining of cvs extrac file")
                if not os.path.exists(extract_folder):
                    os.makedirs(extract_folder)
                #Easy methode
                # vehicle_data_csv=pd.read_csv(csv_file,sep=",")
                # variables=["Rowid", "Timestamp", "Anonymized Vehicle number", "Vehicle type"]
                # csv_data=vehicle_data_csv[variables]
                #output_file = f"{extract_folder}/csv_data.csv"
                #csv_data.to_csv(output_file,index=False)
                # Définir le chemin complet du fichier de sortie en utilisant une f-string
                output_file = f"{extract_folder}/csv_data.csv"
                try :
                    with open(csv_file,'r') as infile, open(output_file,'w') as outfile:
                        writer = csv.writer(outfile)
                        writer.writerow(["Rowid", "Timestamp", "Anonymized Vehicle number", "Vehicle type"])
                        for line in infile:
                            row=line.split(',')
                            writer.writerow([row[0],row[1],row[2],row[3]])
                    print(f"Vehicle-data.csv extracted and saved to {output_file}")
                except Exception as e:
                    print(f"An error occured: {e}")

    def extract_data_from_tsv(self,tsv_file, extract_folder):
            if not os.path.exists(extract_folder):
                os.makedirs(extract_folder)
            output_file=f"{extract_folder}/tsv_data.csv"
            try :
                with open(tsv_file,'r') as infile, open(output_file,'w') as outfile:
                    writer=csv.writer(outfile)
                    writer.writerow(["Number of axles", "Tollplaza id","Tollplaza code"])
                    for line in infile:
                        row=line.split('\t')
                        writer.writerow([row[0],row[1],row[2]])
                print(f"Tollplaza-data.tsv extracted and saved to {output_file}")
            except Exception as e:
                print(f"An error occured:{e}")
        

    def extract_data_from_fixed_width(self,payement_data_txt, extract_folder):
                if not os.path.exists(extract_folder):
                    print("Folder doesn't exist, untardata probably fail")
                output_file=f"{extract_folder}/fixed_width_data.csv"
                try :
                    with open(payement_data_txt,'w') as infile, open(output_file,'w') as outfile:
                            writer=csv.writer(outfile)
                            writer.writerow(["Type of Payment code", "Vehicle Code"])
                            for line in infile:
                                writer.writerow([line[0:6].strip(), line[6:12].strip()])
                    print(f"extract_data_from_fixed_width extracted and saved to {output_file}")
                except Exception as e :
                    print(f"An error occured: {e}")
              
    