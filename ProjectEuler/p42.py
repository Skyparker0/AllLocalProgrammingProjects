# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 07:48:14 2021

@author: batte
"""

def wordToValue(word):
    alphabet = " abcdefghijklmnopqrstuvwxyz"
    total = 0
    for letter in word.lower():
        total += alphabet.index(letter)
    return total

triangleNumbers = [0]
for n in range(1,1001):
    triangleNumbers.append(triangleNumbers[-1] + n)
    
def isTriangleWord(word):
    return wordToValue(word) in triangleNumbers

with open("C:/Users/batte/OneDrive/_Parker/Python/ProjectEuler/non-code-files/p042_words.txt", "r") as handle:
    text = handle.read()
    words = text[1:-1].split('''","''')

count = 0
for word in words:
    if isTriangleWord(word):
        count += 1
        print(word, count)