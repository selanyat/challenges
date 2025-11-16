#!/bin/env python

def solution(n, m):
    
    result = []
    
    for value in range(n, m+1):
        count = 0
        for divisor in range(2, value):
            if value % divisor == 0 and count <= 3:
                count += 1
        if count == 3:
            result.append(value)
    return result

# print(solution(10000,100000))


# Problem

# Description:

# Your task is to write a function that takes two integers n and m, and returns a sorted array of all integers from n to m inclusive, which have exactly 3 divisors (excluding 1 and the number itself).
# Example:

# solution(2, 20) -> [16]

# 16 has 3 divisors: 2, 4, 8 (1 and 16 aren't included)
# Input:

    # n - integer (2 ≤ n ≤ 10^14)
    # m - integer (2 ≤ m ≤ 10^18)

# NOTE: In Rust, the bounds are (2 ≤ n ≤ 2^51), (20 ≤ m ≤ 2^52).
# Output:

# result - array of integers


