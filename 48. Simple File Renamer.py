import os

def rename_files(directory):
    for filename in os.listdir(directory):
        if filename.startswith("old_prefix"):
            new_filename = filename.replace("old_prefix", "new_prefix")
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed {filename} to {new_filename}")

def main():
    directory = input("Enter directory path: ")
    rename_files(directory)

if __name__ == "__main__":
    main()
