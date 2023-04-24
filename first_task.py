import random

"""This is a game, for a number guessing, we created two
functions. One for a guessing number and another for asks 
user if he/she want to play again.
"""


def guessing_game():
    rand_num = random.randint(0, 50)
    #print(rand_num)
    choice = 0
    guess = 0
    user_input = input("Please enter your number: ")
    try:
        user_input = int(user_input)
    except ValueError:
        print("Please enter valid number")
        guessing_game()
    while choice <= 4 and guess == 0:
        if choice == 4:
            print("The number was: ", rand_num)
            break
        elif user_input == rand_num:
            guess += 1
            print("Winner winner, chicken dinner!")
        elif user_input > rand_num:
            print("Your number is higher, enter new one")
            user_input = int(input("Please enter your number: "))
            choice += 1
        else:
            print("Your number is lower, enter new one")
            user_input = int(input("Please enter your number: "))
            choice += 1

guessing_game()


def regame():
    question = input("Do you want to play again (Y or N)?")
    if question == "Y":
        print("Cecxli ainto, tamashi daiwyo")
        guessing_game()
    else:
        print("Thank you for playing!")

regame()


