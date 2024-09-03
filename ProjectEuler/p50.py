# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 07:42:14 2021

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

primes = [x for x in range(1,1000000) if is_prime(x)]

mostPrimes = 0
bestPrime = None

for start in range(0, 300):
    # print("        ",start)
    total = 0
    addIndex = start
    numPrimes = 0
    while True:
        total += primes[addIndex]
        numPrimes += 1
        if total in primes and numPrimes > mostPrimes:
            print(total, numPrimes, primes[start], "to", primes[addIndex])
            mostPrimes = numPrimes
            bestPrime = total
        if total >= 1000000:
            break
        addIndex += 1