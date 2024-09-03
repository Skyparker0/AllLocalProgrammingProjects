# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 07:48:43 2021

@author: batte
"""

def prime_factorization(num):
    primeFactors = []
    remaining = int(num)
    for divisor in range(2,num//2 + 1):
        while remaining % divisor == 0:
            remaining //= divisor
            primeFactors.append(divisor)
    return primeFactors if primeFactors != [] else [num]

def is_special(num, numDistinct):
    return len(set(prime_factorization(num))) == numDistinct

#loop through numbers starting at 1

for num in range(100000,1000000):
    if is_special(num, 4) and is_special(num + 1, 4) and is_special(num + 2, 4) \
        and is_special(num + 3, 4):
        print(num)
        break
    