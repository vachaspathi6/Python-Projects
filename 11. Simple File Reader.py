def main():
    filename = input("Enter filename: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("Current content:")
            print(content)
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()
