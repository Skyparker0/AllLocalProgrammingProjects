# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 14:21:38 2021

@author: batte
"""

#P86

import math


# def min_path(x,y,z):
#     sortedXYZ = sorted([x,y,z])
#     distance = math.sqrt((sortedXYZ[0] + sortedXYZ[1])**2 + sortedXYZ[2] ** 2)
#     return distance

# def shortest_path_int(M):
#     total = 0
#     for x in range(1,M+1):
#         for y in range(x,M+1):
#             for z in range(y,M+1):
#                 minPath = min_path(x,y,z)
#                 if int(minPath) == minPath:
#                     #print(x,y,z)
#                     total += 1
#     return total

def integer_length_paths(M):
    LIMIT = M*5
    
    legPairs = set()
    for s in range(3, int(math.sqrt(LIMIT)) + 1, 2):
        for t in range(s - 2, 0, -2):
            if math.gcd(s, t) == 1:
                a = s * t
                b = (s * s - t * t) // 2
                if b <= M or a <= M:
                    for mult in range(1,M//min(a,b) + 1):
                        legPairs.add((a*mult, b*mult))
                    
    legPairs = [sorted(t) for t in legPairs]
    
    total = 0
    
    for pair in legPairs:
        if pair[0] >= pair[1]//2:
            total += pair[1]//2 - (pair[1] - pair[0] - 1)
        if pair[1] <= M:
            total += pair[0]//2
            
    return total


M = 1
while True:
    M += 1
    if integer_length_paths(M) > 1000000:
        print(M)
        break