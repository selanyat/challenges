#!/bin/env python

def divisors(integer):

    integer = int(integer)
    factors = []

    for number in range(2, integer):
        if integer % number == 0:
            factors.append(number)

    if len(factors) != 0:
        return factors

    else:
        return f"{integer} is prime"


while True:
    print(divisors(input("Enter num: ")))
