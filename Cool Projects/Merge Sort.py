# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 18:53:30 2020

@author: batte
"""

def combine_sorted(L1,L2):
    compList = []
    while True:
        if len(L1) == 0:
            compList += L2
            return compList
        elif len(L2) == 0:
            compList += L1
            return compList
        
        if L1[0] > L2[0]:
            compList.append(L2.pop(0))
        else:
            compList.append(L1.pop(0))
            

def merge_sort(L):
    sortedLists = [[x] for x in L]
    
    while True:
        if len(sortedLists) == 1:
            return sortedLists[0]
        newMergedList = []
        for index in range(1, len(sortedLists), 2):
            newMergedList.append(combine_sorted(sortedLists[index-1], sortedLists[index]))
        
        if len(sortedLists) % 2 != 0:
            newMergedList.append(sortedLists[-1])
        sortedLists = newMergedList[:]