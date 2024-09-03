# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 10:56:14 2021

@author: batte
"""

#P94

import math

def int_area(duo,solo):
    height = math.sqrt(duo*duo - solo*solo/4) 
    print(height)
    return int(height) == height 

total = 0

for solo in range(4,4*10**8,2):#4*10**8):
    for duo in [solo-1,solo+1]:
        if int_area(duo,solo):
            perimeter = 2*duo+solo
            if perimeter < 1000000000:
                total += perimeter
                print(duo,duo,solo,perimeter)