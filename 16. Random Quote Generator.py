import requests

def fetch_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        return response.json()["content"]
    return None

def main():
    quote = fetch_quote()
    if quote:
        print("Random Quote:")
        print(quote)
    else:
        print("Failed to fetch quote.")

if __name__ == "__main__":
    main()
