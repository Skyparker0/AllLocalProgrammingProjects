# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:46:48 2020

@author: batte
"""

##FALLING SAND

import numpy as np
import random
import pygame
import sys
class sandbox:
    
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.sandArray = np.array([[0 for x in range(width)] for i in range(height)])
        
    def __getitem__(self, key):
        return self.get_state(key)
        
    def get_state(self, key):
        if (0 > key[0] or key[0] > self.width-1) or (0 > key[1] or key[1] > self.height-1):
            return -1
        return self.sandArray[key[::-1]]

    def add_sand(self,x,y):
        try:
            self.sandArray[x,y] = 1
        except:
            pass
        
    def del_sand(self,x,y):
        try:
            self.sandArray[x,y] = 0
        except:
            pass
        
    def move_from(self,x1,y1,x2,y2):
        if self[x1,y1] == 1:
            self.del_sand(x1,y1)
            self.add_sand(x2,y2)
        
    def tick_cell(self,x,y):
        if self[x,y] != 1:
            return None
        
        if self[x,y+1] == 0:
            self.move_from(x,y,x,y+2)
        # elif 0 in (self[x-1,y+1],self[x+1,y+1]):
            
        #     if random.randint(0,1) == 1:
        #         if self[x-1,y+1] == 0:
        #             self.move_from(x, y, x-1, y+1)
        #         elif self[x+1,y+1] == 0:
        #             self.move_from(x, y, x+1, y+1)
        #     else:
        #         if self[x+1,y+1] == 0:
        #             self.move_from(x, y, x+1, y+1)
        #         elif self[x-1,y+1] == 0:
        #             self.move_from(x, y, x-1, y+1)
                    
    def tick(self,screen):
        for x in range(self.width):
            for y in range(self.height):
                self.tick_cell(x,y)
                
        for x in range(self.width):
            for y in range(self.height):
                newStatus = self[x,y]
                colors = [(100,100,100),(255,255,255),(255,255,0)]
                pygame.draw.circle(screen,colors[newStatus+1],tuple([1+i*4 for i in [x,y]]),4)
            
            
            
WIDTH = 100
HEIGHT = 100            
pygame.init()
screen = pygame.display.set_mode((WIDTH * 4, HEIGHT * 4))
clock = pygame.time.Clock()

def simulate(screen, width, height):
    sb = sandbox(width,height)
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        
                        pos = tuple((round(i/4) + 1 for i in pygame.mouse.get_pos()))
                        sb.add_sand(pos[0],pos[1])
                        print(sb.get_state(pos))
        
        screen.fill((0, 10, 100))
        
        sb.tick(screen)
        
        pygame.display.flip()
        clock.tick(10)
        

simulate(screen,WIDTH,HEIGHT)