snippets = {}

def add_snippet(name, code):
    snippets[name] = code
    print("Snippet added successfully!")

def view_snippets():
    if snippets:
        print("Snippets:")
        for name, code in snippets.items():
            print(f"{name}: {code}")
    else:
        print("No snippets found.")

def main():
    while True:
        print("\n1. Add Snippet")
        print("2. View Snippets")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter snippet name: ")
            code = input("Enter snippet code: ")
            add_snippet(name, code)
        elif choice == '2':
            view_snippets()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
