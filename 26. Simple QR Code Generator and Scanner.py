import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print("QR Code generated successfully!")

def scan_qr_code(image_path):
    try:
        result = decode(Image.open(image_path))
        print("Scanned data:", result[0].data.decode())
    except FileNotFoundError:
        print("Image not found.")

def main():
    print("1. Generate QR Code")
    print("2. Scan QR Code")
    choice = input("Enter your choice: ")

    if choice == '1':
        data = input("Enter data to encode: ")
        filename = input("Enter filename to save QR Code: ")
        generate_qr_code(data, filename)
    elif choice == '2':
        image_path = input("Enter image path: ")
        scan_qr_code(image_path)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
