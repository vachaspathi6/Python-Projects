import random

def main():
    print("Welcome to the Text-Based RPG Game!")
    player_name = input("Enter your name: ")
    print(f"Hello, {player_name}! Let's begin your adventure.")

    player_health = 100
    enemy_health = random.randint(50, 100)

    print("You encountered an enemy!")
    while player_health > 0 and enemy_health > 0:
        print(f"\nYour Health: {player_health}")
        print(f"Enemy's Health: {enemy_health}")

        action = input("\nChoose your action (attack/heal): ").lower()

        if action == "attack":
            damage = random.randint(5, 20)
            enemy_health -= damage
            print(f"You attacked the enemy and dealt {damage} damage!")
        elif action == "heal":
            heal_amount = random.randint(10, 25)
            player_health = min(100, player_health + heal_amount)
            print(f"You healed yourself and restored {heal_amount} health!")
        else:
            print("Invalid action! Choose 'attack' or 'heal'.")

        if enemy_health > 0:
            enemy_damage = random.randint(5, 15)
            player_health = max(0, player_health - enemy_damage)
            print(f"The enemy attacked you and dealt {enemy_damage} damage!")

    if player_health <= 0:
        print("You lost! Game over.")
    else:
        print("Congratulations! You defeated the enemy!")

if __name__ == "__main__":
    main()
