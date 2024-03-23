def respond(input_text):
    if "hello" in input_text.lower():
        return "Hello! How can I assist you?"
    elif "bye" in input_text.lower():
        return "Goodbye! Have a great day!"
    elif input_text.lower()=="take my order":
        return "OK, Can I have your order please??"
    
    ## keep on adding more elifs

    else:
        return "I'm sorry, I didn't understand that."

def main():
    print("Chatbot: Hello! How can I assist you?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
