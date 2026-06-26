def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."

print("Simple chatbot")
print("Type 'bye' to exit.\n")

while True:
    user_message = input("You: ")
    response = chatbot_response(user_message)
    print("Bot: ", response)
    if response == "Goodbye!":
        break