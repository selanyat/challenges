#!/usr/bin/env python

import random

def getUserInput() -> int:
    user_input = input("Guess a number between 1 and 100: ").strip()

    if not user_input.isdigit():
        print("Invalid option")
        return getUserInput()

    user_input = int(user_input)

    if user_input < 0 or user_input > 100:
        print("Input is out of range")
        return getUserInput()

    return user_input

def genetateRandomNumber() -> int:
    return random.randint(1, 100)

def main():
    number_to_guess = genetateRandomNumber()

    while True:
        user_input = getUserInput()

        if user_input == number_to_guess:
            print("Congratulations! you guessed the number")
            break

        elif user_input < number_to_guess:
            print("Too low")

        else:
            print("Too high")

if __name__ == "__main__":
    main()
