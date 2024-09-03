# -*- coding: utf-8 -*-
"""
Created on Sun May 23 14:20:55 2021

@author: batte
"""


import numpy as np
import pygame
import sys

class Pygame_Array():
    
    def __init__(self,width,height):
        self.array = np.zeros((width,height))
        self.time = 0
        
    def val_to_color(self, value):
        '''Value must be between 0 and 1'''
        return (255,255,255) if value else (0,0,0)
    
    def get_at(self,x,y):
        if x < 0 or x >= self.array.shape[0] or y < 0 or y >= self.array.shape[1]:
            return None
        return self.array[x % self.array.shape[0],y % self.array.shape[1]]
    
    def on_neighbors(self,x,y):
        count = 0
        for pos in [(x, y-1),(x-1,y),(x+1,y),(x,y+1)]:
            count += 1 if self.get_at(pos[0],pos[1]) == True else 0
        return count
        
    
    def set_at(self,x,y,val):
        self.array[x,y] = val
    
    def update(self):
        newArr = self.array.copy()
        for x in range(self.array.shape[0]):
            for y in range(self.array.shape[1]):
                value = True if self.on_neighbors(x,y) in [1,4] else False

                newArr[x,y] = value
                
        self.array = newArr
                
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

arr.set_at(WIDTH//TILE_SIZE//2,HEIGHT//TILE_SIZE//2,True)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                        
    screen.fill((0,0,0))
    
    arr.update()
    arr.draw(screen)
    
    pygame.display.flip()
    clock.tick(5)