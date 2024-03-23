import requests
import shutil

def download_photo(url, filename):
    response = requests.get(url, stream=True)
    with open(filename, 'wb') as file:
        shutil.copyfileobj(response.raw, file)
    print("Photo downloaded successfully!")

def main():
    url = input("Enter photo URL: ")
    filename = input("Enter filename to save photo: ")
    download_photo(url, filename)

if __name__ == "__main__":
    main()
