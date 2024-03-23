import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    length = int(input("Enter password length: "))
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
