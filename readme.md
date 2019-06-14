# Description
This tool helps you get BIC for a defined list of IBANs and exports them to a CSV file.

# Installation
- Install python: brew install python
- Install packages: pip3 install schwifty kontocheck

# /bic_for_iban : Generating BICs for a list of IBANs
- Place all your IBANs (one per line) into ibans.csv file.
- Run the script: python3 convert.py
- Check the bics.csv for the list

# /bank_name : Generating bank names for list of bank codes
- Place all your bank codes (one per line) into bank_codes.csv file.
- Run the script: python3 convert.py
- Check the bank_names.csv for the list
