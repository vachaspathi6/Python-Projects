import requests

def check_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("URL is reachable.")
        else:
            print("URL is not reachable.")
    except requests.ConnectionError:
        print("Could not connect to the URL.")

def main():
    url = input("Enter URL to check: ")
    check_url(url)

if __name__ == "__main__":
    main()
