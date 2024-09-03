# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 09:04:37 2022

@author: batte
"""

#square packing

import random
import pygame
import sys

class Square:
    
    def __init__(self,x,y,sideLen,):
        self.x = x
        self.y = y
        self.sideLen = sideLen
        
    def overlap(self,other):
        #is the right side to the left of other's left side?
        if self.x + self.sideLen < other.x:
            return False
        #is the bottom side above the top of the other?
        if self.y + self.sideLen < other.y:
            return False
        #is other's right side to the left of our left side?
        if other.x + other.sideLen < self.x:
            return False
        #is other's bottom side above our top side?
        if other.y + other.sideLen < self.y:
            return False
        #I guess we're overlapping
        return True
    
    def draw(self,surface): 
        pygame.draw.rect(surface,(255,255,255),pygame.Rect(self.x,self.y,self.sideLen,self.sideLen),1)

class Holder:
    
    def __init__(self,width,height,surface):
        self.width = width
        self.height = height
        self.surface = surface
        self.allSquares = []
        
    def try_new_square(self):
        newSquare = Square(random.randint(0,self.width),random.randint(0,self.height),random.randint(1,100))
        if newSquare.x + newSquare.sideLen > self.width or newSquare.y + newSquare.sideLen > self.height:
            return False
        for otherSquare in self.allSquares:
            if newSquare.overlap(otherSquare):
                return False
            
        self.allSquares.append(newSquare)
        return True
    
    def try_pack_square(self):
        x,y = random.randint(0,self.width),random.randint(0,self.height)
        side = 1
        
        newSquare = Square(x,y,side)
        
        if newSquare.x + newSquare.sideLen > self.width or newSquare.y + newSquare.sideLen > self.height:
            return False
        for otherSquare in self.allSquares:
            if newSquare.overlap(otherSquare):
                return False
            
        side += 1
        
        while True:
            newSquare = Square(x,y,side)
        
            if newSquare.x + newSquare.sideLen > self.width or newSquare.y + newSquare.sideLen > self.height:
                self.allSquares.append(newSquare)
                return True
            for otherSquare in self.allSquares:
                if newSquare.overlap(otherSquare):
                    self.allSquares.append(newSquare)
                    return True
                
            side += 1
        
    def update(self):
        while not self.try_pack_square():
            pass
    
    def draw(self):
        for square in self.allSquares:
            square.draw(self.surface)
        
        
WIDTH = 500
HEIGHT = 500

squareHolder = Holder(WIDTH,HEIGHT,0)

# for x in range(1,10000):
#     squareHolder.try_new_square()

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

squareHolder.surface = screen

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((0,0,0))

    squareHolder.update()
    squareHolder.draw()
    pygame.display.flip()
    clock.tick(50)