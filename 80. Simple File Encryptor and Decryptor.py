def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        encrypted_text += chr(ord(char) + key)
    return encrypted_text

def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        decrypted_text += chr(ord(char) - key)
    return decrypted_text

def main():
    text = input("Enter text to encrypt: ")
    key = int(input("Enter encryption key: "))
    encrypted_text = encrypt(text, key)
    print("Encrypted Text:", encrypted_text)
    decrypted_text = decrypt(encrypted_text, key)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
