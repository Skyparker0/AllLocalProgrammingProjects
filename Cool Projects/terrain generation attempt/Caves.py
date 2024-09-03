# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 14:32:50 2021

@author: batte
"""

import numpy as np
import noise
import pygame
import sys
import random

NOISE_DIV_VAL = 30

def block_at_xy(xy):
    '''
    x and y are ints
    x can be any value
    Just returns a color'''
    
    x,y = xy
        
    noiseVal = noise.pnoise3(x/NOISE_DIV_VAL/zoom,y/NOISE_DIV_VAL/zoom,time/NOISE_DIV_VAL, 3)
    
    #print(noiseVal)
    
    if noiseVal < 0:
        greyVal = 0
    else:
        greyVal = round(noiseVal*255)
    
    #return (random.randint(0,255),) * 3
    return (greyVal,) * 3

worldX = 0
worldY = 40
time = 0
zoom = 0.5

def tick():
    global worldX, worldY
    
    #print(worldX,worldY)
    
    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_UP]:
        worldY += 1
    if keys[pygame.K_DOWN]:
        worldY -= 1
    if keys[pygame.K_LEFT]:
        worldX -= 1
    if keys[pygame.K_RIGHT]:
        worldX += 1
    
def draw_all(surface):
    global worldX, worldY
    
    for drawX in range(0, WIDTH, TILE_WIDTH):
        for drawY in range(0, HEIGHT, TILE_WIDTH):
            worldPosition = (worldX + drawX//TILE_WIDTH, worldY + (HEIGHT//TILE_WIDTH - drawY//TILE_WIDTH))
            color = block_at_xy(worldPosition)
            #pygame.draw.circle(surface, color, (drawX,drawY), TILE_WIDTH//2)
            pygame.draw.rect(surface, color, pygame.Rect(drawX,drawY,TILE_WIDTH,TILE_WIDTH))
    
    
    
if __name__ == '__main__':
    
    WIDTH = 600
    HEIGHT = 600
    TILE_WIDTH = 5#//zoom # round(10/(NOISE_DIV_VAL/30))
    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                            
        screen.fill((0,0,0))
        tick()
        draw_all(screen)
        pygame.display.flip()
        time += 0.1
        clock.tick(300)