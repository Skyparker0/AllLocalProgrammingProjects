# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 13:49:17 2021

@author: batte
"""

import random

filePath = "C:/Users/batte/OneDrive/_Parker/Python/ListOfNouns.txt"

words = []
with open(filePath) as handle:
    for line in handle:
        words.append(line[:-1].lower())
        
def find_similar(word):
    word = word.lower()
    similarWords = [w for w in words if w[0] == word[0] and w[-1] == word[-1] and w != word]
    closestWords = sorted(similarWords,key = lambda w: abs(len(w)-len(word)))
    if closestWords == []:
        return ""
    return random.choice(closestWords[:5])

def create_new_name(name):
    nameList = []
    for nameWord in name.split():
        nameList.append(find_similar(nameWord))
    return " ".join(nameList)