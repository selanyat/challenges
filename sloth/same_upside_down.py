#!/usr/bin/env python

def isValidInput(input):
    if not input.isdigit():
        return False
    
    allowedInput = ["6", "9", "0"]

    for char in input:
        if char not in allowedInput:
            return False
    # TODO Use sets for optimization later
    return True

def sameUpsidedown(value):
    if not isValidInput(value):
        print('invalid')
        return f"{value} is not a valid input"

    new_value = ""
    for char in value[::-1]:
        if char == "0":
            new_value += "0"

        if char == "6":
            new_value += "9"

        if char == "9":
            new_value += "6"

    if value == new_value:
        return True

    return False

### Challenge ###


# Is It the Same Upside Down?
#
# The number 6090609 has a special property: if you turn the number upside down (imagine rotating your screen 180 degrees), you get 6090609 again.
#
# Write a function that takes a string on the digits 0, 6, 9 and returns true if the number is the same upside down or false otherwise.
# Examples
#
# sameUpsidedown("6090609")
# output = true
#
# sameUpsidedown("9669")
# output = false
# # Becomes 6996 when upside down.
#
# sameUpsidedown("9")
# output = false
#
# sameUpsidedown("0")
# output = true
#
# sameUpsidedown("6090609")
# output = true
#
# sameUpsidedown("60906096090609")
# output = true
#
# sameUpsidedown("966909669")
# output = false
# Becomes 699606699 when upside down.
#
# sameUpsidedown("96666660999999")
# output = false
