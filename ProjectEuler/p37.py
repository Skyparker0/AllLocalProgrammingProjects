# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 07:29:00 2021

@author: batte
"""

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

def is_truncatable_prime(num):
    strNum = str(num)
    toCheck = [int(strNum[:x]) for x in range(len(strNum),0,-1)]
    toCheck += [int(strNum[x:]) for x in range(0, len(strNum))]
    return all([is_prime(truncated) for truncated in toCheck])

truncatablePrimes = [x for x in range(1000000) if is_truncatable_prime(x)][5:]
print(sum(truncatablePrimes))
# parents = [2,3,5,7]
# newlyCreated = []
# newFlag = True
# while newFlag:
    