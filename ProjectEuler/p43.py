# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 08:16:36 2021

@author: batte
"""

import itertools

# def is09Pandigital(num):
#     return "".join(sorted(str(num))) == "0123456789"

counted = set()

def isSpecial(string):
    divisors = [2,3,5,7,11,13,17]
    strNum = string
    for divisorIndex, start in enumerate(range(2,9)):
        if int(strNum[start-1:start+2]) % divisors[divisorIndex] != 0:
            return False
    return True


for perm in itertools.permutations([0,1,2,3,4,5,6,7,8,9]):
    if perm[0] != 0:
        strNum = "".join([str(n) for n in perm])
        if isSpecial(strNum):
            counted.add(int(strNum))
                
                
print(sum(counted))