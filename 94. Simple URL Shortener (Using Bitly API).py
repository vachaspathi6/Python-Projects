## To run this code you would need Bitly API key...

import requests

def shorten_url(url, token):
    endpoint = "https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "long_url": url
    }
    response = requests.post(endpoint, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        print("Shortened URL:", data["link"])
    else:
        print("Failed to shorten URL")

def main():
    url = input("Enter URL to shorten: ")
    token = input("Enter your Bitly API token: ")
    shorten_url(url, token)

if __name__ == "__main__":
    main()
