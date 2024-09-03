# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 07:42:24 2021

@author: batte
"""

#P64
#FAILED... :(

import math

def make_continued(num):
    '''Makes the continued fraction of sqrt(num)'''
    
    adders = []
    leftOvers = []
    
    previousVal = math.sqrt(num)
    
    if int(previousVal) == previousVal:
        return [[],[]]
    
    while True:
        newAdder = math.floor(previousVal)
        previousVal = 1/(previousVal-newAdder)
        adders.append(newAdder)
        
        if round(previousVal,3) in leftOvers:
            # repeatIndex = leftOvers.index(round(previousVal,3))
            return adders[:1],adders[1:],leftOvers#adders[:repeatIndex + 1],adders[repeatIndex + 1:]
        
        leftOvers.append(round(previousVal,3))
    
def period(num):
    return len(make_continued(num)[1])

# odds = 0

# for num in range(2,10001):
#     if period(num) % 2 == 1:
#         odds += 1