# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 07:51:56 2021

@author: batte
"""

#P69
import math

# def is_prime(x):
# 	if x <= 1:
# 		return False
# 	elif x <= 3:
# 		return True
# 	elif x % 2 == 0:
# 		return False
# 	else:
# 		for i in range(3, int(math.sqrt(x)) + 1, 2):
# 			if x % i == 0:
# 				return False
# 		return True


# primes = []
# for i in range(1,1001,2):
#     if is_prime(i):
#         primes.append(i)
        
# def phi(n):
#     nonRelPrimes = 0
    
#     limit = int(math.sqrt(n))
#     if limit * limit == n:
#         nonRelPrimes -= 1
        
#     i = 0
#     while True:
#         prime = primes[i]
#         if prime > limit:
#             break
        
        
#         i += 1

# def phi(n):
#     sqrtN = int(math.sqrt(n))
#     nonRelPrimes = set([n])
#     for i in range(2,sqrtN+1):
#         if n % i == 0 and i not in nonRelPrimes:
#             nonRelPrimes.add(n//i)
#             for nonRel in range(i,n,i):
#                 nonRelPrimes.add(nonRel)
#     return n - len(nonRelPrimes)

# def val(n):
#     return n/phi(n)



# bestN = 0
# bestVal = 0
# for N in range(2,1000001,2):
#     value = val(N)
#     if value > bestVal:
#         bestN = N
#         bestVal = value
        
ans = 2*3*5*7*11*13*17 #to not be realitively prime with as many number as
#possible, has to have as many factors as possible.

        # 2*3*5*7*11*13*17
        # = 510510