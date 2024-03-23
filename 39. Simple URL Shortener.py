import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    print("Shortened URL:", shortened_url)

def main():
    url = input("Enter URL to shorten: ")
    shorten_url(url)

if __name__ == "__main__":
    main()
