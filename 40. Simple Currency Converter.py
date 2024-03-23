## To run this project you would need an API KEY. You can get that by signing in the FREE Plan on the following link. 
## Link - https://app.exchangerate-api.com/sign-up

import requests

def convert_currency(amount, from_currency, to_currency):
    api_key = "YOUR_API_KEY"
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    conversion_rate = data["rates"][to_currency]
    converted_amount = amount * conversion_rate
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")

def main():
    amount = float(input("Enter amount: "))
    from_currency = input("Enter from currency: ").upper()
    to_currency = input("Enter to currency: ").upper()
    convert_currency(amount, from_currency, to_currency)

if __name__ == "__main__":
    main()
