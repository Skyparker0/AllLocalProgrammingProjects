# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 08:28:47 2021

@author: batte
"""

#P85



def rectangles(width,height):
    return (width**2 + width)/2 * (height**2 + height)/2



best = (0,0)
bestCloseness = 10000000
for width in range(1,2001):
    for height in range(1,2001):
        howClose = abs(2000000-rectangles(width,height))
        if howClose < bestCloseness:
            bestCloseness = howClose
            best = (width,height)