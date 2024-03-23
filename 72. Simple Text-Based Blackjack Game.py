import random

def draw_card():
    return random.randint(1, 11)

def main():
    player_score = 0
    while True:
        choice = input("Do you want to draw a card? (yes/no): ").lower()
        if choice != 'yes':
            break
        card_value = draw_card()
        player_score += card_value
        print(f"Card drawn: {card_value}")
        print(f"Your current score: {player_score}")
        if player_score > 21:
            print("Busted! You lose.")
            break
    print("Game over.")

if __name__ == "__main__":
    main()
