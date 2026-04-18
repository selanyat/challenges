#!/usr/bin/env python

import random

# check if user wants to roll
# check if option is valid
# if yes roll dice
# if no stop game

def getUserInput() -> str:
    user_input = input("Do you want to roll a dice [y/n]: ").strip().lower()
    # is valid??
    if user_input not in ["y","n"]:
        print("Invalid Input\nEnter either 'y' or 'n'")
        return getUserInput()

    return user_input

def rollDice() -> tuple:
    return (random.randint(1,6), random.randint(1,6))

while True:
    user_input = getUserInput()

    if user_input == "y":
        print(rollDice())

    else:
        print("Thanks for playing :)")
        break
