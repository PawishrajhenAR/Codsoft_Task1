def respond_to_user_input(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"

    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm here to help you!"

    if "what is your favorite color" in user_input:
        return "I don't have eyes, so I don't have a favorite color!"

    elif "goodbye" in user_input:
        return "Goodbye! Have a great day!"

    elif "thank you" in user_input:
        return "You're welcome!"

    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

def main():
    print("Welcome to the Rule-based Chatbot!")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        else:
            response = respond_to_user_input(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    main()
