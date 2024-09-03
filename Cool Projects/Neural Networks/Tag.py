# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 07:30:19 2021

@author: batte
"""

import pygame
import sys
import math
import random
import numpy as np


def average_genomes(g1,g2):
    newGenome = []
    for i in range(len(g1)):
        newGenome.append((g1[i] + g2[i])/2)
    return newGenome


class Grid:
    
    def __init__(self,width,height,surface):
        self.taggers = []
        self.tagee = None
        self.width, self.height = width,height
        self.surface = surface
        self.currentSimLen = 0
        
        for i in range(TAGGERCOUNT):
            newTagger = Tagger(20,20,,self)
            self.taggers.append()

    def tick(self):
        self.currentSimLen += 1
class Point:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def distance(self,other):
        return (self.x - other.x)**2 + (self.y - other.y)**2

class Tagger(Point):
    
    def __init__(self,x,y,genome,grid):
        Point.__init__(self,x,y)
        self.genome,self.grid = genome,grid
        #genome is 4 numbers, each -1 to 1
        
    def fitness(self):
        return self.distance(self.grid.tagee)
        
    def draw(self,surface):
        r = round((self.genome[0] + self.genome[1] + 2)*63)
        g = round((self.genome[1] + self.genome[2] + 2)*63)
        b = round((self.genome[2] + self.genome[3] + 2)*63)
        
        pygame.draw.circle(surface,(r,g,b),(self.x,self.y),2)
        
    def update(self):
        xToTagee = self.grid.tagee.x - self.x
        yToTagee = self.grid.tagee.y - self.y
        # xToCenter =  self.grid.width//2-self.x
        # yToCenter =  self.grid.height//2-self.y
        xPoints = 0    #if negative, move left, positive, right
        yPoints = 0    #if negative, move up, positive, down
        
        #neural network time!
        
        xPoints += self.genome[0] * xToTagee
        yPoints += self.genome[1] * xToTagee
        xPoints += self.genome[2] * yToTagee
        yPoints += self.genome[3] * yToTagee
        
        if xPoints > 0:
            self.x += 1
        else:
            self.x += -1
        self.x = self.x % self.grid.width
            
        if yPoints > 0:
            self.y += 1
        else:
            self.y += -1
        self.y = self.y % self.grid.height
        
class Tagee(Point):
    
    def __init__(self,x,y,grid):
        Point.__init__(self,x,y)
        self.grid = grid
        
    def draw(self,surface):
        pygame.draw.circle(surface,(0,255,0),(self.x,self.y),4)
        
    def update(self):
        playerControls = False
        
        if playerControls:
            mx,my = pygame.mouse.get_pos()
            
            if mx > self.x:
                self.x += 1
            else:
                self.x += -1
                
            if my > self.y:
                self.y += 1
            else: 
                self.y += -1
        else:
            self.x += random.randint(-1,1)
            self.y += random.randint(-1,1)
            
            self.x = self.x % self.grid.width
            self.y = self.y % self.grid.height
        
        
TAGGERCOUNT = 20
GAMELENGTH = 1000

pygame.init()
WIDTH,HEIGHT = 600,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()    

gameGrid = Grid(WIDTH,HEIGHT,screen)

while True:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        
           
    screen.fill((0,0,0))
    update_all()
    pygame.display.flip()
    clock.tick(20)