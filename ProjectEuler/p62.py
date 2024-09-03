# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 08:30:15 2021

@author: batte
"""

#p62

digiDict = dict()
#Like {'12459':4} and if another cube has those same digits, 4 is increased

for toBeCubed in range(10000,1,-1): #in reverse order so the last cube found is the smallest
    digits = ''.join(sorted(str(toBeCubed**3)))
    
    if digits in digiDict:
        digiDict[digits] += 1
        if digiDict[digits] == 5:
            print(toBeCubed)
            
    else:
        digiDict[digits] = 1