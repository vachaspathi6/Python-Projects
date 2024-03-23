def calculate_tip(bill_amount, tip_percentage):
    return bill_amount * (tip_percentage / 100)

def main():
    bill_amount = float(input("Enter bill amount: $"))
    tip_percentage = float(input("Enter tip percentage: "))
    tip = calculate_tip(bill_amount, tip_percentage)
    print("Tip amount: $", tip)

if __name__ == "__main__":
    main()
