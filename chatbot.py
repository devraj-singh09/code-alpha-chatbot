# Basic Rule-Based Chatbot

def chatbot():
    print("================================")
    print("     Welcome to Python Chatbot")
    print("================================")
    print("Type 'bye' to exit the chatbot.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello" or user == "hi":
            print("Bot: Hello! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I'm fine, thank you!")

        elif user == "what is your name":
            print("Bot: My name is Python Bot.")

        elif user == "what can you do":
            print("Bot: I can answer some basic questions.")

        elif user == "thanks" or user == "thank you":
            print("Bot: You're welcome!")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Start the chatbot
chatbot()