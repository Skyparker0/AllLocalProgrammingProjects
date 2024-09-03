# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 11:03:26 2021

@author: batte
"""

def phis_to(num):
    phis = [n for n in range(0,num+1)]
    for startNum in range(2,num+1):
        if phis[startNum] == startNum:    #That number is prime; no factors pulled out
            for index in range(startNum,num+1,startNum):
                phis[index] -= phis[index]//startNum
    return phis

def coprimes(lst):
    return [i for i in lst if i]

def phis_to_special(num):
    phis = [list(range(1,n+1)) for n in range(0,num+1)]
    for startNum in range(2,num+1):
        if len(coprimes(phis[startNum])) == startNum:    #That number is prime; no factors pulled out
            for index in range(startNum,num+1,startNum): #Multiples
                phis[index][startNum-1:num+1:startNum] = [False]*(index//startNum)
    
    return phis
    
allPhis = phis_to_special(12000)
minNum,minDen,maxNum,maxDen = (1,3,1,2)
totalBetweens = 0

for d,n in enumerate(allPhis):
    for numerator in n:
        #minNum/minDen < numerator/d < maxNum/maxDen
        if minNum * d < minDen * numerator and numerator * maxDen < d * maxNum:
            print(f"{numerator}/{d}")
            totalBetweens += 1
            
print(totalBetweens)
