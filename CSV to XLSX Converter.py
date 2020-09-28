import pandas as pd
import os
import openpyxl

path = (PATH) #Enter the file path here as a raw string

folder = [os.path.splitext(filename)[0] for filename in os.listdir(path)] #Splits extension from the filename

for files in folder:
    read_file = pd.read_csv('PATH'+files+'.csv') #Reads the CSV file, enter path
    write_file = read_file.to_excel('PATH'+files+'.xlsx', index=False) #Writes the file to Excel, enter path
