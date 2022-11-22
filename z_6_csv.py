import csv

with open('ccc.scv') as f:
    reader = csv.reader(f)
    header = next(reader)
    print('Headers: ', 'headers')
    for row in reader:
        print(row)
