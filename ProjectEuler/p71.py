# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 09:32:41 2021

@author: batte
"""

#P71

#428571/1000000 Seems like a pretty good aproximation

#428564/999983 better
#numbers = [(428571,1000000),(428564,999983)]

def closeness(frac):
    return 3/7 - (frac[0]/frac[1])

best = (1,1)
mostClose = 1
for den in range(1,1000001):
    num = int(3/7 * den)
    frac = (num,den)
    fracCloseness = closeness(frac)
    
    if fracCloseness < mostClose and fracCloseness > 0:
        best=frac
        mostClose=fracCloseness
        
print(best)