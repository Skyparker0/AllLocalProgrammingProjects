# -*- coding: utf-8 -*-
"""
Created on Tue May 11 07:40:11 2021

@author: batte
"""

#closest Color

import numpy as np
import math
import noise
import pygame
import sys
import random

class Color(object):
    
    def __init__(self, x,y,color):
        self.x, self.y, self.color = x,y,color

    def get_pos(self):
        return self.x, self.y
    
    def get_color(self):
        return self.color
    
    def get_distance(self,x,y):
        return abs(self.x - x) + abs(self.y - y)#####((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5
        #return ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5
    
class Pygame_Array():
    
    def __init__(self,width,height):
        self.width, self.height = width, height
        
        self.array = np.array([[(0,0,0)]*height] * width)
        self.time = 0
        
        self.colors = []
        
        for i in range(100):
            self.colors.append(Color(random.randint(0,width),
                random.randint(0,height), 
                tuple([random.randint(0,255) for i in range(3)])
                ))
        
    def val_to_color(self, value):
        '''Value must be between 0 and 1'''
        return value
    
    def get_at(self,x,y):
        return self.array[x,y]
    
    def set_at(self,x,y,val):
        self.array[x,y] = val
    
    def update(self):
        
        for x in range(self.width):
            for y in range(self.height):
                value = (0,0,0)
                minDist = 1000
                
                for colorHolder in self.colors:
                    distance = colorHolder.get_distance(x, y)

                    if distance < minDist:
                        minDist = distance
                        value = colorHolder.get_color()
                        
                        
                    if distance < 1:
                        value = (255,0,0)
                        
                # value = (max(round(255 * (minDist + 0.1)/100), 255),) * 3
                
                self.set_at(x,y,value)
                
    def draw(self, surface):
        for x in range(self.array.shape[0]):
            for y in range(self.array.shape[1]):
                pygame.draw.rect(surface, self.val_to_color(self.get_at(x,y)), 
                                 pygame.Rect(x*TILE_SIZE,y*TILE_SIZE,TILE_SIZE,TILE_SIZE))
                

WIDTH,HEIGHT,TILE_SIZE = 500,500, 3


arr = Pygame_Array(WIDTH//TILE_SIZE,HEIGHT//TILE_SIZE)

arr.update()

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                        
    screen.fill((0,0,0))
    
    
    arr.draw(screen)
    
    pygame.display.flip()
    clock.tick(10)