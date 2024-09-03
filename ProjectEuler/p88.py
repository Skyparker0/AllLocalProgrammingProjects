# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 08:09:24 2021

@author: batte
"""

#P88

import math

largestK = 12000

kToNumber = [0,0] + [None] * largestK


tries = {biggestNumber:[[biggestNumber]] for biggestNumber in range(2,largestK+1)}



for biggestNumber in tries:
    print(biggestNumber)
    for smallerNumber in range(2,biggestNumber+1):
        endings = tries[smallerNumber].copy()
        for numOfBigNum in range(1,int(math.log(largestK,biggestNumber)+1)):
            for end in endings:
                factors = [biggestNumber]*numOfBigNum + end
                kValue = math.prod(factors) - sum(factors) + len(factors)
                if kValue <= largestK:
                    if kToNumber[kValue] == None or kToNumber[kValue] > math.prod(factors):
                        kToNumber[kValue] = math.prod(factors)
                        print('change')
                    if factors not in tries[biggestNumber]:
                        tries[biggestNumber].append(factors)




# import math

# def prime_factorization(num):
#     remaining = int(num)
    
#     factors = []
    
#     for div in range(2,int(math.sqrt(num)) + 1):
#         if remaining % div == 0:
#             factors += [div] * (remaining//div)
#             remaining //= div
            
#     return factors

# kToNumber = {} #eg 2:4 or 3:6

# number = 4

# def min_prod_sum(k):
#     '''
#     for number in range(k, forever)
#         if number is a product-sum with k terms, number is the answer'''
    
#     number = k
#     while True:
        
        
#         number += 1