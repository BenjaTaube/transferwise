import csv

with open('transferwise.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    transferwise_lines = list(reader)

main_header = ['Konto', 'Kontonavn']
main_header_data = ['transferwise USD balance', 'transferwise USD balance']

# In and outgoing balance calculation
running_balance_after_first_payment = float(transferwise_lines[-1][6])
first_payment_amount = float(transferwise_lines[-1][2])
running_balance_before_first_payment = running_balance_after_first_payment - first_payment_amount

running_balance_after_last_payment = transferwise_lines[1][6]

saldo_header = ['Inngående saldo', 'Utgående saldo']
saldo_header_data = [running_balance_before_first_payment, running_balance_after_last_payment]

data_header = ['Bokført dato', 'Forklarende tekst', 'Inn', 'Ut']
data_header_data = []
transferwise_lines_data = transferwise_lines[1:]

dnblines = [
    main_header,
    main_header_data,
    saldo_header,
    saldo_header_data,
    data_header,
]
for transaction_line in transferwise_lines_data:
    date = transaction_line[1]
    description = transaction_line[4]
    amount = transaction_line[2]
    if float(amount) > 0:
        in_amount = amount
        out_amount = None
    else:
        in_amount = None
        out_amount = amount

    dnblines.append([date, description, in_amount, out_amount])


with open('dnb.csv', 'w', newline='') as writeFile:
    writer = csv.writer(writeFile,)
    writer.writerows(dnblines)

readFile.close()
writeFile.close()
