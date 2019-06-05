from schwifty import IBAN # Library from https://pypi.org/project/schwifty/
import csv

iban_reader = csv.reader(open('ibans.csv', mode='r'), delimiter=';')
bic_writer = csv.writer(open('bics.csv', mode='w'), delimiter=';')

for row in iban_reader:
    iban = IBAN(row[0])
    bic = iban.bic
    bic_writer.writerow([iban.compact, iban.bic])