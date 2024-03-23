import shutil

def backup_file(source, destination):
    shutil.copy(source, destination)
    print("File backed up successfully!")

def main():
    source_file = input("Enter source file path: ")
    destination_file = input("Enter destination file path: ")
    backup_file(source_file, destination_file)

if __name__ == "__main__":
    main()
