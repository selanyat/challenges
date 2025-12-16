#!/bin/env python

def pyramid(n):
    result = []

    count = 0
    while count < n:
        result.append([1]*(count+1))
        count += 1

    return result

# Description
# Write a function that given an integer n >= 0, returns an array of n ascending length subarrays, all filled with 1s.
#
# 0 => [ ]
# 1 => [ [1] ]
# 2 => [ [1], [1, 1] ]
# 3 => [ [1], [1, 1], [1, 1, 1] ]


