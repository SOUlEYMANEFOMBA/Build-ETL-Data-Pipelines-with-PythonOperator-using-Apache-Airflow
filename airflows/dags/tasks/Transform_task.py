import sys
import os
import csv

class TransformTask():
     
    def transform_data(self,input_file,destination_path):
            print("begining of transform data")
            if not os.path(destination_path):
                print("folder doesn't exist, untardata probably fail")
                sys.exit(1)
                
            output_file = f"{destination_path}/transformed_data.csv"
            try:
                with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
                    reader = csv.DictReader(infile)
                    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
                    writer.writeheader()
                    for row in reader:
                        row['Vehicle type'] = row['Vehicle type'].upper()
                        writer.writerow(row)
                        
                print(f"Data transfomed and saved to {output_file}")
            except Exception as e:
                print(f'An error occured: {e}')
