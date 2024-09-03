# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 08:02:25 2021

@author: batte
"""

import pygame
import sys

color = (110,70,30)

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                        
    screen.fill((0,0,0))
    pygame.draw.rect(screen,color, pygame.Rect(0,0,500,500))
    pygame.display.flip()
    clock.tick(30)