# -*- coding: utf-8 -*-
"""
Created on Sat May  1 06:09:45 2021

@author: batte
"""

#KillFeed

# nameGenerator- has things like "noun/_/noun", "adj/noun", etc
# returns a random name

# killFeedGenerator- creates ways for playerA to kill playerB, using things like
# "pA/through a /melee/ at /pB"

# 100 random names generated

# the killFeedGenerator is used to kill off all the players till 1 remains.

import random

def get_words(filePath):
    words = []
    with open(filePath) as handle:
        for line in handle:
            words.append(line[:-1].lower())
    return words

class WordType(object):
    '''
    usage: Vegetable = WordType(['potato', 'corn', 'Broccoli'])
    '''
    
    def __init__(self,words):
        self.words = words
        
    def __str__(self):
        return str(random.choice(self.words))
        

class WordCombo(object):
    '''Is fed a list of strings and WordTypes, can be asked to return a randomized
    output:
        WordCombo(["I Like", Vegetable]).create_combo() -> "I Like potato"'''
        
    def __init__(self,comboList):
        self.comboList = comboList
        
    def __str__(self):
        return ''.join([str(w) for w in self.comboList])
    
noun = WordType(get_words("TxtFiles/nouns.txt"))
verb = WordType(get_words("TxtFiles/verbs.txt"))
adjective = WordType(get_words("TxtFiles/adjectives.txt"))
adverb = WordType([x.strip(" ") for x in get_words("TxtFiles/adverbs.txt")])

name = WordType(get_words("TxtFiles/names.txt"))

animal = WordType(get_words("TxtFiles/animals.txt"))

number = WordType([i for i in range(0,100)])
connection = WordType(["_","-"])

# playerName = WordType([
#     WordCombo(["_",noun,number,"_"]),
#     WordCombo([noun,connection,noun]),
#     WordCombo([noun,connection,number]),
#     WordCombo([adjective, connection, animal, connection, number]),
#     WordCombo([name, connection, name]),
#     WordCombo([adjective,connection,verb])
#     ])

beastName = WordCombo([adjective, "_", animal, "_", number])

listOfBeastNames = []

while len(listOfBeastNames) < 500:
    possibleBeastName = str(beastName)
    beastNameWords = possibleBeastName.split("_")
    if beastNameWords[0][0] == beastNameWords[1][0]:
        listOfBeastNames.append(possibleBeastName)

player = WordType(listOfBeastNames)

meleeBlunt = WordCombo([adjective, " ", WordType(["rock","pan",
                    "piece of bread","club","pebble","tree branch"])])
meleeSharp = WordCombo([adjective, " ", WordType(["sharpened stick", 
                    "longsword","set of silverware","shark tooth","wooden spear",])])


elimination = WordType([
    WordCombo([player, " ", adverb, " hit ", player, " over the head with a ", meleeBlunt]),
    WordCombo([player, " was hit by a ", meleeBlunt, " dropped by ", player]),
    WordCombo([player, " ", adverb, " threw a ", meleeBlunt, " at ", player]),
    WordCombo([player, " poked ", player, " ", adverb, " with a ", meleeSharp]),
    WordCombo([player, " swung at ", player, " with a ", meleeSharp]),
    WordCombo([player, " stepped on a ", meleeSharp, " ", adverb, " placed by ", player])
    ])