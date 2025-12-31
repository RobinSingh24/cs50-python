from sys import exit,argv
import tabulate
import csv

if len(argv)!=2:
    if len(argv)>2:
        exit('Too many command-line arguments')
    else:
        exit('Too few command-line arguments')

if not argv[1].endswith('.csv'):
    exit('Not a CSV file')

try:
    rows = []
    header = []
    filename = argv[1]
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for _ in reader:
            rows.append(_)

    header = rows[0:1]
    header = [item for sublist in header for item in sublist]
    rows = rows[1:]

    print(tabulate.tabulate(rows, header, tablefmt="grid"))

except FileNotFoundError:
    exit('File does not exist')
