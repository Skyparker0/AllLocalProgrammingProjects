# -*- coding: utf-8 -*-
"""
Created on Mon May 17 07:50:29 2021

@author: batte
"""

#P56

maxSum = 0
bestCombo = (0,0)

for a in range(1,100):
    for b in range(1,100):
        total = sum([int(i) for i in str(a**b)])
        if total > maxSum:
            maxSum = total
            bestCombo = (a,b)
            
print(maxSum,bestCombo)