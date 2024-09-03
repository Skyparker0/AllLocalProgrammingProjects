# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 07:12:28 2022

@author: batte
"""

#Anagrams

allWords = []
 
with open("Words.txt") as handle:
    for line in handle:
        allWords.append(line.strip("\n").lower())
        

def anagramsOf(text, wordlistPos=0):
    for index in range(wordlistPos)