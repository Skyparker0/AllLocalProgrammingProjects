# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 17:08:00 2020

@author: batte
"""

import numpy as np
import pygame

class sandbox:
    
    def __init__(self, width, height):
        self.grains = np.array([[0]*height]*width)
        self.width = width
        self.height = height
        
    def swap(self, x1,y1,x2,y2):
        self.grains[x1,y1], self.grains[x2,y2] = self.grains[x2,y2], self.grains[x1,y1]
        
    def put(self, x, y, setTo):
        self.grains[x][y] = setTo
        
    def move_all(self):
        snapshot = self.grains.copy()
        
        for pos in [(x,y) for x in range(self.width) for y in range(self.height)]:
            if snapshot[pos] == 1:
                try:
                    if snapshot[pos[0],pos[1]+1] == 0:
                        self.swap(pos[0],pos[1],pos[0],pos[1]+1)
                except IndexError:
                    pass
                
    def print_out(self):
        for pos in [(x,y) for x in range(self.width) for y in range(self.height)]: