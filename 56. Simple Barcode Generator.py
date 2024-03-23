import barcode
from barcode.writer import ImageWriter

def generate_barcode(data, barcode_type):
    barcode_class = barcode.get_barcode_class(barcode_type)
    barcode_instance = barcode_class(data, writer=ImageWriter())
    filename = barcode_instance.save(f"barcode_{data}")
    print(f"Barcode saved as {filename}")

def main():
    data = input("Enter data for barcode: ")
    barcode_type = input("Enter barcode type (EAN13, UPC, CODE128, etc.): ")
    generate_barcode(data, barcode_type)

if __name__ == "__main__":
    main()
