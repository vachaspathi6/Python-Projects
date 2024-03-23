import os

def list_files(directory):
    print("Files in directory:", directory)
    for filename in os.listdir(directory):
        print(filename)

def main():
    directory = input("Enter directory path: ")
    list_files(directory)

if __name__ == "__main__":
    main()
