# -*- coding: utf-8 -*-
"""
Created on Thu May  6 14:17:45 2021

@author: batte
"""

import math

def sin(degrees):
    return round(math.sin(math.radians(degrees)),5)

def asin(oOverH):
    return round(math.degrees(math.asin(oOverH)),5)

def cos(degrees):
    return round(math.cos(math.radians(degrees)),5)

def acos(aOverH):
    return round(math.degrees(math.acos(aOverH)),5)


def newPosition(start,degrees, center):
    '''Automaticly clockwise and around (0,0)
    returns the end-coordinate resulting from the start coord turning degrees'''
    x,y = start    #adjacent, opposite
    
    h = ((x-center[0])**2 + (y-center[1])**2)**0.5   #Hypotenuse
    
    angle = asin((y-center[1])/h)
    newAngle = angle - degrees #add degrees if counterclockwise

    newX = center[0] + cos(newAngle) * h
    newY = center[1] + sin(newAngle) * h
    
    return (round(newX,3), round(newY,3))
    
    