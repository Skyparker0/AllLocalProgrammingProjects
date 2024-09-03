# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 07:12:48 2021

@author: batte
"""

def is_palindrome(number):
    strNum = str(number)
    return all([strNum[index] == strNum[-(index+1)] for index in range(0, len(strNum)//2)])

total = 0

for x in range(1000000):
    if is_palindrome(x) and is_palindrome(bin(x)[2:]):
        print(x, bin(x)[2:])
        total += x
        
print(total)