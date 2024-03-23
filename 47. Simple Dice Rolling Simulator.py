import random

def roll_dice():
    return random.randint(1, 6)

def main():
    while True:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print("You rolled:", result)
        choice = input("Roll again? (yes/no): ").lower()
        if choice != 'yes':
            break

if __name__ == "__main__":
    main()
