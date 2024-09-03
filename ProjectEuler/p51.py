# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 07:52:33 2021

@author: batte
"""

#Problem 51

import time
import math

# def is_prime2(num):
#     if num == 2:
#         return True
#     if num == 1:
#         return False
#     for divisor in range(2, math.ceil(num ** 0.5) + 1):
#         if num % divisor == 0:
#             return False
#     return True


# start = time.time()
# for x in range(1,1000000):
#     if is_prime(x):
#         pass
# stop = time.time()
# print("is_prime:", stop-start)

# start = time.time()
# for x in range(1,1000000):
#     if is_prime2(x):
#         pass
# stop = time.time()
# print("is_prime2:", stop-start)

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
    
def can_make_eight(prime):
    '''
    for every positioning of any number of "fill-ins" (*):
        for every number 0-9 to replace these *s with:
            if the created number is prime:
                count += 1
        if count == 8:
            return True'''
    
primeList = [x for x in range(1,1000000) if is_prime(x)]

for prime in primeList:
    # if can make eight, stop. It's done