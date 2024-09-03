# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

minsDict = {}
def sum_of_squares(n, depth = 4):
    
    if n in minsDict:      #If this number has been found already return it's found value
        return minsDict[n]
    
    if n ** 0.5 == int(n ** 0.5): # If this number is a perfect square return 1
        minsDict[n] = 1
        return 1
    
    if depth == 1:
        return None
    
    
    
    for i in range(int(n**0.5), int((n/2) ** 0.5 -0.01),-1): # See if the number can be made in 2
        if sum_of_squares(n- i**2, 1) == 1:
            minsDict[n] = 2
            return 2
        
    if depth == 2:
        return None
    
    for i in range(int(n**0.5), int((n/3) ** 0.5 -0.01),-1): # See if the number can be made in 3
        if sum_of_squares(n- i**2, 2) == 2:
            minsDict[n] = 3
            return 3
        
    if depth == 3:
        return None
    
    for i in range(int(n**0.5), int((n/4) ** 0.5 -0.01),-1): # See if the number can be made in 4
        if sum_of_squares(n- i**2, 3) == 3:
            minsDict[n] = 4
            return 4

for i in range(1,1001):
    sum_of_squares(i)

for i in range(1,100000):
    sum_of_squares(i**2)