import os

def display_images(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            print(os.path.join(directory, filename))

def main():
    directory = input("Enter directory containing images: ")
    display_images(directory)

if __name__ == "__main__":
    main()
