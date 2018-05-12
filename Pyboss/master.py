import os 
import csv

#pull in raw data files
csvpath = os.path.join('.',"raw_data","employee_data1.csv")

with open(csvpath, newline ='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter= ',')

    