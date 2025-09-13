import csv

with open("insurance.csv","r") as insurance_csv:
    insurance = csv.DictReader(insurance_csv)
