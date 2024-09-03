# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 08:02:50 2022

@author: batte
"""

allWords = []
path = "C:/Users/batte/OneDrive/_Parker/Python/txt files/Words.txt"

with open(path) as handle:
    for line in handle:
        allWords.append(line.strip("\n").lower())
        
        
def working_words(startingLetter, letterSides, wantedLetters = ""):
    workingList = []
    
    for word in allWords:
        if word[0] == startingLetter or startingLetter == "":
            works = True
            oldSide = None
            for i in range(len(word)):
                chosenSide = None
                for side in range(4):
                    if word[i] in letterSides[side]:
                        chosenSide = side
                        break
                if chosenSide == None:
                    works = False
                if chosenSide == oldSide:
                    works = False
                oldSide = chosenSide
            if works:
                workingList.append(word)
            
    def sortMetric(word):
        return len(set(l for l in word)) + (sum([i in word for i in wantedLetters])*5)
            
    return sorted(workingList,key = sortMetric,reverse=True)