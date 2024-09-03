# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 07:44:29 2021

@author: batte
"""

#P65

adders = [2,1]

for val in range(2,2000,2):
    adders += [val,1,1]
    
def add_fracs(f1,f2):
    '''f1 and f2 are tuples. returns a tuple of them added'''
    newNumer,newDenom = (f1[0]*f2[1] + f2[0]*f1[1],f1[1]*f2[1])
    
    return newNumer,newDenom
    
def simplify(frac):
    newNumer, newDenom = frac
    
    for div in range(2,int(newDenom**0.5) + 1):
        while newNumer % div == 0 and newDenom % div == 0:
            newNumer //= div
            newDenom //= div
            
    return (newNumer,newDenom)

def continuedE(depth):
    frac = (0,1)
    for index in range(depth-1,0,-1):
        frac = add_fracs(frac,(adders[index],1))
        frac = frac[::-1]
    frac = add_fracs(frac,(adders[0],1))
    return frac

print(continuedE(100))