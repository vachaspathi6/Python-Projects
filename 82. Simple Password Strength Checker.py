def password_strength(password):
    if len(password) < 8:
        return "Weak"
    elif len(password) < 12:
        return "Moderate"
    else:
        return "Strong"

def main():
    password = input("Enter password: ")
    strength = password_strength(password)
    print("Password Strength:", strength)

if __name__ == "__main__":
    main()
