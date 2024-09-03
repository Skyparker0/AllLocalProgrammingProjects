# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 10:23:39 2022

@author: batte
"""

#P98


#Look through all words in the list
#For the word, find its anagram(s)
#Using every square with the same # of digits, see if rules work
#if they do, it works

path = "C:/Users/batte/OneDrive/_Parker/Python/ProjectEuler/non-code-files/p098_words.txt"

words = []

with open(path) as handle:
    for line in handle:
        words += [x.strip('"') for x in line.split(",")]
        
        
squaresOfLen = {i:[] for i in range(1,15)}
for base in range(1,10000000):
    squared = base*base
    squaresOfLen[len(str(squared))].append(squared)
    
    
def is_anagramic_square(word1,word2):
    for square in squaresOfLen[len(word1)]:
        square = str(square)
        breaksRules = False
        rules = dict()
        
        for i in range(len(word1)):
            number = square[i]
            letter = word1[i]
            
            if letter in rules and number != rules[letter]:
                breaksRules = True
                break
            
            rules[letter] = number
            
            if list(rules.values()).count(number) >= 2:
                breaksRules = True
                break
            
        if breaksRules:
            continue
        
        newNumber = ""
        for letter in word2:
            newNumber += rules[letter]
            
        if int(newNumber) in squaresOfLen[len(word1)]:
            return [int(square),int(newNumber)]
    
alreadyUsed = []

biggestSquare = 0

for word in words:
    if word in alreadyUsed:
        continue
    alreadyUsed.append(word)
    
    for otherWord in words:
        if otherWord in alreadyUsed:
            continue
        if len(otherWord) == len(word) and sorted(otherWord) == sorted(word):
            print(word,otherWord)
            result = is_anagramic_square(word,otherWord)
            if result:
                print(result)
                largerSquare = max(result)
                if largerSquare > biggestSquare:
                    biggestSquare = largerSquare
                    
print(biggestSquare)
            