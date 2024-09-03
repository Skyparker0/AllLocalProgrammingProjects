# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 14:09:33 2021

@author: batte
"""

#P92

def reaches_89(number):
    while True:
        if number == 89:
            return True
        elif number == 1:
            return False
        number = sum([int(digit)*int(digit) for digit in str(number)])

total = 0

for i in range(1,10**7):
    if i % 100000 == 0:
        print(i)
    if reaches_89(i):
        total += 1
        
# print(sum([1 for i in range(1,10000000) if reaches_89(i)]))