"""This code can be used to create a simple virtual shopping assistant
    that helps users manage their shopping lists. It allows users to add items
      to their list, remove items from their list, and view their final shopping list.
        The program uses a while loop to keep prompting the user for commands until they choose
           to quit the program."""

shopping_list = []
name= input("Welcome, I am your virtual shopping assistant, please enter your name: ")
def shopping_assistant():
    show_help()
    while True:
        command = input("Enter a command: ")
        if command == "1":
            add_item(shopping_list)
        elif command == "2":
            delete_item(shopping_list)
        elif command == "3":
            show_list(shopping_list)
        elif command == "4":
            quit()
            break
        elif command == "5":
            show_help()

        else:
            print("Invalid command, please try again.")
def show_help():
    print("Hello {}, Here are the available commands, please choose a command:".format(name))
    print(" '1' - Add an item to the shopping list")
    print(" '2' - Remove an item from the shopping list")
    print(" '3' - Show the final shopping list")
    print(" '4' - Quit the shopping assistant")
    print(" '5' - Show again available commands ")
    options = {
        "1": lambda: add_item(shopping_list),
        "2": lambda: delete_item(shopping_list),
        "3": lambda: show_list(shopping_list),
        "4": quit,
        "5": show_help,
    }

def add_item(shopping_list):
    item = input("Enter the item you want to add: ")
    shopping_list.append(item)
    print("{} has been added to the shopping list".format(item))

def delete_item(shopping_list):
    item = input("Enter the item you want to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print("{} has been removed from the shopping list".format(item))
    else:
        print("{} is not in the shopping list".format(item))

def show_list(shopping_list):
    print("Here is your final shopping list:")
    for item in shopping_list:
        print("- {}".format(item))

def quit():
    print("Thanks for visiting, see you later {}!".format(name))

#Now we can start shopping with calling shopping_assistant function

shopping_assistant()









