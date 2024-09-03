# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 08:16:24 2021

@author: batte
"""

import pygame
import sys
import noise

WIDTH = 500
HEIGHT = 500
time = 0

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def draw(surface):
    TILE_SIZE = 5
    for x in range(WIDTH//TILE_SIZE):
        for y in range(HEIGHT//TILE_SIZE):
            noiseVal = noise.pnoise3(x/20, y/20, time)
            pygame.draw.rect(surface, ((noiseVal + 1)/2 * 255,)*3, pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                        
    screen.fill((0,0,0))
    draw(screen)
    pygame.display.flip()
    time += 1/30
    clock.tick(30)