# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 12:10:54 2021

@author: batte
"""

import itertools

def pairWorks(d1,d2):
    if '6' in d1 or '9' in d1:
        d1 += ('6','9')
    if '6' in d2 or '9' in d2:
        d2 += ('6','9')
        
        
    for square in ['01','04','09','16','25','36','49','64','81']:
        if (square[0] in d1 and square[1] in d2) or (square[1] in d1 and square[0] in d2):
            continue
        return False
    return True


possibleDice = list(itertools.combinations(['0','1','2','3','4','5','6','7','8','9'],6))

workingPairs = [] #eg. [[1,2,3,4],[5,6,7,8]]

for die1 in possibleDice:
    for die2 in possibleDice:
        if pairWorks(die1,die2):
            if (die1,die2) not in workingPairs and (die2,die1) not in workingPairs:
                workingPairs.append((die1,die2))
                
print(len(workingPairs))