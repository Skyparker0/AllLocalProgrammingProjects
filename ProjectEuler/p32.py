# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 08:15:07 2021

@author: batte
"""

from math import *

def factors(num):
    factors = []
    for factor in range(1, floor(num ** 0.5) + 1):
        if num % factor == 0:
            factors.append((factor, num // factor))
    return factors

def isPanProd(num):
    for m1, m2 in factors(num):
        if sorted(str(m1) + str(m2) + str(num)) == [str(x) for x in range(1,10)]:
            print(m1,m2,num)
            return True

pandigitalProducts = []

for product in range(1,99999):
    if isPanProd(product):
        pandigitalProducts.append(product)
        
print(pandigitalProducts)