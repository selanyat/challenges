#!/usr/bin/env python

import random

def yesOrNo() -> str:
    user_choice = input("Do you want to roll a dice [y/n]: ").strip().lower()
    # is valid??
    if user_choice not in ["y","n"]:
        print("Invalid Input\nEnter either 'y' or 'n'")
        return yesOrNo()

    return user_choice

def rollDice() -> tuple:
    return (random.randint(1,6), random.randint(1,6))

def setMaxRolls() -> int:
    user_input = input("Enter maximun number of times to roll dice: ")

    while not user_input.isdigit():
        print("Invalid Input")
        return setMaxRolls()

    if int(user_input) < 0:
        print("Number must be 0 or more")
        return setMaxRolls()

    return int(user_input)

def main():
    roll_count = 0
    max_rolls = setMaxRolls()

    for _ in range(max_rolls):
        user_choice = yesOrNo()

        if user_choice == "y":
            roll_count += 1
            print(rollDice())

        else:
            print("Thanks for playing :)")
            break

    print(f"You rolled the dice {roll_count} time(s)")

if __name__ == "__main__":
    main()
