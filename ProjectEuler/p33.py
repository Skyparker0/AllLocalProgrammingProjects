# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 14:18:33 2021

@author: batte
"""

digitCancellingFractionsProd = []

def is_digitCancellingFraction(numerator, denominator):
    numList = [int(x) for x in str(numerator)]
    denList = [int(x) for x in str(denominator)]
    
    if 0 in numList or 0 in denList or numList == denList:
        return False
    
    if numList[0] in denList and numList[0] != 0:
        denCopy = list(denList)
        denCopy.remove(numList[0])
        if numList[1] / denCopy[0] == numerator/denominator:
            return (numList[1], denCopy[0])
    
    if numList[1] in denList and numList[1] != 0:
        denCopy = list(denList)
        denCopy.remove(numList[1])
        if numList[0] / denCopy[0] == numerator/denominator:
            return (numList[0], denCopy[0])
    
    return False

for a in range(10,100):
    for b in range(a,100):
        if is_digitCancellingFraction(a, b) != False:
            digitCancellingFractionsProd.append(is_digitCancellingFraction(a, b))