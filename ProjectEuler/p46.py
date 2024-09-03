# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 08:44:25 2021

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

class InfoHolder:
    
    def __init__(self):
        self.oddCompositeNumbers = [9]
        self.primes = [2,3]
        self.fitsConjecture = [9]
        
    def primesUpTo(self,limit):
        currentCheck = self.primes[-1]
        
        while currentCheck < limit:
            currentCheck += 2
            if is_prime(currentCheck) and currentCheck not in self.primes:
                self.primes.append(currentCheck)
        
    def nextOddCompositeNumber(self):
        currentCheck = self.oddCompositeNumbers[-1]
        
        while True:
            currentCheck += 2
            self.primesUpTo(currentCheck)
            if currentCheck not in self.primes:
                self.oddCompositeNumbers.append(currentCheck)
                return currentCheck
    
    def doesNotFit(self):
        numToCheck = self.nextOddCompositeNumber()
        
        for prime in self.primes:
            i = math.sqrt((numToCheck - prime)/2)
            if i == int(i):
                return False
        return numToCheck