# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 09:41:52 2021

@author: batte
"""

import math

# def integer_length_paths(M):
#     LIMIT = M*2
    
#     triples = set()
#     for s in range(3, int(math.sqrt(LIMIT)) + 1, 2):
#         for t in range(s - 2, 0, -2):
#             if math.gcd(s, t) == 1:
#                 a = s * t
#                 b = (s * s - t * t) // 2
#                 c = (s * s + t * t) // 2
#                 if c <= M:
#                     for mult in range()
#                     triples.add((a, b, c))
                    
#     return [sorted(t) for t in triples if all([x <= M for x in t])]

def integer_length_paths(M):
    LIMIT = M*10
    
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