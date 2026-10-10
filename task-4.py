def get_reply(text):
    if text in ["hi", "hello", "hey"]:
        return "Hi!"
    elif "how are you" in text:
        return "I'm fine, thanks! What about you?"
    elif "your name" in text:
        return "I'm just a small python chatbot."
    elif "what can you do" in text or text == "help":
        return "You can say hello, ask how I am, ask my name, or type bye."
    elif "thank" in text:
        return "No problem!"
    elif text in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."


print("Bot: Hello! Type bye when you want to stop.")

while True:
    user = input("You: ").lower().strip()

    if user == "":
        print("Bot: Say something :)")
        continue

    answer = get_reply(user)
    print("Bot:", answer)

    if user in ["bye", "goodbye", "exit", "quit"]:
        break