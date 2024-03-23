import json

def load_passwords():
    try:
        with open("passwords.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_passwords(passwords):
    with open("passwords.json", "w") as file:
        json.dump(passwords, file)

def add_password(passwords, website, username, password):
    passwords[website] = {"username": username, "password": password}
    save_passwords(passwords)
    print("Password added successfully!")

def view_passwords(passwords):
    if passwords:
        print("Stored Passwords:")
        for website, data in passwords.items():
            print(f"Website: {website}, Username: {data['username']}, Password: {data['password']}")
    else:
        print("No passwords stored.")

def main():
    passwords = load_passwords()
    while True:
        print("\n1. Add Password")
        print("2. View Passwords")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            add_password(passwords, website, username, password)
        elif choice == '2':
            view_passwords(passwords)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
