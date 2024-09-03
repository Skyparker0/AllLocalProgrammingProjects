# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 08:51:19 2021

@author: batte
"""

#P84 Did not solve

rolls = [2,3,3,4,4,4,5,5,5,5,6,6,6,7,7,8]#[2,3,3,4,4,4,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,8,9,9,9,9,10,10,10,11,11,12]#[2,3,3,4,4,4,5,5,5,5,6,6,6,7,7,8]
CCsquares = [2,17,33]
CHsquares = [7,22,36]
G2Jsquare = [30]


probDict = {square:0 for square in range(40)}



def process_land(endSquare):
    if endSquare in CCsquares:
        probDict[endSquare] += 14/16
        probDict[0] += 1/16
        probDict[10] += 1/16
    elif endSquare in CHsquares:
        probDict[endSquare] += 6/16
        
        probDict[0] += 1/16
        probDict[10] += 1/16
        probDict[11] += 1/16
        probDict[24] += 1/16
        probDict[39] += 1/16
        probDict[5] += 1/16
        
        if endSquare == 7:
            probDict[15] += 2/16
        elif endSquare == 22:
            probDict[25] += 2/16
        else:
            probDict[5] += 2/16
            
        if endSquare == 7:
            probDict[12] += 1/16
        elif endSquare == 22:
            probDict[28] += 1/16
        else:
            probDict[12] += 1/16
        
        if endSquare-3 == 33:
            probDict[33] += 14/16 * 1/16
            probDict[0] += 1/16 * 1/16
            probDict[10] += 1/16 * 1/16
        else:
            probDict[endSquare-3] += 1/16

    elif endSquare in G2Jsquare:
        probDict[10] += 1
    else:
        probDict[endSquare] += 1



for start in range(40):
    for roll in rolls:
        process_land((start+roll)%40)
        
print({k: v for k, v in sorted(probDict.items(), key=lambda item: item[1])})