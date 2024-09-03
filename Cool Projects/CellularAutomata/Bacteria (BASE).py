# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 10:56:07 2021

@author: batte
"""

import pygame
import sys
import math
import random
import numpy as np

class Pixel:
    
    def __init__(self,x,y):
        self.x,self.y = x,y
        self.color = (255,255,255)
        
    def get_pos(self):
        return self.x,self.y
    
    def move(self,x,y):
        self.x = (self.x + x) % WIDTH
        self.y = (self.y + y) % HEIGHT
    
    def draw(self,surface,color = None):
        pygame.draw.rect(surface,color if color else self.color,\
                         pygame.Rect(self.x,self.y,1,1))
            
    def update(self):
        self.move(random.randint(-1,1),random.randint(-1,1))


pygame.init()
WIDTH,HEIGHT = 600,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()    
 
pixels = []
for x in range(100):
    newPixel = Pixel(random.randint(0,600),random.randint(0,600))
    pixels.append(newPixel)

def update_all():
    for pixel in pixels:
        pixel.update()
    
    for pixel in pixels:
        pixel.draw(screen)

while True:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        
           
    screen.fill((0,0,0))
    update_all()
    pygame.display.flip()
    clock.tick(20)