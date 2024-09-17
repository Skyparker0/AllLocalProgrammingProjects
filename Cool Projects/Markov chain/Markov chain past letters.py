# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 10:07:18 2021

@author: batte
"""

#markov chain several words back

import random

PAST_WORDS = 4

paths = ["markov.txt",
         "C:/Users/batte/OneDrive/_Parker(OUTDATED USE DRIVE)/Python/txt files/shakespeare.txt",
         "C:/Users/batte/OneDrive/_Parker(OUTDATED USE DRIVE)/Python/txt files/harrypotter.txt",
         "C:/Users/batte/OneDrive/_Parker(OUTDATED USE DRIVE)/Python/txt files/disney.txt",
         "C:/Users/batte/OneDrive/_Parker(OUTDATED USE DRIVE)/Python/txt files/Words.txt"
         ]

filepath = paths[4]

text = ""

with open(filepath, encoding="utf8") as handle:
    # for i in range(1000):
    #     text += next(handle)
    for line in handle:
        text += line.strip("\n") + " "
        
text = text[:100000]
        
def text_to_words(text):
    # text = text.replace("\n", " ")
    # text = text.lower()
    
    letters = [x for x in text]
    random.shuffle(letters)
    return letters

def make_markov_chain(text):
    markovChain = {}     #{I:[[am],[a],[coder]]}
    
    letters = text_to_words(text)
    
    for index in range(len(letters)-1):
        letter = letters[index]
        
        if letter not in markovChain:
            markovChain[letter] = [[] for i in range(PAST_WORDS)]
            
        for addition in range(1,PAST_WORDS+1):
            newIndex = index+addition
            
            if newIndex >= len(letters):
                break
            
            markovChain[letter][addition-1].append(letters[newIndex])
    
    return markovChain

chain = make_markov_chain(text)

def make_word(markovChain=chain):
    MULTIPLIER = 0.5
    
    letters = []
    
    letters.append(random.choice(list(markovChain.keys())))
    
    while letters[-1][-1] != " ":
        pointValue = 1
        wordProbs = {} #{a:1.5}
        
        for howManyBack in range(1,PAST_WORDS+1):
            if howManyBack > len(letters):
                break
            
            stemWord = letters[-howManyBack]
            for nextWord in markovChain[stemWord][howManyBack-1]:
                if nextWord not in wordProbs:
                    wordProbs[nextWord] = 0
                    
                wordProbs[nextWord] += pointValue
                
            pointValue *= MULTIPLIER
                        
        chosenWord = random.choices(list(wordProbs.keys()),list(wordProbs.values()))[0]
        
        letters.append(chosenWord)
        
    return "".join(letters)


print(make_word())
                