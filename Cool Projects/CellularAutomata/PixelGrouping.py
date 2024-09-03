# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 11:54:24 2022

@author: batte
"""

#PixelGrouping

import numpy as np
import pygame
import sys
import random
import time
    

class Grid:
    #A grouping of pixels, held as a numpy array
    def __init__(self,width,height,drawSize):
        self.array = np.array([[0]*(width//drawSize)]*(height//drawSize))
        self.width = width//drawSize
        self.height = height//drawSize
        self.drawSize = drawSize
    
        self.coordOrder = []
        for x in range(self.width):
            for y in range(self.height):
                self.coordOrder.append((x,y))
    
        random.shuffle(self.coordOrder)
        
    def get(self,x,y):
        return self.array[x,y]
    
    def put(self,x,y,val):
        self.array[x,y] = val
    
    def neighbors(self,x,y):
        totNeighbors = 0
        
        for checkX in range(max(0,x-1),min(self.width,x+2)):
            for checkY in range(max(0,y-1),min(self.height,y+2)):
                if checkX == x and checkY == y:
                    continue
                if self.get(checkX,checkY) == 1:
                    totNeighbors += 1
                    
        return totNeighbors
    
    def update(self):

        ignores = []
        for coord in self.coordOrder:
            x,y = coord
            if self.get(x,y) == 0 or coord in ignores:
                continue
            
            #check neighbors' neighbors
            
            self.put(x,y,0) # so it doesn't count itself
            
            best,chosenOnes = 0,[]
            
            for checkX in range(max(0,x-1),min(self.width,x+2)):
                for checkY in range(max(0,y-1),min(self.height,y+2)):
                    if (x== checkX and y== checkY) or self.get(checkX,checkY) == 1:
                        continue
                    numNeighbors = self.neighbors(checkX,checkY)
                    if numNeighbors == best:
                        chosenOnes.append((checkX,checkY))
                    elif numNeighbors > best:
                        chosenOnes = [(checkX,checkY)]
                        best = numNeighbors
                        
                        
            #Randomness added so blobs of pixels don't sit around
            if (best >= self.neighbors(x,y) or random.random() < 0.1) \
                    and chosenOnes:
                chosen = random.choice(chosenOnes)
                self.put(x,y,0)
                self.put(chosen[0],chosen[1],1)
                ignores.append((chosen[0],chosen[1]))
            else:
                self.put(x,y,1)
    
    def draw(self,surface):
        for x in range(self.width):
            for y in range(self.height):
                pixVal = self.get(x,y)
                color = [pixVal * 255]*3
                pygame.draw.rect(surface,color,pygame.Rect(x*self.drawSize,
                                                            y*self.drawSize,
                                                            self.drawSize,
                                                            self.drawSize))
    
    
    
WIDTH,HEIGHT = 500,500
drawSize = 5

pixelGrid = Grid(WIDTH,HEIGHT,drawSize)

for i in range(200):
    pixelGrid.put(random.randint(0,pixelGrid.width-1),
                  random.randint(0,pixelGrid.height-1),
                  1
                  )

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((0,0,0))
    
    # pixelGrid.put(50+random.randint(-5,5),50+random.randint(-5,5),1)
    pixelGrid.update()
    
    pixelGrid.draw(screen)
    pygame.display.flip()
    
    clock.tick(10)