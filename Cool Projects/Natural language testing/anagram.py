# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 17:45:53 2021

@author: batte
"""

#Anagram

allWords = []
filepath = "anagramWords.txt"
with open(filepath) as handle:
    for line in handle:
        fixedWord = line.strip("\n").lower()
        if len(fixedWord) > 2:
            allWords.append(fixedWord)
        
        
def solve_anagrams(startString, words):
    completedAnagrams = []
    wordToGoal = {}
    
    for word in words:
        modifiedString = startString[:]
        flag = True
        for character in word:
            if character in modifiedString:
                characterIndex = modifiedString.find(character)
                modifiedString = modifiedString[:characterIndex] \
                    + modifiedString[characterIndex+1:]
            else:
                flag = False
                break
        if flag:
            wordToGoal[word] = modifiedString
            
    newWords = list(wordToGoal.keys())
            
    for word in wordToGoal:
        if wordToGoal[word] == "":
            completedAnagrams.append(word)
        for extendedAnagram in solve_anagrams(wordToGoal[word],newWords):
            completedAnagrams.append(word + " " + extendedAnagram)
            
    completedAnagrams = set([" ".join(sorted(ana.split())) for ana in completedAnagrams])
    return completedAnagrams
    