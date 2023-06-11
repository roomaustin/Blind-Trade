import pyttsx3

# Initialize the Speech Engine
engine = pyttsx3.init()

class User:
    def __init__(self, name):
        self.name = name

    def ask_question(self):
        engine.say("What would you like to do today?")
        engine.runAndWait()
        self.action = input()

    def respond(self):
        if "shop" in self.action:
            engine.say("Opening the shopping menu.")
            engine.runAndWait()
            # Further code to open shopping menu
        elif "order" in self.action:
            engine.say("Opening your orders.")
            engine.runAndWait()
            # Further code to open orders
        else:
            engine.say("Sorry, I didn't understand that.")
            engine.runAndWait()


# Usage
user = User("John")
user.ask_question()
user.respond()
