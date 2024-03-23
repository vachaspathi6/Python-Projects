import os

def list_files(directory):
    files = os.listdir(directory)
    print("Files in directory:")
    for file in files:
        print(file)

def main():
    directory = input("Enter directory path: ")
    list_files(directory)

if __name__ == "__main__":
    main()
