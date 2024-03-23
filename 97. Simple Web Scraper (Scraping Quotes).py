import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "http://quotes.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('span', class_='text')
    for quote in quotes:
        print(quote.text)

def main():
    scrape_quotes()

if __name__ == "__main__":
    main()
