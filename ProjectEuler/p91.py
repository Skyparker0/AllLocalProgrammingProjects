# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 14:52:35 2021

@author: batte
"""

#P91

'''
2500 possibilities where 0,0 is the right angle

'''

LIMIT = 50

def solutions_on_line(slope, intercept):
    solutions = 0
    
    for x in range(0,LIMIT+1):
        y = round(slope * x + intercept,6)
        if int(y) == y and y >= 0 and y <= LIMIT:
            solutions += 1
        
            
    return solutions-1

totalSolutions = LIMIT**2

for x in range(0,LIMIT+1):
    for y in range(0,LIMIT+1):
        #X,Y = the right angle position
        if x == 0 and y == 0:
            continue
        
        if y == 0:
            totalSolutions += LIMIT
            continue
            
        perpendicularSlope = -(x/y)
        intercept = y - perpendicularSlope*x
        
        numSolutions = solutions_on_line(perpendicularSlope,intercept)
        

        totalSolutions += solutions_on_line(perpendicularSlope,intercept)
        
        
print(totalSolutions)