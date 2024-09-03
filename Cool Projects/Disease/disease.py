# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 16:33:25 2021

@author: batte
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 08:05:12 2021

@author: batte
"""

import numpy as np
import sys
import pygame
import math
import random

class Point:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def get_pos(self):
        return (self.x,self.y)
    
    def set_pos(self,x,y):
        self.x,self.y = x,y
        
    def move(self,deltaX,deltaY):
        self.x += deltaX
        self.y += deltaY
        
    def distance(self,other):
        return math.sqrt((self.x - other.x)**2+(self.y-other.y)**2)
        
    
class Pawn(Point):
    
    def __init__(self,x,y,infected,master):
        Point.__init__(self,x,y)
        self.infected = infected
        self.master = master
        self.tile = 0
        self.direction = random.randint(0,360)
        
    def update(self,reverse = False):
        distance = self.master.walkSpeed
        turnSpeed = self.master.turnSpeed
        
        x,y = self.get_pos()
        tile = x // self.master.tileSize + y // self.master.tileSize * math.ceil(self.master.width/self.master.tileSize)
            
        if self.tile in self.master.walls \
          or x <= 0 or x >= self.master.width \
          or y <= 0 or y >= self.master.height:
            self.move(math.cos(math.radians(self.direction))*distance*-1,
                math.sin(math.radians(self.direction))*distance*-1)
            self.direction += 180
        else:
            self.direction += random.randint(-turnSpeed,turnSpeed)
            self.move(math.cos(math.radians(self.direction))*distance,
                  math.sin(math.radians(self.direction))*distance)
          
        x,y = self.get_pos()
        self.set_pos(constrain(x,0,self.master.width),constrain(y,0,self.master.height))
        
    def try_infect(self):
        if self.infected and self.tile not in self.master.walls:
            for other in self.master.tiles[self.tile]:
                if random.random() < self.master.spreadChance:
                    other.infected = True
                    # other.direction = self.direction

    def draw(self,surface):
        color = (10,10,10)
        
        if self.infected:
            color = (255,0,0)
            # for other in self.master.tiles[self.tile]:
            #     pygame.draw.line(surface,color,self.get_pos(),other.get_pos(),1)
        else:
            color = (0,255,0)
        
        pygame.draw.circle(surface, color,[int(i) for i in self.get_pos()],4)
        
        
        
        
class Simulation:
    
    def __init__(self,width,height,numPawns,startInfected,spreadChance,tileSize, turnSpeed, walkSpeed):
        self.width, self.height, self.numPawns, self.startInfected, self.spreadChance,self.tileSize,self.turnSpeed,self.walkSpeed = width,height,numPawns,startInfected,spreadChance,tileSize,turnSpeed,walkSpeed
        
        self.walls = [tile for tile in range(math.ceil(self.width/self.tileSize) * math.ceil(self.height/self.tileSize + 1) + 1) if random.random() < 0.4]
        
        self.pawns = []
        for i in range(numPawns):
            while True:
                newPawn = Pawn(random.randint(0,width),
                               random.randint(0,width),
                               i < startInfected,
                               self)
                x,y = newPawn.get_pos()
                
                tile = x // self.tileSize + y // self.tileSize * math.ceil(self.width/self.tileSize)
                
                if tile not in self.walls:
                    break
                
            self.pawns.append(newPawn)
            
        self.clear_tiles()
            
    def clear_tiles(self):
        self.tiles = {i:[] for i in range(
            math.ceil(self.width/self.tileSize) * math.ceil(self.height/self.tileSize + 1) + 1
            )}
        
        for pawn in self.pawns:
            x,y = pawn.get_pos()
            
            tile = x // self.tileSize + y // self.tileSize * math.ceil(self.width/self.tileSize)
            pawn.tile = tile
            self.tiles[tile].append(pawn)
            
    def update(self,surface):
        for pawn in self.pawns:
            pawn.update()
            
        self.clear_tiles()
           
        for pawn in self.pawns:
            pawn.try_infect() 
           
        for x in range(math.ceil(self.width/self.tileSize)+ 1):
            for y in range(math.ceil(self.height/self.tileSize) + 1):
                tile = x + y * math.ceil(self.width/self.tileSize)
                
                if tile in self.walls:
                    color = (0,0,0)
                else:
                    color = (100,100,100)
                    
                pygame.draw.rect(surface, color, 
                        pygame.Rect(x*self.tileSize + 1, 
                                    y*self.tileSize + 1, 
                                    self.tileSize -2,self.tileSize -2))
            
        for pawn in self.pawns:
            pawn.draw(surface)
        
        
                        
##Utility functions##

def constrain(var, minimum,maximum):
    return maximum if var > maximum else minimum if var < minimum else var

##
        
WIDTH, HEIGHT = 700,700

POPULATION = 1000
NUMINFECTED = 2
TRANSMISSIONRATE = (1) /20 #/20 because 20 fps
TILESIZE = 50
TURNSPEED = 20
WALKSPEED = 2




pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()    
   

sim = Simulation(WIDTH, HEIGHT,POPULATION,NUMINFECTED,TRANSMISSIONRATE,TILESIZE,TURNSPEED,WALKSPEED)


while True:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

    sim.update(screen)
    pygame.display.flip()
    screen.fill((0,0,0))
    clock.tick(20)