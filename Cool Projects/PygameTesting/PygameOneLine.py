# -*- coding: utf-8 -*-
"""
Created on Mon May 10 07:53:20 2021

@author: batte
"""

import pygame
import sys
import math


pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
    
def color(x,y):
    return ((x/500) ** 0.5 * 255, (y/500) ** 0.5 * 255,x/500 * y/500 * 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                        
    screen.fill((0,0,0))
    
    for x in range(500):
        for y in range(500):
            pygame.draw.rect(screen, color(x,y),pygame.Rect(x,y,1,1))
    
    pygame.display.flip()
    clock.tick(1)