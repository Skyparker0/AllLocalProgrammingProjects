# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 08:23:15 2021

@author: batte
"""

import itertools
import math
# itertools.permutations()

def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False
    for divisor in range(2, math.ceil(num ** 0.5) + 1):
        if num % divisor == 0:
            return False
    return True

for perm in itertools.permutations([1,2,3,4,5,6,7]):
    if is_prime(int("".join([str(x) for x in perm]))):
        print(int("".join([str(x) for x in perm])))