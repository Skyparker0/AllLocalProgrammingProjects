# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 07:29:48 2021

@author: batte
"""

#P66     didn't work :(

def find_min_x(D):
    if D == int(D**0.5)**2:
        raise ValueError('must not be perfect square')
        
    y = 1
    
    while True:
        ySide = y * y * D
        posX = (ySide + 1)**0.5
        
        if posX == int(posX):
            return int(posX)
        
        y += 1
        
# def find_min_x(D):
#     if D == int(D**0.5)**2:
#         raise ValueError('must not be perfect square')
        
#     x = int(D**0.5)+1
    
#     while True:
#         for y in range(1,x):
#             if x**2 - D * y**2 == 1:
#                 return x
        
#         x += 1

        
largestX = 0
chosenD = 0

for D in [661,778]:

    try:
        minX = find_min_x(D)
        if minX > largestX:
            largestX = minX
            chosenD = D
            print(D)
    except ValueError:
        continue