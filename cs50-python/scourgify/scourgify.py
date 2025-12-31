from sys import argv, exit
import csv

if len(argv)!=3:
    if len(argv)>3:
        exit('Too few command-line arguments')
    else:
        exit('Too many command-line arguments')

input = argv[1]
output = argv[2]


try:
    with open(input, 'r') as infile:
        reader = csv.DictReader(infile)
        with open(output, 'w') as outfile:
            writer = csv.DictWriter(outfile, fieldnames = ['first','last','house'])
            writer.writeheader()
            for row in reader:
                last, first = row['name'].split(',')
                house = row['house']
                entry = {'first':first.strip(),'last':last, 'house': house}
                writer.writerow(entry)

except FileNotFoundError:
    exit(f'Could not read {input}')

