# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 16:07:35 2021

@author: batte
"""

#P67

filepath = 'C:/Users/batte/OneDrive/_Parker/Python/ProjectEuler/non-code-files/p067_triangle.txt'

valueTree = []
with open(filepath) as handle:
    
    for line in handle:
        valueTree.append([int(num) for num in line.split()])
        
# valueTree = []
# for row in triangle[:-1]:
#     valueTree.append([None]*len(row))
# valueTree.append(triangle[-1])    
    
for row in range(len(valueTree)-2,-1,-1):
    for col in range(row+1):
        valueTree[row][col] += max([valueTree[row+1][col],valueTree[row+1][col+1]])

# def greatest_sum(height):
#     '''If height is 0, returns solution, if height is 99, returns the biggest
#     number on row 99'''
    
#     if height == len(triangle)-1:
#         return max(triangle[height])
    
    