# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 08:03:24 2021

@author: batte
"""

import math

def find_triples(limit):
    triples = set() #list of threeples (a,b,c)
    for c in range(3, limit + 1):
        for b in range(1,c):
            a = (c**2 - b**2) ** 0.5
            if int(a) == a:
                triples.add(tuple(sorted((int(a),b,c))))
    return triples

triples = find_triples(500)
sums = {0:[0]}
for triple in triples:
    tripleSum = sum(triple)
    if tripleSum in sums:
        sums[tripleSum][0] += 1
        sums[tripleSum].append(triple)
    else: 
        sums[tripleSum] = [1,triple]
        
sums = dict(sorted(sums.items(), key=lambda item: item[1][0]))