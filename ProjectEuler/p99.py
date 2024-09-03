# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 09:52:51 2022

@author: batte
"""

#P99

digitsToKeep = 10

def aproximate(base,exponent):
    currentNumber = base
    zeroes = 0
    for i in range(exponent-1):
        currentNumber *= base
        zeroes += len(str(currentNumber)[digitsToKeep:])
        currentNumber = int(str(currentNumber)[:digitsToKeep])
        
    return currentNumber,zeroes

path = "C:/Users/batte/OneDrive/_Parker/Python/projectEuler/non-code-files/p099_base_exp.txt"

biggestNum = (0,0)
chosenLine = 0
lineNum = 0
with open(path) as handle:
    for line in handle:
        lineNum += 1
        result = aproximate(int(line.split(",")[0]),int(line.split(",")[1]))
        
        if result[1] > biggestNum[1] or (result[1] == biggestNum[1] and result[0] > biggestNum[0]):
            biggestNum = result
            chosenLine = lineNum
            print(biggestNum)