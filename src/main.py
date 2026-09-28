from llm import ask_llm

print("Cognitive Assistant System starting...")

# CAS asks for your name => how she should adress you. When the name is received she will exclude any empty space, if the name is empty it'll use Miss instead.
name = input("What is your name? ").strip()
if not name:
    name = "Miss"
print(f"Hello, {name}!\nHow could I assist you today?")

# loop for user commands. ignores empty commands requiring an actual input suggesting help
while True:
    user_input = input("> ").strip()
    if user_input == "":
        print("Please enter a command or type 'help' for assistance.")
        continue
    elif user_input.lower() in ["exit", "quit"]:
        print("Goodbye! Have a great day!")
        break
    elif user_input.lower() == "help":
        print("Available commands: \n- help\n- exit/quit")
    else:
        response=ask_llm(user_input)
        print(f"CAS: {response}")