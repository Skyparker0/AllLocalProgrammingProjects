# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 17:51:06 2022

@author: batte
"""

#SpellingBee

allWords = []
path = "C:/Users/batte/OneDrive/_Parker/Python/txt files/Words.txt"

with open(path) as handle:
    for line in handle:
        allWords.append(line.strip("\n"))


def working_words(required, usables):
    workingList = []
    
    for word in allWords:
        if required in word.lower() and all([letter in usables for letter in word.lower()]) and len(word) > 3:
            workingList.append(word)
            
    return sorted(workingList,key = len,reverse=True)

