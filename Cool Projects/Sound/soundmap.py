# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 07:35:35 2021

@author: batte
"""

import math
import pygame
import sys

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def distance(self,other):
        return math.sqrt((self.x - other.x)**2+(self.y-other.y)**2)

class SoundObject(Point):
    def __init__(self,x,y,sound):
        Point.__init__(self,x,y)
        self.sound = sound
        self.volume = 100
    
class Player(Point):
    def __init__(self,x,y):
        Point.__init__(self,x,y)
        self.direction = 0    # 0^  90>  180v  270<
        
        
        
        
        
        
pygame.init()
screen = pygame.display.set_mode((300,200))
clock = pygame.time.Clock()    

while True:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        
    keys = pygame.key.get_pressed()[-50:-46]
    
    left = keys[3]
    up = keys[0]
    down = keys[1]
    right = keys[2]
    
    width, height = 99,99
    
    if left:
        pygame.draw.rect(screen,(200,200,200),pygame.Rect(0,100,width, height))
    else:
        pygame.draw.rect(screen,(100,100,100),pygame.Rect(0,100,width, height))
    if up:
        pygame.draw.rect(screen,(200,200,200),pygame.Rect(100,0,width, height))
    else:
        pygame.draw.rect(screen,(100,100,100),pygame.Rect(100,0,width, height))
    if down:
        pygame.draw.rect(screen,(200,200,200),pygame.Rect(100,100,width, height))
    else:
        pygame.draw.rect(screen,(100,100,100),pygame.Rect(100,100,width, height))
    if right:
        pygame.draw.rect(screen,(200,200,200),pygame.Rect(200,100,width, height))
    else:
        pygame.draw.rect(screen,(100,100,100),pygame.Rect(200,100,width, height))
        
    pygame.display.flip()
    screen.fill((0,0,0))
    clock.tick(30)