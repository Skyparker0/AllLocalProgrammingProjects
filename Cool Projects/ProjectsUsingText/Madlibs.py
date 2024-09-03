# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 16:49:37 2022

@author: batte
"""

# Mad Libs

import random

autoFill = input("AUTO-FILL OR USER-FILL (1 or 2): ") != "2"

textToLib = """
Cheese is valued for its portability, long shelf life, and high content of fat, protein, calcium, and phosphorus. Cheese is more compact and has a longer shelf life than milk, although how long a cheese will keep depends on the type of cheese.[3] Hard cheeses, such as Parmesan, last longer than soft cheeses, such as Brie or goat's milk cheese. The long storage life of some cheeses, especially when encased in a protective rind, allows selling when markets are favorable. Vacuum packaging of block-shaped cheeses and gas-flushing of plastic bags with mixtures of carbon dioxide and nitrogen are used for storage and mass distribution of cheeses in the 21st century.
"""

paths = ["C:/Users/batte/OneDrive/_Parker/Python/word_files/nouns.txt",
    "C:/Users/batte/OneDrive/_Parker/Python/word_files/adjectives.txt",
    "C:/Users/batte/OneDrive/_Parker/Python/word_files/verbs.txt",
    "C:/Users/batte/OneDrive/_Parker/Python/word_files/adverbs.txt"]

nounList = []
with open(paths[0]) as handle:
    for line in handle:
        nounList.append(line.strip("\n").lower())

adjectiveList = []
with open(paths[1]) as handle:
    for line in handle:
        adjectiveList.append(line.strip("\n").lower())

verbList = []
with open(paths[2]) as handle:
    for line in handle:
        verbList.append(line.strip("\n").lower())

adverbList = []
with open(paths[3]) as handle:
    for line in handle:
        adverbList.append(line.strip("\n").lower())


def madlib(text):
    words = text.split()
    for i in range(0,len(words),1):
        lowerWord = words[i].lower()
        if autoFill:
            if lowerWord in nounList:
                words[i] = random.choice(nounList)
            # if lowerWord in adjectiveList:
            #     words[i] = random.choice(adjectiveList)
            # if lowerWord in verbList:
            #     words[i] = random.choice(verbList)
            # if lowerWord in adverbList:
            #     words[i] = random.choice(adverbList)
        else:
            if lowerWord in nounList:
                words[i] = input("Noun ")
            if lowerWord in adjectiveList:
                words[i] = input("Adjective ")
            if lowerWord in verbList:
                words[i] = input("Verb ")
            if lowerWord in adverbList:
                words[i] = input("Adverb ")
                
    return " ".join(words)
            
print(madlib(textToLib))