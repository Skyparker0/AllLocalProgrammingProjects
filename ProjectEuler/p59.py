# -*- coding: utf-8 -*-
"""
Created on Sat May 22 07:49:35 2021

@author: batte
"""

#P59

#ord   chr

filepath = "C:/Users/batte/OneDrive/_Parker/Python/ProjectEuler/non-code-files/p059_cipher.txt"

def decrypt(number, code):
    return chr(number ^ code)

def get_text(numList, code):
    text = ""
    for i,num in enumerate(numList):
        text += decrypt(num,code[i%len(code)])
        
    return text
       
# englishWords = []
# with open('C:/Users/batte/OneDrive/_Parker/Python/Words.txt') as handle:
#     for line in handle:
#         englishWords.append(line.strip('\n').lower())
# def count_words(text):
#     words = [word.lower() for word in text.split(' ')]
#     count = sum([1 for word in words if word in englishWords])
#     return count    

goodChars = [i for i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "]
def get_score(text):
    score = 0
    for letter in text:
        if letter in goodChars:
            score += 1
        else:
            score -= 1
    return score
    

   
numbers = []
with open(filepath) as handle:
    for line in handle:
        numbers.extend([int(n) for n in line.split(',')])


        
bestScore = 0
chosenText = ''
        
for a in range(97,123): #123
    for b in range(97,123):
        for c in range(97,123):
            code = (a,b,c)
            text = get_text(numbers, code)
            score = get_score(text)
        
            if score > bestScore:
                bestScore = int(score)
                chosenText = str(text)