# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 08:22:10 2021

@author: batte
"""

#P61

#put all tri quad pent... numbers < 10000 into lists

if True: #creation of those numbers

    triNums = []
    num = 1
    adder = 2
    while num < 10000:
        if num >= 1000:
            triNums.append(num)
        num += adder
        adder += 1
        
    quadNums = []
    num = 1
    adder = 3
    while num < 10000:
        if num >= 1000:
            quadNums.append(num)
        num += adder
        adder += 2
        
    pentNums = []
    num = 1
    adder = 4
    while num < 10000:
        if num >= 1000:
            pentNums.append(num)
        num += adder
        adder += 3
        
    hexNums = []
    num = 1
    adder = 5
    while num < 10000:
        if num >= 1000:
            hexNums.append(num)
        num += adder
        adder += 4
        
    hepNums = []
    num = 1
    adder = 6
    while num < 10000:
        if num >= 1000:
            hepNums.append(num)
        num += adder
        adder += 5
        
    octNums = []
    num = 1
    adder = 7
    while num < 10000:
        if num >= 1000:
            octNums.append(num)
        num += adder
        adder += 6
        
def strLst(lst):
    return [str(item) for item in lst]
        
figNums = [strLst(triNums),strLst(quadNums),strLst(pentNums),
            strLst(hexNums),strLst(hepNums),strLst(octNums)]

def findWorkingNumbers(number, posFigNumIndexes,currentDepth,startDigits):
    '''
    finds and returns possible continuations given a starting number, what
    types of numbers it can go to next (so if you start with a  tri num,
    0 will not be in posFigNumIndexes), how deep it is (depth goes 1 to 5) 
    if depth is 5, the found numbers must end in startDigits
    '''
    numberEnd = number[2:]
    for figNumIndex in posFigNumIndexes:
        for posNum in figNums[figNumIndex]:
            
            if posNum[:2] == numberEnd:
                if currentDepth == 5 and posNum[2:] == startDigits:
                    return [[number,posNum]]
                
                continuations = findWorkingNumbers(posNum,
                     [index for index in posFigNumIndexes if index != figNumIndex],
                     currentDepth + 1,startDigits)
                if continuations != None:
                    return [[[number] + continuation] for continuation in continuations]
                  
                    
for figNumIndex in (0,1,2,3,4,5):
    for startNum in figNums[figNumIndex]:
        print(findWorkingNumbers(startNum,
            [index for index in [0,1,2,3,4,5] if index != figNumIndex],
            1,startNum[:2]))