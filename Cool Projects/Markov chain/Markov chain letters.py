# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 10:18:26 2021

@author: batte
"""

#word maker

import random

filepath = "C:/Users/batte/OneDrive/_Parker/Python/Cool Projects/Markov chain/markov.txt"

text = ""

with open(filepath, encoding="utf8") as handle:
    # for i in range(1000):
    #     text += next(handle)
    for line in handle:
        text += line
        
chain = {}

for index in range(len(text)-1):
    char = text[index]
    
    if char in chain:
        chain[char].append(text[index+1])
    else:
        chain[char] = [text[index+1]]
        
        
        
sentance = ""   
while len(sentance) < 20:
    sentance = ""
    
    lastChar = random.choice(list(chain.keys()))
    
    sentance += lastChar
    
    while lastChar != " ":
        lastChar = random.choice(chain[lastChar])
        
        sentance += lastChar
    
print(sentance)