# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 10:53:29 2021

@author: batte
"""

# P79

path = "non-code-files/p079_keylog.txt"

tries = []

with open(path) as handle:
    for line in handle:
        tries.append(line.strip('\n'))
        
def att1():
    
    
            
    possibilities = []
            
    for start in range(0,10):
        newPossibility = list(range(start,10)) + [8,7,6,5,4,3,2,1,0,1,2,3,4,5,6,7,8,9]*2
        possibilities.append([str(i) for i in newPossibility])
        newPossibility = list(range(start,-1,-1)) + [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0]*2
        possibilities.append([str(i) for i in newPossibility])
    
    
    def password_for_possibility(possibility):
        keptIndexes = set()
        
        for TRY in tries:
            index = -1
            for character in TRY:
                index = possibility[index+1:].index(character) + index+1
                keptIndexes.add(index)
                
        password = "".join([possibility[i] for i in keptIndexes])
        return password
    
    bestPassword = ""
    bestLength = 150
    
    for possibility in possibilities:
        password = password_for_possibility(possibility)
        if len(password) < bestLength:
            bestLength = len(password)
            bestPassword = password
        
        
    print(bestPassword)
    
comesAfter = {num:set() for num in "0123456789"}

for TRY in tries:
    comesAfter[TRY[0]].add(TRY[1])
    comesAfter[TRY[0]].add(TRY[2])
    comesAfter[TRY[1]].add(TRY[2])
    
    
# 73162890