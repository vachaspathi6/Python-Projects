import random
import string

passwords = {}

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def add_password(service):
    password = input("Enter service password: ")
    passwords[service] = password
    print(f"Password for {service} added successfully!")

def view_password(service):
    if service in passwords:
        print(f"Password for {service}: {passwords[service]}")
    else:
        print(f"No password found for {service}.")

def main():
    while True:
        print("\n1. Add Password")
        print("2. View Password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            service = input("Enter service name: ")
            add_password(service)
        elif choice == '2':
            service = input("Enter service name: ")
            view_password(service)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
