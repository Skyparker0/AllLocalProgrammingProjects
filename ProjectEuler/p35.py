# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 08:00:18 2021

@author: batte
"""

#p35

import math

def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False
    for divisor in range(2, math.ceil(num ** 0.5) + 1):
        if num % divisor == 0:
            return False
    return True
    
    #return all([num % divisor != 0 for divisor in [2] + list(range(3, ))])
    
def is_circle_prime(num):
    strNum = str(num)
    if num in [2,5]:
        return True
    if any([num in strNum for num in "024568"]):
        return False
    for i in range(len(strNum)):
        strNum = strNum[1:] + strNum[0] if len(strNum) > 1 else strNum
        if not is_prime(int(strNum)):
            return False
    return True

allCirclePrimes = []

for number in range(1,1000000):
    if is_circle_prime(number):
        allCirclePrimes.append(number)