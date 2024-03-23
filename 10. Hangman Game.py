import random

def choose_word():
    words = ['Algorithm', 'Variable', 'Function', 'Method', 'Class', 'Object', 
            'Loop', 'Condition', 'Statement', 'Expression', 'Syntax', 'Compiler', 
            'Interpreter', 'Debugging', 'Testing', 'Multiprocessing', 'Networking',
            'Repository', 'Merge', 'Branch', 'Commit', 'Hashing', 'Multithreading', 
            'Pull Request', 'API', 'Library', 'Framework', 'Module', 
            'Package', 'Dependency', 'Exception', 'Sorting', 'Searching' 
            'String', 'Integer', 'Float', 'Boolean', 'List', 'Tuple', 
            'Dictionary', 'Set', 'Stack', 'Queue', 'Binary', 'Recursion', 
            ]
    
    return random.choice(words)

def play_game():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        display_word = ''.join(letter if letter in guessed_letters else '_' for letter in word)
        print("Word:", display_word)

        if '_' not in display_word:
            print("Congratulations! You guessed the word:", word)
            break

        guess = input("Enter a letter: ").lower()
    
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess! Attempts left:", attempts)
        


    if attempts == 0:
        print("You ran out of attempts! The word was:", word)

def main():
    print("Hangman Game")
    play_game()

if __name__ == "__main__":
    main()
