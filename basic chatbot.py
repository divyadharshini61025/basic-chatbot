while True:
    user = input("You: ").lower()
    if user in ['hi', 'hello']:
        print("Bot: Hi!")
    elif user in ['how are you']:
        print("Bot: I'm fine, thanks!")
    elif user == 'bye':
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand.")
