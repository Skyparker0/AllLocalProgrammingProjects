# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 07:38:42 2021

@author: batte
"""

#P54

# from lowest to highest, in the following way:

#     High Card: Highest value card.
#     One Pair: Two cards of the same value.
#     Two Pairs: Two different pairs.
#     Three of a Kind: Three cards of the same value.
#     Straight: All cards are consecutive values.
#     Flush: All cards of the same suit.
#     Full House: Three of a kind and a pair.
#     Four of a Kind: Four cards of the same value.
#     Straight Flush: All cards are consecutive values of same suit.
#     Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

class Hand(object):
    
    def __init__(self, cardText):
        self.cards = cardText.split()
