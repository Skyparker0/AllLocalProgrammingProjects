# -*- coding: utf-8 -*-
"""
Created on Sun May 23 08:04:16 2021

@author: batte
"""

#P60

####Tooooo..... Hard..............

def is_prime(x):
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, int(x**0.5) + 1, 2):
			if x % i == 0:
				return False
		return True
    
def first_x_primes(x):
    primes = []
    check = 2
    while len(primes) < x:
        if is_prime(check):
            primes.append(check)
        check += 1
    return primes

firstPrimes = first_x_primes(1000)

for a in range(len(firstPrimes)):
    for b in range(len(firstPrimes)):
        for c in range(len(firstPrimes)):
            for d in range(len(firstPrimes)):
                for e in range(len(firstPrimes)):
                    pass
    