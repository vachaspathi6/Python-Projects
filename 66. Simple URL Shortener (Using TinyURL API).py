import requests

def shorten_url(url):
    api_url = "https://api.tinyurl.com/dev/api-create.php"
    response = requests.post(api_url, data={"url": url})
    print(response)
    if response.status_code == 200:
        print("Shortened URL:", response.text)
    else:
        print("Failed to shorten URL")

def main():
    url = input("Enter URL to shorten: ")
    shorten_url(url)

if __name__ == "__main__":
    main()
