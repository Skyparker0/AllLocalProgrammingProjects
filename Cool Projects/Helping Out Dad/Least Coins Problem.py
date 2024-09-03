# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 07:40:18 2021

@author: batte
"""


# Coin problem
'''
given N types of coins (e.g. N=4, coins can =[1,5,10,25])
what distinct positive-integer coin values make change for 1 cent to 1
dollar using the least possible coins

notes: The first coin MUST be one, so all values can be reached
'''


def make_change(coinValues, goal):
    '''
    Parameters
    ----------
    coinValues : list or tuple
        What kinds of coins are to be used to make change ex. (1,5,10,25).
        coinValues[0] assumed to be 1, and coinValues in ascending order
    goal : int
        What number of cents we are trying to reach.

    Returns
    -------
    int-least coins needed.
    '''
    if len(coinValues) == 2:
        return goal // coinValues[1] + goal % coinValues[1]
    
    leastCoinsNeeded = 100000
    
    for subtractorMult in range(0, goal // coinValues[-1] + 1):    #Greedy the largest value
        subtractor = coinValues[-1] * subtractorMult    
        result = make_change(coinValues[:-1],goal - subtractor) + subtractorMult
        if result < leastCoinsNeeded:
            leastCoinsNeeded = result
            
    return leastCoinsNeeded

def coinCombos(N,start,end=None):
    if end == None:
        end = 101-N
        
    if N == 1:
        return [[i] for i in range(start, end+1)]
    
    combos = []
    for comboStart in range(start, end+1):
        ends = coinCombos(N-1,comboStart+1,end+1)
        combos.extend([[comboStart] + end for end in ends])
    return combos

def comboValue(combo):
    total = 0
    for goal in range(1,101):
        total += make_change(combo,goal)
    return total

def best_coinValues(N):
    '''
    Parameters
    ----------
    N : int
        the number of distinct coins to be used.

    Returns
    -------
    What set of N coins uses the least total coins to make change for goal =
    1 through 100.
    '''
    
    combos = [[1] + end for end in coinCombos(N-1,2)]
    
    chosenCombo = None
    leastCoins = 10000
    
    for combo in combos:
        coinsNeeded = comboValue(combo)
        if coinsNeeded < leastCoins:
            leastCoins = coinsNeeded
            chosenCombo = combo
    return chosenCombo