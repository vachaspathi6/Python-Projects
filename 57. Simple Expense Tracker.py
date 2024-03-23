class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount):
        self.expenses.append((category, amount))
        print("Expense added successfully!")

    def view_expenses(self):
        if self.expenses:
            print("Expenses:")
            for category, amount in self.expenses:
                print(f"{category}: ${amount}")
        else:
            print("No expenses found.")

def main():
    tracker = ExpenseTracker()
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            tracker.add_expense(category, amount)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
