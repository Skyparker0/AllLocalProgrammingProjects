# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 07:57:40 2021

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

primes = [x for x in range(1000,10000) if is_prime(x)]

for prime in primes:
    for step in range(2, (10000-prime) // 2, 2):
        prime2 = prime + step
        prime3 = prime + step + step
        if sorted(str(prime)) == sorted(str(prime2)) == sorted(str(prime3)) \
        and prime2 in primes and prime3 in primes:
            print(prime, prime2, prime3)