# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 08:54:48 2021

@author: batte
"""

#P72

#for d in range(1,1000001):
    #TotalReducedFractions += phi(d)
    
def phis_to(num):
    phis = [n for n in range(0,num+1)]
    for startNum in range(2,num+1):
        if phis[startNum] == startNum:    #That number is prime; no factors pulled out
            for index in range(startNum,num+1,startNum):
                phis[index] -= phis[index]//startNum
    return phis


print(sum(phis_to(1000000)[2:]))