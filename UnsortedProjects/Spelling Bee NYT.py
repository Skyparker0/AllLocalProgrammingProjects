# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 09:46:49 2020

@author: batte
"""

#spelling Bee

dictFile = open('txt files/RegularWords.txt','r')
lines = dictFile.readlines()
lines = [l.strip('\n').lower() for l in lines]
dictFile.close()

def spellingBee(letters):
    legal = {}
    
    needed = letters[0]
    
    for word in lines:
        if (needed in word) and (not False in [letter in letters for letter in word])\
            and len(word) >= 4:
            legal[word] = (1 if len(word) == 4 else len(word))\
                + (7 if [l for l in letters if l not in word] == [] else 0)
    return legal


legalWords = spellingBee([x.lower() for x in input("Enter seven letters, with the center letter first: ")])


best = 0
bestword = ''

sorted_words = sorted(legalWords.items(), key=lambda kv: kv[1])

for x in sorted_words:
    print(x)
'''
for x in legalWords:
    print(x, legalWords[x])
    if legalWords[x] > best:
        best = legalWords[x]
        bestword = x
        
print(bestword,best)
    '''