# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 09:25:20 2021

@author: batte
"""

#P78

waysToMake = [0,[0,1]]#{1:[0,1]} # Number being made : [0,Combos where the smallest value >= 1,Combos where the smallest value >= 2, etc]

def ways_to_make(n):
    waysToMakeN = [0] + [1] * n
    
    for number in range(n//2,0,-1):
        waysToMake[n-number][0] = n
        waysToMakeN[number] = (waysToMakeN[number+1] + waysToMake[n-number][number]) % 1000000
        
    waysToMake.append(waysToMakeN)
                    
    return waysToMakeN

def number_of_ways(n):
    for i in range(len(waysToMake),n):
        temp = ways_to_make(i)
    temp = None
    
    for uselessIndex in range(n//2):
        waysToMake[uselessIndex] = None
    
    ways = ways_to_make(n)
    return ways[1]



answer = 1
n = 1
while answer % 1000000 != 0:
    n += 1
    answer = number_of_ways(n)
    
print(n)