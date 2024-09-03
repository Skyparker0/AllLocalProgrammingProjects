# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 09:40:57 2021

@author: batte
"""

import math

def digit_factorial(n):
    return sum([math.factorial(int(d)) for d in str(n)])

def non_repeat(n):
    non_repeating_terms = [n]
    currentNumber = n
    while True:
        currentNumber = digit_factorial(currentNumber)
        if currentNumber in non_repeating_terms:
            return len(non_repeating_terms)
        non_repeating_terms.append(currentNumber)
        
sixties = 0

for n in range(100000,1000000):
    if non_repeat(n) == 60:
        sixties += 1
        #print(n)
        