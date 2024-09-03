# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 08:23:51 2021

@author: batte
"""

#P81

import numpy as np

path = "non-code-files/p081_matrix.txt"


matrix = []
with open(path) as handle:
    for line in handle:
        matrix.append([int(x) for x in line.strip('\n').split(",")])
        
matrix = np.array(matrix)

def least_neighbor(pos):
    
    width, height = matrix.shape
    x,y = pos
    if x >= width-1 and y >= height-1:
        return 0
    elif x >= width-1:
        return matrix[y+1,x]
    elif y >= height-1:
        return matrix[y,x+1]
    elif x < width-1 and y < height-1:
        return min(matrix[y+1,x],matrix[y,x+1])
    
    
x = matrix.shape[0] -1 
y = matrix.shape[1] -1
while True:
    for i,diagX in enumerate(range(x,1+y)):
        diagY = y - i
        matrix[diagY,diagX] += least_neighbor((diagX,diagY))
    
    if x > 0:
        x -= 1
    elif y > 0:
        y -= 1
    else:
        break
    
print(matrix[0,0])