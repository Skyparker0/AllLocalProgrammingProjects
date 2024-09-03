# -*- coding: utf-8 -*-
"""
Created on Mon May 10 07:25:11 2021

@author: batte
"""

# P 55

def is_palindrome(num):
    string = str(num)
    length = len(string)
    return string[:(length + 1)//2] == string[length//2:][::-1]

def is_lychrel(num):
    currentNum = num
    
    itterNum = 0
    while itterNum < 50:
        itterNum += 1
        currentNum = currentNum + int(str(currentNum)[::-1])
        if is_palindrome(currentNum):
            return False#itterNum
        
    return True

lychrelNumbers = []

for n in range(10000):
    if is_lychrel(n):
        lychrelNumbers.append(n)