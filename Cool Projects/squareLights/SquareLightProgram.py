# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 12:57:55 2021

@author: batte
"""

import numpy as np
import pygame
import sys

class World(object):
    
    def __init__(self,grid):
        '''
        grid; 2d np array with numbers 0-1 (brightness) or -1 (wall)'''
        self.originalGrid = grid.copy()
        self.editedGrid = grid.copy()
        self.width, self.height = grid.shape
        self.update()
        
    def __str__(self):
        output = ""
        for y in range(self.height):
            for x in range(self.width):
                output += str(round(self.edited_get(x,y)*10)/10) + " "
            output += "\n"
        return output
            
    def original_set(self,x,y,new):
        if not (-1 < x < self.width and -1 < y < self.height):
            return None
        self.originalGrid[x,y] = new
        self.update()
        
    def edited_set(self,x,y,new):
        if not (-1 < x < self.width and -1 < y < self.height):
            return None
        self.editedGrid[x,y] = new
        
    def original_get(self,x,y):
        if not (-1 < x < self.width and -1 < y < self.height):
            return None
        return self.originalGrid[x,y]
        
    def edited_get(self,x,y):
        if not (-1 < x < self.width and -1 < y < self.height):
            return None
        return self.editedGrid[x,y]
    
    def reveal(self,x,y,value):
        if not (-1 < x < self.width and -1 < y < self.height):
            return None
        
        myValue = self.edited_get(x,y)
        
        if myValue == -1:    #don't update walls
            return None
        # update that tile's value if need be
        if value > myValue:
            self.edited_set(x,y,value)
        elif value != 0:    # if this wasn't the start of the chain, don't update anything
            #self.edited_set(x,y,max(0.9, value + myValue))
            return None
            
        myValue = self.edited_get(x,y) #value may have been changed, get again
        
        #now update all near tiles, if brightness not too low
        
        if myValue < 0.1:
            return None
        
        for xChange in range(-1, 2):
            for yChange in range(-1,2):
                multiplier = 0.8
                if abs(xChange) == abs(yChange) == 1:
                    multiplier *= 0.9#1/1.41
                self.reveal(x + xChange, y + yChange, myValue * multiplier)
        
        
    
    def update(self):
        self.editedGrid = self.originalGrid.copy()
        for x in range(self.width):
            for y in range(self.height):
                if self.original_get(x,y) > 0:
                    self.reveal(x,y, 0)
                    
    def mouse_input(self, pos, click):
        tileX = pos[0]//TILE_WIDTH
        tileY = pos[1]//TILE_WIDTH
        
        #print(pos, (tileX,tileY))
        
        if click == "rightClick":
            self.original_set(tileX,tileY,-1)
            #wall
        elif click == "leftClick":
            self.original_set(tileX,tileY,1)
            #light
                    
    def draw(self,surface):
        for tileY in range(self.height):
            drawY = tileY * TILE_WIDTH
            for tileX in range(self.width):
                drawX = tileX * TILE_WIDTH
                
                tileValue = self.edited_get(tileX,tileY)
                
                color = (0,0,0)
                if tileValue >= 0:
                    color = (round(tileValue*255),) * 3
                else:
                    color = (0,100,0)
                    
                pygame.draw.rect(surface, color, pygame.Rect(drawX,drawY,TILE_WIDTH,TILE_WIDTH))
                    
                    
                    

# print(w)

WIDTH = 600
HEIGHT = 600
TILE_WIDTH = 20

grid = np.zeros((WIDTH//TILE_WIDTH,HEIGHT//TILE_WIDTH))
grid[WIDTH//2//TILE_WIDTH,HEIGHT//2//TILE_WIDTH] = 1
w = World(grid)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                w.mouse_input(pygame.mouse.get_pos(), "leftClick")
            if event.button in [2,3]:
                w.mouse_input(pygame.mouse.get_pos(), "rightClick")
                        
    screen.fill((0,0,0))
    w.draw(screen)
    pygame.display.flip()
    clock.tick(60)
