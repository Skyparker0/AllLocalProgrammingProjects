# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 17:23:05 2021

@author: batte
"""

#P93

import itertools

def evaluate(numList):
    #e.g. [1,[2,3],4]
    
    if not type(numList) is list or len(numList) == 1:
        return [numList]
    
    numbersReached = []

    for start in evaluate(numList[0]):
        for second in evaluate(numList[1]):
            if type(start) is list:
                start = start[0]
            if type(second) is list:
                second = second[0]
                
            numbersReached += evaluate([start+second] + numList[2:])
            numbersReached += evaluate([start-second] + numList[2:])
            numbersReached += evaluate([start*second] + numList[2:])
            if second != 0:
                numbersReached += evaluate([start/second] + numList[2:])
            
    return numbersReached
                
    
def extend_set(setToExtend, listOfLists):
    for thing in listOfLists:
        if int(thing[0]) == thing[0]:
            setToExtend.add(thing[0])
    

def all_reachable(numbers):
    
    # 1 1 1 1
    # 1 2 1
    # 1 1 2
    # 1 (1 2)
    # 1 3
    # 2 2
    
    numbersReached = set()
    
    allCombos = itertools.permutations(numbers)
    
    # for a in [0,1,2,3]:
    #     for b in [x for x in [0,1,2,3] if x not in [a]]:
    #         for c in [x for x in [0,1,2,3] if x not in [a,b]]:
    #             d = [x for x in [0,1,2,3] if x not in [a,b,c]][0]
    #             allCombos.append([numbers[a],numbers[b],numbers[c],numbers[d]])
                
                    
    for combo in allCombos:
        extend_set(numbersReached, evaluate(combo))
        extend_set(numbersReached, evaluate([combo[0],[combo[1],combo[2]],combo[3]]))
        extend_set(numbersReached, evaluate([combo[0],combo[1],[combo[2],combo[3]]]))
        extend_set(numbersReached, evaluate([combo[0],[combo[1],[combo[2],combo[3]]]]))
        extend_set(numbersReached, evaluate([combo[0],[combo[1],combo[2],combo[3]]]))   
        extend_set(numbersReached, evaluate([[combo[0],combo[1]],[combo[2],combo[3]]]))         
    
    return numbersReached

def consecutive(numSet):
    n = 1
    while True:
        if n not in numSet:
            return n - 1
        n += 1

mostConsecutive = 0
choice = []

for a in range(1,7):
    for b in range(a,8):
        for c in range(b,9):
            for d in range(c,10):
                reachable = all_reachable([a,b,c,d])
                if consecutive(reachable) > mostConsecutive:
                    mostConsecutive = consecutive(reachable)
                    choice = [a,b,c,d]
                    print(choice)
