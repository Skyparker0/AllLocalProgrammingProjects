# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 10:07:18 2021

@author: batte
"""

#markov chain several words back

import random

PAST_WORDS = 5

paths = ["markov.txt",
         "C:/Users/batte/OneDrive/_Parker/Python/txt files/shakespeare.txt",
         "C:/Users/batte/OneDrive/_Parker/Python/txt files/harrypotter.txt",
         "C:/Users/batte/OneDrive/_Parker/Python/txt files/disney.txt"
         ]

filepath = paths[3]

text = ""

with open(filepath, encoding="utf8") as handle:
    # for i in range(1000):
    #     text += next(handle)
    for line in handle:
        text += line
        
        
def text_to_words(text):
    # text = text.replace("\n", " ")
    # text = text.lower()
    
    words = text.split()
    return words

def make_markov_chain(text):
    markovChain = {}     #{I:[[am],[a],[coder]]}
    
    words = text_to_words(text)
    
    for index in range(len(words)-1):
        word = words[index]
        
        if word not in markovChain:
            markovChain[word] = [[] for i in range(PAST_WORDS)]
            
        for addition in range(1,PAST_WORDS+1):
            newIndex = index+addition
            
            if newIndex >= len(words):
                break
            
            markovChain[word][addition-1].append(words[newIndex])
    
    return markovChain

chain = make_markov_chain(text)

def make_sentance(markovChain=chain):
    MULTIPLIER = 0.5
    
    words = []
    
    words.append(random.choice(list(markovChain.keys())))
    
    while words[-1][-1] != ".":
        pointValue = 1
        wordProbs = {} #{a:1.5}
        
        for howManyBack in range(1,PAST_WORDS+1):
            if howManyBack > len(words):
                break
            
            stemWord = words[-howManyBack]
            for nextWord in markovChain[stemWord][howManyBack-1]:
                if nextWord not in wordProbs:
                    wordProbs[nextWord] = 0
                    
                wordProbs[nextWord] += pointValue
                
            pointValue *= MULTIPLIER
                        
        chosenWord = random.choices(list(wordProbs.keys()),list(wordProbs.values()))[0]
        
        words.append(chosenWord)
        
    return " ".join(words)
                