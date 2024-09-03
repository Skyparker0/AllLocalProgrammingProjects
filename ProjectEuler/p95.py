# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 11:00:55 2021

@author: batte
"""

#P95

import math

def sum_divisors(x):
    total = 1
    squareRoot = math.sqrt(x)
    for i in range(2, math.floor(math.sqrt(x)+1)):
        if x % i == 0:
            total += i + x//i
    if int(squareRoot) == squareRoot:
        total -= int(squareRoot)
    return total

def chain(start):
    last = start
    chain = []
    while True:
        chain.append(last)
        last = sum_divisors(last)
        if last > 1000000:
            return []
        if last == start:
            return chain
        if last in chain:
            return chain[chain.index(last):]
        
        
bestChain = []
bestLen = 0

for i in range(1000000):
    newChain = chain(i)
    chainLen = len(newChain)
    if chainLen > bestLen:
        bestLen = chainLen
        bestChain = newChain