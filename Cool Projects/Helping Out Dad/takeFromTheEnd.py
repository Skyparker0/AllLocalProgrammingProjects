# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 08:00:46 2022

@author: batte
"""

#Take From the End game

def solve_sequence(numberList):
    if len(numberList) == 2:
        return numberList[0] - numberList[1], numberList[1]-numberList[0]
    return numberList[0] - max(solve_sequence(numberList[1:])), numberList[-1] - max(solve_sequence(numberList[:-1]))
        
    