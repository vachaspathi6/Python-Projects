import random

def roll_dice():
    return random.randint(1, 6)

def main():
    input("Press Enter to roll the dice...")
    result = roll_dice()
    print("You rolled:", result)

if __name__ == "__main__":
    main()
