# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 18:30:54 2023

@author: batte
"""

import ast

def permutations(numString):
    '''Permutations of the original string of numbers'''
    allPerms = set([numString])
    
    if len(numString) <= 1:
        return allPerms
    
    for i in range(len(numString)):
        for perm in permutations(numString[:i] + numString[i+1:]):
            allPerms.add(numString[i] + perm)
    
    return allPerms
            
def allOperations(numList, evaluations = False):
    evals = set()
    
    if len(numList) == 1:
        return set(numList)
    
    for op in "+-*/":
        for ending in allOperations(numList[1:]):
            evals.add(numList[0] + op + ending)
                  
    if evaluations:
        return set([eval(eq) for eq in evals])
    
    return evals
                  
def allOutcomes(numString):
    '''Recursive: splits every number that can be achived using substrings rather than
    parentheses'''
    
    if len(numString) == 1:
        return [int(numString)]
    
    outcomes = set()
    
    for splitpoint in range(0, len(numString)-1):
        # due to permutations, won't have to check outcomes of the first half
        firstBatch = numString[:splitpoint+1]
        firstResults = allOperations([i for i in firstBatch]) #all the numbers achiveable
        
        secondBatch = numString[splitpoint+1:]
        secondResults = allOutcomes(secondBatch)
        
        
        for f in firstResults:
            for s in secondResults:
                for outcome in allOperations([str(f),str(s)],True):
                    outcomes.add(outcome)
                
    return outcomes
        
def allTenSolve(startNums):
    sortNums = [int(i) for i in sorted(startNums)]
    return sortNums