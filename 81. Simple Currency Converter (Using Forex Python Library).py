from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")

def main():
    amount = float(input("Enter amount: "))
    from_currency = input("Enter from currency: ").upper()
    to_currency = input("Enter to currency: ").upper()
    convert_currency(amount, from_currency, to_currency)

if __name__ == "__main__":
    main()
