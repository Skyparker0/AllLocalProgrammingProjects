# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 17:12:21 2021

@author: batte
"""

### odd cards

import random

def play_hand():
    '''Returns 0 if the even player wins, 1 if the odd player wins, tie if tie'''
    deck = [1,1,1,2,2] * 4
    random.shuffle(deck)
    oddPlayerHand = deck[:len(deck)//2]
    evenPlayerHand = deck[len(deck)//2:]
    scores = [0,0] #scores[0] = even player's score
    
    # print(oddPlayerHand)
    # print(evenPlayerHand)

    
    for i in range(len(deck)//2):
        # print(oddPlayerHand[-1], evenPlayerHand[-1])
        total = oddPlayerHand.pop() + evenPlayerHand.pop()
        scores[total%2] += 2
        
    if scores[0] > scores[1]:
        return 0
    elif scores[1] > scores[0]:
        return 1
    else:
        return 'tie'
    
results = []

for test in range(10000):
    results.append(play_hand())
    
print('odd wins', results.count(1), 'even wins', results.count(0))