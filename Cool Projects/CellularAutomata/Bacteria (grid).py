# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 12:48:25 2021

@author: batte
"""

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

class Bacteria:
    
    def __init__(self,x,y,gene,parent):
        self.x,self.y = x,y
        self.color = (255,255,255)
        self.gene = gene
        self.parent = parent
        self.energy = 20
        self.age = 0
        
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
 
allBac = []
for x in range(1000):
    newBac = Bacteria(random.randint(0,600),random.randint(0,600), "0000",None)
    allBac.append(newBac)

def update_all():
    for bac in allBac:
        bac.update()
    
    for bac in allBac:
        bac.draw(screen)

while True:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        
           
    screen.fill((0,0,0))
    update_all()
    pygame.display.flip()
    clock.tick(20)