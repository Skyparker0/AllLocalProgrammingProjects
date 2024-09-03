# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 07:23:24 2021

@author: batte
"""

#p34

import math

def is_digit_factorial(num):
    return sum([math.factorial(int(x)) for x in str(num)]) == num

total = 0
for number in range(10,1000000):
    if is_digit_factorial(number):
        print(number)
        total += number
print("total", total)