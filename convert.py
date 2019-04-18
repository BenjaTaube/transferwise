import csv

with open('transferwise.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    lines = list(reader)

main_header = ['Konto', 'Kontonavn']
saldo_header = ['Inngående saldo', 'Utgående saldo', 'Sum inn på konto', 'Sum ut av konto']
data_header = ['Konto', 'Kontonavn']

dnblines = [main_header]

with open('dnb.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(dnblines)

readFile.close()
writeFile.close()
