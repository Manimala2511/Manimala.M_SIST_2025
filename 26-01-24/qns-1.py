"""best division
Kristen loves playing with and comparing numbers. She thinks that if she takes two different positive numbers, the one whose digits sum to a larger number is better than the other. If the sum of digits is equal for both numbers, then she thinks the smaller number is better. For example, Kristen thinks that  is better than  and that  is better than .

Given an integer, , can you find the divisor of  that Kristin will consider to be the best?"""
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    def digits(n):
        return sum(int(digit) for digit in str(n))

def best_divisors(n):
    best_divisor = 1
    sum = 1
   
    
    for i in range(2, n + 1):
        if n % i == 0:
            current_sum = digits(i)
            if current_sum > sum or (current_sum == sum and i < best_divisor):
                sum = current_sum
                best_divisor = i       
    return best_divisor

print(best_divisors(n))
