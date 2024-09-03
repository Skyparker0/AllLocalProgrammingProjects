# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 07:40:23 2021

@author: batte
"""

#P52
import sys

def special(num):
    digits = sorted(str(num*2))
    for mult in [3,4,5,6]:
        if sorted(str(num*mult)) != digits:
            return False
    return True

for tenPow in range(1,10):
    for x in range(10**tenPow, 10**tenPow + 7* 10**(tenPow-1)):
        if special(x):
            print(x)
            sys.exit()