# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 07:43:31 2021

@author: batte
"""

# Sand Simulation

import numpy as np
import pygame
import sys
import random

def pixel_to_color(pixelNum):
    return [(255,255,255), (200,170,0), (0,0,200), (110,70,30)][int(pixelNum)]

class Rule:
    
    def __init__(self, startPixel, thingsToSwap, positionsToSwapWith):
        """
        Parameters
        ----------
        startPixel : int, 0 or more
            This is the kind of substance that will be swapping with thingsToSwap.
        thingsToSwap : list of ints
            All the kinds of materials (can just be one) that will
            get swapped with the start pixel (if in positionsToSwapWith).
        positionsToSwapWith : list of tuples
            A list of "change values," [(0,1)] would mean the startPixel swaps with any of the
            thingsToSwap if they are directly beneath it (+0x, +1y).
    
        Returns
        -------
        None.
        """
        
        self.startPixel = startPixel
        self.thingsToSwap = thingsToSwap
        self.positionsToSwapWith = positionsToSwapWith
        
    def get_start(self):
        return self.startPixel
    
    def get_swaps(self):
        return self.thingsToSwap
    
    def get_positions(self):
        return self.positionsToSwapWith
    
materials = {
    0:'air',
    1:'sand',
    2:'water',
    3:'wood',
    4:''
             }
    
rules = [   #must be written in order; sand falls down before left or right.
         #sand
    Rule(1, [0,2], [(0,1)]),
    Rule(1, [0,2], [(-1,1),(1,1)]),
        #water
    Rule(2, [0], [(0,1)]),
    Rule(2, [0], [(-1,1),(1,1)]),
    Rule(2, [0], [(-1,0),(1,0)]),
        #wood
    ]

class Sandbox(object):
    '''
    An array holding a grid of empty space, sand, and possibly other things (water, fire,
    steam, wood, stone, etc.)
    Can update all positions, add sand (and others) in, and draw to a pygame surface
    
    (in array) Numbers for substances; 0 = air, 1 = sand'''
    
    def __init__(self, width,height):
        self.width = width
        self.height = height
        self.array = np.zeros((width,height))
        
    def __str__(self):
        output = ""
        for y in range(self.height):
            for x in range(self.width):
                output += self.get_at(x,y)
            output += "\n"
                
    def get(self,x,y):
        if 0 > y or y >= self.height or 0 > x or x >= self.width:
            return None
        return self.array[x,y]
        
    def get_size(self):
        return (self.width, self.height)
    
    def get_array(self):
        return self.array
    
    def put(self,x,y,number):
        if 0 > y or y >= self.height or 0 > x or x >= self.width:
            return None
        self.array[x,y] = number
        
    def swap(self, coord1, coord2):
        c1 = self.get(coord1[0], coord1[1])
        c2 = self.get(coord2[0], coord2[1])
        
        self.put(coord2[0], coord2[1], c1)
        self.put(coord1[0], coord1[1], c2)
        
    def use_rule(self,rule,x,y):
        '''
        applies a rule, rule, at x,y.
        returns None if the rule yeilds no swaps for the position, or a position to swap
        x,y with (so if 5,5 is returned, the pixel at x,y is swapped with that at 5,5)'''
        
        start = rule.get_start()
        swaps = rule.get_swaps()
        positions = rule.get_positions() #so the sand may fall left or right randomly
        
        random.shuffle(positions)
        
        if self.get(x,y) != start:
            return None
        
        for positionChange in positions:
            newPosition = (x + positionChange[0], y + positionChange[1])
            if self.get(newPosition[0],newPosition[1]) in swaps:
                return newPosition
            
        return None
        
        
    def update(self):
        '''Goes through every point, from bottom to top, updating it based on neighbors.'''
        yVals = list(range(self.height-1, -1, -1))
        #random.shuffle(yVals)
        for y in yVals:
            xVals = list(range(0, self.width))
            random.shuffle(xVals)
            for x in xVals:
                for rule in rules:
                    result = self.use_rule(rule, x, y)
                    if result != None:
                        self.swap((x,y), result)
                # if self.get(x,y) == 1:
                #     if self.get(x,y+1) == 0:
                #         self.swap((x,y), (x,y+1))
                #     else:
                #         checkCoords = [x-1, x+1]
                #         random.shuffle(checkCoords)
                #         for i in range(2):
                #             if self.get(checkCoords[i], y+1) == 0:
                #                 self.swap((x,y), (checkCoords[i],y+1))
                #                 break
                    
                    
                        
    def draw(self, surface):
        for y in range(self.height):
            for x in range(self.width):
                pixel = self.get(x,y)
                color = pixel_to_color(pixel)
                pygame.draw.rect(surface,color,pygame.Rect(x * PIXEL_SIZE,y * PIXEL_SIZE\
                                                           ,PIXEL_SIZE,PIXEL_SIZE))
                
                

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
PIXEL_SIZE = 10
TIME = 0

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
    
sandbox = Sandbox(SCREEN_WIDTH//PIXEL_SIZE, SCREEN_HEIGHT//PIXEL_SIZE)


chosenMaterial = 1
matLower, matUpper = 0,3
mouseDown = False

def placementHandling(surface):
    pygame.draw.rect(surface,(220,220,220),pygame.Rect(0,0,60,60))
    pygame.draw.circle(surface, pixel_to_color(chosenMaterial), (30,30),30)
    
    if mouseDown:
        mx, my = pygame.mouse.get_pos()
        
        mx //= PIXEL_SIZE
        my //= PIXEL_SIZE
        
        sandbox.put(mx,my,chosenMaterial)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouseDown = True
                
            if event.button == 4:
                chosenMaterial += 1
                
            if event.button == 5:
                chosenMaterial -= 1
                
            if chosenMaterial < matLower:
                chosenMaterial = matUpper
            if chosenMaterial > matUpper:
                chosenMaterial = matLower
                
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouseDown = False
                        
    screen.fill((0,0,0))
    sandbox.update()
    sandbox.draw(screen)
    placementHandling(screen)
    pygame.display.flip()
    
    TIME += 0.1
    clock.tick(30)