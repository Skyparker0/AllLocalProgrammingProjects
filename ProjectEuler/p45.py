# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 07:41:20 2021

@author: batte
"""

import itertools

def triN(n):
    return n * (n + 1) / 2

def pentN(n):
    return n * (3 * n - 1) / 2

def hexN(n):
    return n * (2 * n - 1)

triNums = [0]
pentNums = [0]
hexNums = [0]

for n in itertools.count(1):
    triNums.append(triN(n))
    pentNums.append(pentN(n))
    hexNums.append(hexN(n))
    
    if triNums[-1] in pentNums and triNums[-1] in hexNums:
        print(triNums[-1])
        
### The one printed after 40755.0, 1533776805.0