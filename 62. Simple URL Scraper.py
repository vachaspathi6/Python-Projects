import requests
from bs4 import BeautifulSoup

def scrape_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    # links = soup.find_all('a')
    # for link in links:
    #     print(link.get('href'))

def main():
    url = input("Enter URL to scrape: ")
    scrape_urls(url)

if __name__ == "__main__":
    main()
