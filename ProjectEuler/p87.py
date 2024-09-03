# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 15:04:45 2021

@author: batte
"""

#P87

import math

def is_prime(x):
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, int(math.sqrt(x)) + 1, 2):
			if x % i == 0:
				return False
		return True


primes = []
for i in range(1,7080):
    if is_prime(i):
        primes.append(i)
        
squares = [x**2 for x in primes if x**2 < 50000000]
cubes = [x**3 for x in primes if x**3 < 50000000]
quads = [x**4 for x in primes if x**4 < 50000000]

prime_power_triples = set()

for square in squares:
    for cube in cubes:
        for quad in quads:
            primeSum = square + cube + quad
            if primeSum < 50000000:
                prime_power_triples.add(primeSum)
                
print(len(prime_power_triples))