# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 08:17:02 2021

@author: batte
"""

#P75
import math

#Naive approach - try all possible values for sides.

def has_one_triangle(l):
    found = 0
    for A in range(3,l//3):
        for B in range(A+1,(l-A)//2 + 1):
            C = l-A-B
            if C**2 == A**2 + B**2:
                found += 1
                if found > 1:
                    return False
    if found == 1:
        return True
    return False

# for l in range(12,500,2):#range(12,1500001,2):
#     if has_one_triangle(l):
#         print(l)

#WAYYYYYY too slow

#Euclid's formula

def triples_sums(maxSum=1500000):
    tripsSums = []
    n = 1
    
    while True: #All n's
        m = n+1
        
        if 2*m**2 + 2*m*n > maxSum: #If the starting value of the new n already has a too big sum, end
            return tripsSums
        
        while True: #All m's        
            # if math.gcd(n, m) != 1:
            #     continue
            
        
            sidesSum = 2*m*(m+n)
            
            if sidesSum > maxSum:
                break
            
            tripsSums.append(sidesSum)
            
            m += 2   #Skip cases where both are odd
        n += 1

total = 0



l = sorted(list(triples_sums()))
l.remove(108)
newList = set()
badList = set()

for step in l:
    for multiple in range(step,1500001,step):
        if multiple not in newList and multiple not in badList:
            newList.add(multiple)
        else:
            if multiple not in badList:
                newList.remove(multiple)
            badList.add(multiple)
