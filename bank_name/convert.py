import csv
import kontocheck
kontocheck.lut_load()

iban_reader = csv.reader(open('bank_codes.csv', mode='r'), delimiter=',')
bic_writer = csv.writer(open('bank_names.csv', mode='w'), delimiter=',')
bic_writer.writerow(['Bank Code', 'Bank Name'])

for row in iban_reader:
    if len(row[0]) == 8:
        row.append(kontocheck.get_name(row[0],9))
        bic_writer.writerow(row)