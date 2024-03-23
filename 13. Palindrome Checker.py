def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

def main():
    text = input("Enter text: ")
    if is_palindrome(text):
        print("Palindrome!")
    else:
        print("Not a palindrome.")

if __name__ == "__main__":
    main()
