# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 07:25:51 2021

@author: batte
"""

#p68
# workingRings = []

# for startNode in range(1,7):
#     used = [startNode,]
#     path = str(startNode)
    
# 653 1031 914 842 725

import itertools

innerNodes = list(itertools.permutations([1,2,3,4,5]))

def makeFullRing(inNodes):
    fRing = []
    for index in range(5):
        section = (14 - inNodes[index]-inNodes[index-4],inNodes[index],inNodes[index-4])
        fRing.append(section)
    return fRing

def ringWorks(fRing):
    endNodes = []
    for section in fRing:
        endNodes.append(section[0])
        
            
    return sorted(endNodes) == [6,7,8,9,10] and endNodes[0] == 6

fRings = [makeFullRing(inNodes) for inNodes in innerNodes]
fRings = [ring for ring in fRings if ringWorks(ring)]
print(fRings)