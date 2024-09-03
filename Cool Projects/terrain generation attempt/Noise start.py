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

def height_at_x(x):
    #just pulls a perlin noise value
    return noise.pnoise1(x/NOISE_DIV_VAL,3)


def block_at_xy(xy):
    '''
    x and y are ints
    x can be any value
    y must be >= 0 (should be from 0-100 that there is anything interesting)
    returns 0=lava, 1=stone, 2=dirt, 3=grass, 4=water, 5=sky, 6=space
    (more added) 7 = ore'''
    
    x,y = xy
    
    height = round(height_at_x(x) * 10)
    
    if y < 0 + height/3:
        if noise.pnoise2(x/NOISE_DIV_VAL,y/NOISE_DIV_VAL) < -0.15:
            return 10
        return 0
    elif  y < 30 + height/2:
        if noise.pnoise2(x/NOISE_DIV_VAL,y/NOISE_DIV_VAL) < -0.2:
            return 7
        return 1
    elif  y < 40 + height:
        if noise.pnoise2(x/NOISE_DIV_VAL,y/NOISE_DIV_VAL) < -0.25:
            return 8
        return 2
    elif y < 42 + height:
        if noise.pnoise2(x/NOISE_DIV_VAL,y/NOISE_DIV_VAL) < -0.3:
            return 9
        return 3
    elif y < 45:# and height <=0:
        return 4                            #strange water
    elif y < 100:
        return 5
    else:
        return 6
        
    
def block_color(blockNum):
    '''0=lava, 1=stone, 2=dirt, 3=grass, 4=water, 5=sky, 6=space
    (more added) 7 = uranium, 8=dirt-uranium, 9 = grass-uranium, 10=lava-uranium'''
    color = [(200,40,0), 
            (70,70,80), 
            (60,34,20), 
            (20,80,20), 
            (30,30,130), 
            (200,200,255), 
            (40,0,40), 
            (0,255,0),
            (100,100,150),
            (30,40,30),
            (180,20,20)][blockNum]
    
    return color
    

worldX = 0
worldY = 40

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
            color = block_color(block_at_xy(worldPosition))
            #pygame.draw.circle(surface, color, (drawX,drawY), TILE_WIDTH//2)
            pygame.draw.rect(surface, color, pygame.Rect(drawX,drawY,TILE_WIDTH,TILE_WIDTH))
    
    
    
if __name__ == '__main__':
    
    WIDTH = 600
    HEIGHT = 600
    TILE_WIDTH = round(10/(NOISE_DIV_VAL/30))
    
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
        clock.tick(300)