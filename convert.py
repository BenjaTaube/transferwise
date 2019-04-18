import csv

row = ['2', ' Marie', ' California']
row1 = ['2', ' molo', ' mololand']

with open('transferwise.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    lines = list(reader)
    lines[2] = row
    lines[1] = row1

with open('dnb.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)

readFile.close()
writeFile.close()