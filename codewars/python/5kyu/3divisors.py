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
