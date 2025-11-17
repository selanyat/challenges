#!/bin/env python

def getInput(inp):
    while not inp.isdigit():
        print("Input must be a number")
        inp = input("Enter new digit : ")

    return int(inp)

#while True:
    #print(getInput())

def divisors(integer):

    integer = getInput(integer)
    print(integer)
    factors = []

    for number in range(2, integer):
        if integer % number == 0:
            factors.append(number)

    if len(factors) != 0:
        return factors

    return f"{integer} is prime"

print(divisors(input("Enter a number: ")))



# Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#, empty table in COBOL) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
# Examples:

# divisors(12) --> [2, 3, 4, 6]
# divisors(25) --> [5]
# divisors(13) --> "13 is prime"

