# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 07:36:31 2021

@author: batte
"""

#P70
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
ps = [x for x in range(2,10**7 // 2)if is_prime(x)]

# def phi(n):
#     sqrtN = int(math.sqrt(n))
#     nonRelPrimes = set([n])
#     for i in range(2,sqrtN+1):
#         if n % i == 0 and i not in nonRelPrimes:
#             nonRelPrimes.add(n//i)
#             for nonRel in range(i,n,i):
#                 nonRelPrimes.add(nonRel)
#     return n - len(nonRelPrimes)

# def phi2(n):
#     limit = n//2
#     nonRel = 1 #because itself won't be caught
#     for prime in ps:
#         if prime > limit:
#             break
#         if n % prime == 0:
#             nonRel += n//prime - 1
#     return n - nonRel

# def special(n):
#     strN = str(n)
#     strPhi = str(phi(n))
#     return sorted(strN) == sorted(strPhi)

# for n in range(87100,1000000000):
#     if special(n):
#         print(n, phi(n))

#8319823, they used a really neat method