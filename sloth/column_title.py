#!/usr/bin/env python

from math import log10, ceil

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def number_of_letters(integer):
    if integer == 1:
        return 1

    estimated_number = int(ceil(log10(integer) / log10(26)))

    if integer < ((26 ** (estimated_number -1)) + 26) and estimated_number != 1:
        return estimated_number - 1
    else:
        return estimated_number

def convert_to_title(column_number):
    length = number_of_letters(column_number)

    title = ""

    for _ in range(length):
        letter_index = (column_number % 26) - 1
        print(letter_index)
        title += letters[letter_index]

        column_number = column_number // 26

    print(f"result {title[::-1]}, len {length} ")
    return title[::-1]



# Excel Sheet Column Title
#
# Given a positive integer, return its corresponding column title displayed in Excel sheets.
#
# For example:
#
# 1 -> A
# 2 -> B
# 3 -> C
# ...
# 26 -> Z
# 27 -> AA
# 28 -> AB
# ...
#
# Examples
#
convert_to_title(78)
convert_to_title(1)
# output = "A"
#
convert_to_title(18)
# output = "R"
#
convert_to_title(28)
# output = "AB"
#
convert_to_title(52)
# output = "AZ"
#
convert_to_title(701)
# output = "ZY"
convert_to_title(229704)
# output = "MATT"
convert_to_title(209380622941)
# output = "ZATOICHI"
