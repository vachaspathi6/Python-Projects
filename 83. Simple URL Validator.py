import re

def validate_url(url):
    pattern = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https:// or ftp://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'localhost|' # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(pattern, url) is not None

def main():
    url = input("Enter URL to validate: ")
    if validate_url(url):
        print("Valid URL")
    else:
        print("Invalid URL")

if __name__ == "__main__":
    main()
