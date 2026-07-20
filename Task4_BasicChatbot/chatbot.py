print("Welcome to Mini Chatbot")
print("Enter 'quit' to end the conversation.\n")

while True:
    message = input("You: ").lower()

    if message == "hi":
        print("Bot: Hello there!")

    elif message == "who are you":
        print("Bot: I am a simple Python chatbot.")

    elif message == "good morning":
        print("Bot: Good morning! Have a great day.")

    elif message == "help":
        print("Bot: Try saying hi, who are you, good morning, help, or quit.")

    elif message == "quit":
        print("Bot: See you later!")
        break

    else:
        print("Bot: I couldn't understand that.")
