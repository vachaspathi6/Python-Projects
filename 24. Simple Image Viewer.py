from PIL import Image

def view_image(image_path):
    try:
        img = Image.open(image_path)
        img.show()
    except FileNotFoundError:
        print("Image not found.")

def main():
    image_path = input("Enter image path: ")
    view_image(image_path)

if __name__ == "__main__":
    main()
