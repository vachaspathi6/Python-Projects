def chatbot():
    responses = {
        "hi": "Hello!",
        "how are you?": "I'm good, thank you!",
        "bye": "Goodbye!"
    }
    while True:
        user_input = input("You: ").lower()
        if user_input in responses:
            print("Chatbot:", responses[user_input])
        else:
            print("Chatbot: Sorry, I don't understand.")

def main():
    print("Welcome to Chatbot!")
    chatbot()

if __name__ == "__main__":
    main()
