# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 08:42:49 2021

@author: batte
"""

#P76


waysToMake = {1:[1]} # Number being made : [Combos where the smallest value >= 1,Combos where the smallest value >= 2, etc]

def ways_to_make(n):
    if n in waysToMake:
        return waysToMake[n]
    
    if n > max(waysToMake):
        for i in range(max(waysToMake),n):
            temp = ways_to_make(i)
        temp = None
    
    waysToMakeN = [1] * n
    
    for number in range(1,n//2 + 1):
        newWays = waysToMake[n-number][number-1]
        for lowerLimit in range(number):
            waysToMakeN[lowerLimit] += newWays
        
    waysToMake[n] = waysToMakeN
                    
    return waysToMakeN

answer = ways_to_make(100)[0]-1
print(answer)