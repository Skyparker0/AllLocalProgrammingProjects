# -*- coding: utf-8 -*-
"""
Created on Mon May 10 17:16:49 2021

@author: batte
"""

import numpy as np
import math
import noise
import pygame
import sys

class Pygame_Array():
    
    def __init__(self,width,height):
        self.array = np.zeros((width,height))
        self.time = 0
        
    def val_to_color(self, value):
        '''Value must be between 0 and 1'''
        return (round(value * 255),) * 3
    
    def get_at(self,x,y):
        return self.array[x,y]
    
    def set_at(self,x,y,val):
        self.array[x,y] = val
    
    def update(self):
        self.time += 0.1
        
        noiseDiv = 10
        
        for x in range(self.array.shape[0]):
            for y in range(self.array.shape[1]):
                value = (noise.pnoise3(x/noiseDiv, y/noiseDiv,self.time/noiseDiv) + 1) / 2
                self.set_at(x,y,value)
                
    def draw(self, surface):
        for x in range(self.array.shape[0]):
            for y in range(self.array.shape[1]):
                pygame.draw.rect(surface, self.val_to_color(self.get_at(x,y)), 
                                 pygame.Rect(x*TILE_SIZE,y*TILE_SIZE,TILE_SIZE,TILE_SIZE))
                

WIDTH,HEIGHT,TILE_SIZE = 500,500, 10

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

arr = Pygame_Array(WIDTH//TILE_SIZE,HEIGHT//TILE_SIZE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                        
    screen.fill((0,0,0))
    
    arr.update()
    arr.draw(screen)
    
    pygame.display.flip()
    clock.tick(30)