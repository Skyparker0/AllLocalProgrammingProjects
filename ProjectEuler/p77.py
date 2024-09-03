# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 08:56:54 2021

@author: batte
"""

#P77

import math

def is_prime(x):
     if x <= 1:
        return False
     elif x <= 3:
        return True
     elif x % 2 == 0:
        return False
     else:
        for i in range(3, int(math.sqrt(x)) + 1, 2):
             if x % i == 0:
                return False
        return True

waysToMake = {1:[0]}

def ways_to_make(n):    #except only using prime numbers
    if n in waysToMake:
        return waysToMake[n]
    
    if n > max(waysToMake):
        for i in range(max(waysToMake),n):
            temp = ways_to_make(i)
        temp = None
    
    if is_prime(n):
        waysToMakeN = [1] * n
    else:
        waysToMakeN = [0] * n
    
    for number in range(1,n//2 + 1):
        newWays = waysToMake[number][number-1] * \
                  waysToMake[n-number][number-1]
        for lowerLimit in range(number):
            waysToMakeN[lowerLimit] += newWays
        
    waysToMake[n] = waysToMakeN
                    
    return waysToMakeN

def number_of_ways(n):
    ways = ways_to_make(n)
    if ways[-1] == 1:
        return ways[0]-1
    return ways[0]

answer = 0
n = 0
while answer < 5000:
    n += 1
    answer = number_of_ways(n)
    
print(n)