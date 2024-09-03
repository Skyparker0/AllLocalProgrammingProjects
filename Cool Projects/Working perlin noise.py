# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 15:26:03 2020

@author: batte
"""

import noise
import numpy as np
import pygame
import sys

#count = {0:0,1:0}



# for x in np.arange(2,size,0.1):
#     for y in np.arange(2,size,0.1):
#         count[np.floor(noise.pnoise2(x,y) + 1)] += 1
    

def pickFromPalette(n, palette):
    '''
    n = number from zero to less than one
    returns a color from the palette'''
    if not 0 <= n < 1:
        raise ValueError("n must be between 0 and less than 1")
    numColors = len(palette)
    n *= numColors
    return palette[int(np.floor(n))]
    
def nGrid(width,height,startX,startY,z,step):
    grid = np.zeros((width,height))
    
    gridX = 0
    gridY = 0
    
    for x in np.arange(startX,startX + width * step, step):
        gridY = 0
        for y in np.arange(startY,startY + height * step, step):
            try:
                grid[gridX,gridY] = noise.pnoise3(x, y, z, 3)       ############NOISE################
            except IndexError:
                pass   # Probably should figure out why it happens
            gridY += 1
        gridX += 1
        
    return grid        


pool_bottom = ["008CEE","0079C4","034EA9","033A95","0465C0","0296D2","B5F5EF"]

def renderGrid(grid, penSize, surface):
    width, height = grid.shape[0], grid.shape[1]
    
    surfaceWidth, surfaceHeight = surface.get_size()
    
    for x in range(width):
        for y in range(height):
            value = grid[x,y]
            value = (value + 1)/2   #Between 0-1
            value **= 1
            pygame.draw.circle(surface, [round((value + 1)/2 * 255)] * 3,  \
                               #COLOR
                               #pygame.Color("#" + pickFromPalette(value,pool_bottom))
                               #[20,20,round(0.2 * round((value + 1)/2/0.2) * 255)]
                               #[0,0,round(0.1 * round((value + 1)/2/0.1) * 255)]
                               #[round(np.floor(value + 1) * 255)] * 3
                               # [round((value + 1)/2 * 255)] * 3)
                               (penSize * (1 + 2 * x), penSize * (1 + 2 * y)), penSize)
        
pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()    
 
penSize = 3
zoom = 0.2

x = 1
y = 1
z = 1

sineChange = 0
  
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button == 5:
        #         cameraDist = min(cameraDist + 0.2, 5)

        #     elif event.button == 4:
        #         cameraDist = max(cameraDist - 0.2, 0.4)
                         
    screen.fill((0,0,0))
    
    sineChange += 0.1
    
    x += 0
    y += 0
    z += 0.05 #np.sin(sineChange)/10   +    np.cos(sineChange)/10
    
    grid = nGrid(int(screen.get_width()/(2*penSize)),int(screen.get_height()/(2*penSize)),x,y,z,zoom/penSize)
    
    renderGrid(grid, penSize, screen)
    
    pygame.display.flip()
    clock.tick(10)