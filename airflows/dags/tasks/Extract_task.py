import os
import pandas as pd 
import csv
import sys

class ExtractTask():
    
    def extract_data_from_csv(self,csv_file,extract_folder):
                print("begining of csv extrac file")
                if not os.path.exists(extract_folder):
                    print("Folder doesn't exist, untardata probably fail")
                    sys.exit(1)
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
            print("begining of tsv extrac file")
            if not os.path.exists(extract_folder):
                print("Folder doesn't exist, untardata probably fail")
                sys.exit(1)
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
                print("begining of fised_data extrac file")
                if not os.path.exists(extract_folder):
                    print("Folder doesn't exist, untardata probably fail")
                    sys.exit(1)
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
                
    def consolidate_data(self,csv_data_file,tsv_data_file,fixed_width_data_file,extract_folder):
                print("begining of consolidate data")
                if not os.path.exists(extract_folder):
                    print("folder doesn't exist, untardata probably fail")
                    sys.exit(1)
                
                output_file = f"{extract_folder}/extracted_data.csv"
                try :
                    with open(csv_data_file,'r') as csvfile, open(tsv_data_file,'r') as tsvfile, open(fixed_width_data_file,'r') as fixedfile, open(output_file,'w') as outfile:
                        csv_reader = csv.reader(csvfile)
                        tsv_reader = csv.reader(tsvfile)
                        fixed_reader = csv.reader(fixedfile)
                        writer=csv.writer(outfile)
                        writer.writerow(["Rowid", "Timestamp", "Anonymized Vehicle number", "Vehicle type", "Number of axles", "Tollplaza id", "Tollplaza code", "Type of Payment code", "Vehicle Code"])
                        next(csv_reader)
                        next(tsv_reader)
                        next(fixed_reader)
                        for csv_row,tsv_row,fixed_row in zip(csv_reader,tsv_reader,fixed_reader):
                            writer.writerow(csv_row,tsv_row,fixed_row)
                    print(f"Data consolidated and saved to {output_file}")
                except Exception as e:
                    print(f"An error occured : {e}")               
                