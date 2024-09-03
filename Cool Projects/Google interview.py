# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 06:28:44 2020

@author: batte
"""

##telephone

# import numpy as np

# keyPad = np.array([[-1]*7]*8)

# keyPad[2][2:5] = [7,8,9]
# keyPad[3][2:5] = [4,5,6]
# keyPad[4][2:5] = [1,2,3]
# keyPad[5][3] =      0


numberPairs = {
    0:[4,6],
    1:[8,6],
    2:[7,9],
    3:[4,8],
    4:[9,3,0],
    5:[],
    6:[7,1,0],
    7:[2,6],
    8:[1,3],
    9:[4,2]
    }

def phone_numbers(startNum, length):
    if length == 1:
        return [str(startNum)]
    else:
        result = []
        for miniList in [phone_numbers(x,length-1)  for x in numberPairs[startNum]]:
            result.extend([str(startNum) + miniList[x] for x in range(len(miniList))])
        return result