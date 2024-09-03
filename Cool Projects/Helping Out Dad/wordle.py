# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 15:07:15 2022

@author: batte
"""

# WORDLE

allWordleWords = []
path = "../../word_files/wordles_all_words.txt"

with open(path) as handle:
    for line in handle:
        allWordleWords.append(line.strip("\n"))
        
realWordleSolutions = []
path = "../..//word_files/real_wordles.txt"

with open(path) as handle:
    for line in handle:
        realWordleSolutions.append(line.strip("\n")+"*")
        
letterFrequency = {letter:[0,0,0,0,0] for letter in "abcdefghijklmnopqrstuvwxyz"}
for word in realWordleSolutions:
    for letterIndex in range(5):
        letterFrequency[word[letterIndex]][letterIndex] += 1 

def follow_rules(listToChange, unusables, wrongPlace, rightPlace):
    
    global letterFrequency
    
    def score(word):
        score = 0
        
        usedLetters = []
        
        for letterIndex in range(5):
            if word[letterIndex] in usedLetters:
                continue
            usedLetters.append(word[letterIndex])
            score += newLetterFrequency[word[letterIndex]][letterIndex]
            
        return score
    
    newList = []
    
    for word in listToChange:
        passes = True
        for i in range(5):
            if word[i] in unusables:
                passes = False
            if word[i] == wrongPlace[i]:
                passes = False
            if word[i] != rightPlace[i] and rightPlace[i] != ".":
                passes = False
                
        for x in wrongPlace:
            if x != "." and x not in word:
                passes = False
                
        if passes:
            newList.append(word)
    
    newLetterFrequency = {letter:[0,0,0,0,0] for letter in "abcdefghijklmnopqrstuvwxyz"}
    for word in listToChange:
        for letterIndex in range(5):
            newLetterFrequency[word[letterIndex]][letterIndex] += 1 
    
    returnList = sorted(newList,key = score,reverse = True)
    print(returnList[:5])
    return returnList

sortedWords = realWordleSolutions #+ allWordleWords
sortedWords = follow_rules(sortedWords, ".....", ".....", ".....")
sortedWords = follow_rules(sortedWords, "s..t.", ".la.e", ".....")
sortedWords = follow_rules(sortedWords, "b...r", "..l..", ".a.e.")
sortedWords = follow_rules(sortedWords, "p.n..", ".....", ".a.el")