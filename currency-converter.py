def currency_converter(amount, from_currency, to_currency):
    exchange_rates = {
        'USD': {
            'EUR': 0.86,
            'GBP': 0.76,
            'JPY': 111.38
        },
        'EUR': {
            'USD': 1.16,
            'GBP': 0.88,
            'JPY': 128.95
        },
        'GBP': {
            'USD': 1.32,
            'EUR': 1.14,
            'JPY': 146.63
        },
        'JPY': {
            'USD': 0.009,
            'EUR': 0.0078,
            'GBP': 0.0068
        }
    }
    
    if from_currency == to_currency:
        return amount
    
    try:
        converted_amount = amount / exchange_rates[from_currency][to_currency]
        return converted_amount
    
    except KeyError:
        print("Invalid currency")
        return None

# Get user input
amount = float(input("Enter the amount: "))
from_currency = input("Enter the source currency: ").upper()
to_currency = input("Enter the target currency: ").upper()

converted_amount = currency_converter(amount, from_currency, to_currency)

if converted_amount:
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
