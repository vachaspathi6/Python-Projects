contacts = {}

def add_contact(name, number):
    contacts[name] = number
    print("Contact added successfully!")

def view_contacts():
    if contacts:
        print("Contacts:")
        for name, number in contacts.items():
            print(f"{name}: {number}")
    else:
        print("No contacts found.")

def main():
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            add_contact(name, number)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
