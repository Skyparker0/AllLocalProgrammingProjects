# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 07:33:52 2021

@author: batte
"""

### number triangle

import itertools

def tri_solve(numbers, baseSize, height):
    if sum([baseSize - i for i in range(height)]) != len(numbers):
        raise ValueError
    
    solutions = [] # list of "triangles"; [[3],[1,4],[5,6,2]]
    
    for base in itertools.permutations(numbers, baseSize):
        currentTriangle = [list(base)]
        foundNumbers = list(base)
        for i in range(height-1):
            currentLayer = [abs(currentTriangle[0][x] - currentTriangle[0][x + 1]) 
                            for x in range(len(currentTriangle[0]) - 1)]
            currentTriangle.insert(0,currentLayer)
            foundNumbers.extend(currentLayer)
        if all([x in foundNumbers for x in numbers]):
            solutions.append(currentTriangle)
            
    return solutions