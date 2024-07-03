import re

rules = {
    "Hello": "Hi there!",
    "Hi":"Hello, How can I help you?",
    "What's your name?": "My name is Bot!",
    "What can you do?": "I can chat with you!",
    "Thank you": "You're welcome"
}

def match_rule(rules, statement):
    for pattern, response in rules.items():
        if re.search(pattern, statement):
            return response

while True:
    statement = input("You: ")
    response = match_rule(rules, statement)
    if response:
        print("Bot:", response)
    else:
        print("Bot: I'm sorry, I don't understand")

