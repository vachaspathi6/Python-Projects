from PIL import Image

def resize_image(image_path, new_width, new_height):
    img = Image.open(image_path)
    img = img.resize((new_width, new_height))
    img.save("resized_image.jpg")
    print("Image resized successfully!")

def main():
    image_path = input("Enter image path: ")
    new_width = int(input("Enter new width: "))
    new_height = int(input("Enter new height: "))
    resize_image(image_path, new_width, new_height)

if __name__ == "__main__":
    main()
