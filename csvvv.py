import csv

with open('ccc.scv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        