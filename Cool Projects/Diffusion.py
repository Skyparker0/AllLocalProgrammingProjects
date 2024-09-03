# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 07:26:23 2020

@author: batte
"""

import numpy as np
import pygame
import sys

WIDTH = 20
HEIGHT = 20
DRAWSIZE = 30

waterSurface = np.zeros((WIDTH,HEIGHT))

def update(water, seepAmmount):
    '''If seep ammount is bigger, it takes longer to diffuse'''
    newWater = water.copy()
    
    for x in range(1, water.shape[0]-1):
        for y in range(1, water.shape[1]-1):
            newWater[x,y] = (np.sum(water[x-1:x+2, y-1:y+2]) + water[x,y] * seepAmmount)/(9 + seepAmmount)
            
    return newWater

def draw(water, screen):
    drawSize = min(screen.get_size()) // min(water.shape)
    def color(value):
        return [np.ceil(value)/10 * 255] * 3#tuple([np.floor(value/10 * 255)] * 3)
    
    for x in range(0, water.shape[0]):
        for y in range(0, water.shape[1]):
            pygame.draw.circle(screen, color(water[x,y]), 
                               (drawSize//2 + drawSize * x, drawSize//2 + drawSize * y), 
                               drawSize//2)
            
            
pygame.init()
screen = pygame.display.set_mode((WIDTH * DRAWSIZE, HEIGHT*DRAWSIZE))
clock = pygame.time.Clock()

#####
waterSurface[5,5] = 10
waterSurface[10,5] = 10
waterSurface[15,5] = 10
#####

while True:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        
    screen.fill((0,0,0))
    waterSurface = update(waterSurface,0)
    draw(waterSurface, screen)
    pygame.display.flip()
    clock.tick(1)