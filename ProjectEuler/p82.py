# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 09:15:00 2021

@author: batte
"""

#P82

import numpy as np

path = "non-code-files/p082_matrix.txt"


trueMatrix = []
with open(path) as handle:
    for line in handle:
        trueMatrix.append([int(x) for x in line.strip('\n').split(",")])
        

        
trueMatrix = np.array(trueMatrix)
WIDTH,HEIGHT = trueMatrix.shape
newMatrix = np.array([[None] * WIDTH]*HEIGHT)
newMatrix[:,-1] = trueMatrix[:,-1]

def update(row,column):
    neighbors = []
    
    if row == HEIGHT - 1:
        neighbors = [newMatrix[row,column+1],newMatrix[row-1,column]]
    elif row == 0:
        neighbors = [newMatrix[row,column+1],newMatrix[row+1,column]]
    else:
        neighbors = [newMatrix[row,column+1],newMatrix[row+1,column],newMatrix[row-1,column]]
    
    neighbors = [x for x in neighbors if x != None]
    
    newMatrix[row,column] = trueMatrix[row,column] + min(neighbors)

def complete_col(column):
    oldColumn = newMatrix[:,column]
    newColumn = []
    while list(oldColumn) != list(newColumn):
        oldColumn = newMatrix[:,column]
        
        for row in range(0,HEIGHT):
            update(row,column)
            
        for row in reversed(range(0,HEIGHT)):
            update(row,column)
        
        newColumn = newMatrix[:,column]
        
for column in reversed(range(0,WIDTH-1)):
    complete_col(column)
    
print(min(newMatrix[:,0]))