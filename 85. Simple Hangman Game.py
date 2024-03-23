import random

def choose_word():
    words = ['python', 'java', 'ruby', 'javascript', 'php']
    return random.choice(words)

def play_hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 7
    while attempts > 0:
        display_word = ''.join(char if char in guessed_letters else '_' for char in word)
        print("Word:", display_word)
        guess = input("Guess a letter: ")
        if guess in word:
            guessed_letters.append(guess)
            if all(char in guessed_letters for char in word):
                print("Congratulations! You guessed the word:", word)
                break
        else:
            attempts -= 1
            print(f"Incorrect guess! You have {attempts} attempts left.")
    else:
        print("Out of attempts! The word was:", word)

def main():
    print("Welcome to Hangman!")
    play_hangman()

if __name__ == "__main__":
    main()
