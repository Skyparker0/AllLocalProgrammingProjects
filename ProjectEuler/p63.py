# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 07:42:14 2021

@author: batte
"""

#P63

workingNumbers = set()
count = 0
for base in range(1,10):
    for exponent in range(1,22):
        if len(str(base**exponent)) == exponent:
            count += 1
            print(base,exponent)