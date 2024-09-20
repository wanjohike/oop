# install currencyconverter module
from currency_converter import CurrencyConverter

def convert_currency(amount, base_Currency, target_Currency):
    c = CurrencyConverter()
    result = c.convert(amount, base_Currency, target_Currency)
    return result

amount = float(input('Enter the mount to convert: '))
base_currency = input('Enter the base currency: ').upper()
target_currency = input('Enter the target currency: ').upper()

# perform the conversions
converted_amount = convert_currency(amount, base_currency, target_currency)

print(f'{amount} {base_currency} = {converted_amount:}{target_currency}')