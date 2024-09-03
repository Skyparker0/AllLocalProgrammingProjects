# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 07:30:56 2022

@author: batte
"""

allWordleWords = []
path = "C:/Users/batte/OneDrive/_Parker/Python/word_files/wordles_all_words.txt"

with open(path) as handle:
    for line in handle:
        allWordleWords.append(line.strip("\n"))
        
        
wantedLetters = "pjm"


def score(word):
    score = 0
    usedLetters = ""
    for i in range(5):
        if word[i] in usedLetters:
            continue
        if word[i] in wantedLetters:
            score += 1
            usedLetters += word[i]
            
    return score

print(sorted(allWordleWords,key=score,reverse=True)[:10])
