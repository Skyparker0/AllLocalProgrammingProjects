# -*- coding: utf-8 -*-
"""
Created on Sun May  2 08:37:15 2021

@author: batte
"""

import random

allCards = list(range(0,21)) * 2

random.shuffle(allCards)

cardsOnTable = [allCards.pop() for i in range(6)]

playerOneDeck = allCards[:len(allCards)//2]
playerTwoDeck = allCards[len(allCards)//2:]

playerOneHand = [playerOneDeck.pop() for i in range(5)]
playerTwoHand = [playerTwoDeck.pop() for i in range(5)]

def turn():
    for tableIndex in range(6):
        for card in playerOneHand:
            if cardsOnTable[tableIndex]