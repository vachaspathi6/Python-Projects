import requests
import shutil

def download_image(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, file)
        print("Image downloaded successfully!")
    else:
        print("Failed to download image")

def main():
    url = input("Enter image URL: ")
    filename = input("Enter filename to save image: ")
    download_image(url, filename)

if __name__ == "__main__":
    main()
