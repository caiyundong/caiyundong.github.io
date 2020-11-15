import random


def pss():
    my_choice = input("Please input paper, scissor, stone: ")

    if my_choice not in ['paper', 'scissor', 'stone']:
        print("Error: Wrong input:", my_choice)
        return

    bot_choice = random.choice(['paper', 'scissor', 'stone'])

    print("My choice:", my_choice, "Bot Choice:", bot_choice)

    if (my_choice == 'paper' and bot_choice == 'stone') or (my_choice == 'scissor' and bot_choice == 'paper') or (my_choice == 'stone' and bot_choice == 'scissor'):
        print("You win")
    elif my_choice == bot_choice:
        print("Draw")
    elif (bot_choice == 'paper' and my_choice == 'stone') or (bot_choice == 'scissor' and my_choice == 'paper') or (bot_choice == 'stone' and my_choice == 'scissor'):
        print("You lose")
    else:
        print("Wrong Input")


while True:
    pss()
