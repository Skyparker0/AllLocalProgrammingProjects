# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 07:41:30 2021

@author: batte
"""

#Markov.py

import random

def text_to_words(text):
    # text = text.replace("\n", " ")
    text = text.lower()
    
    words = text.split()
    return words

def make_markov_chain(text):
    markovChain = {}     #{apple:[pie,pie,pie]}
    
    words = text_to_words(text)
    
    for index in range(len(words)-1):
        word = words[index]
        nextWord = words[index+1]
        
        if word in markovChain:
            markovChain[word].append(nextWord)
        else:
            markovChain[word] = [nextWord]
    
    return markovChain

def make_sentance(text):
    chain = make_markov_chain(text)
    
    sentance = ""
    
    lastWord = random.choice(list(chain.keys()))
    
    sentance += lastWord + " "
    
    while True:
        if lastWord not in chain:
            return sentance
        lastWord = random.choice(chain[lastWord])
        sentance += lastWord + " "
        if "." in lastWord:
            return sentance

filepath = "Cool Projects\Markov chain\markov.txt"

text = ""

with open(filepath, encoding="utf8") as handle:
    # for i in range(1000):
    #     text += next(handle)
    for line in handle:
        text += line

print(text)



