# -*- coding: utf-8 -*-
"""
Created on Sun May 23 09:11:29 2021

@author: batte
"""

import math
import pygame
import random
import sys

class Point(object):
    
    def __init__(self,x,y):
        self.x, self.y = x,y
        
    def get_pos(self):
        return (self.x,self.y)
    
    def distance(self,other):
        mx, my = self.get_pos()
        ox, oy = other.get_pos()
        return math.sqrt((mx - ox)**2 + (my-oy)**2)
    
    def closest_point(self, listOfPoints):
        leastDistance = 1000000
        choice = None
        
        for point in listOfPoints:
            dist = self.distance(point)
            
            if dist < leastDistance:
                leastDistance = dist
                choice = point
                
        return choice
                
    
class World(object):
    
    def __init__(self):
        self.characters = []
        self.objects = []
        
    def add_character(self,newChar):
        self.characters.append(newChar)
        
    def add_object(self,newObj):
        self.objects.append(newObj)
        
    def get_characters(self):
        return self.characters
    
    def get_objects(self):
        return self.objects
    
    def update(self):
        for char in self.characters:
            char.update()
            
    def draw(self,surface):
        for obj in self.objects:
            obj.draw(surface)
            
        for char in self.characters:
            char.draw(surface)
    
class Object(Point):
    
    def __init__(self,x,y,health,master):
        self.x, self.y = x,y
        self.maxHealth = health
        self.health = health
        self.master = master
        self.master.add_object(self)
        
    def get_health(self):
        return self.health
    
    def damage(self, dmg):
        self.health -= dmg
        self.health = max([0,self.health])
        
    def update(self):
        pass
    
    def draw(self,surface):
        width,height = 30, 30
        pygame.draw.rect(surface, (255,round(255*self.health/self.maxHealth),0),   \
    pygame.Rect(self.x - width//2,self.y - height,width,height))
    
class Character(Point):
    
    def __init__(self,x,y,stats,master):
        '''
        stats= tuple containing (hp,dps,speed,attackDistance)
        '''
        self.time = random.randint(-10,10)
        self.x, self.y = x,y
        self.maxHealth,self.dph,self.speed,self.attDist = stats
        self.health = stats[0]
        self.target = None
        self.master = master
        self.master.add_character(self)
        self.state = 'travel'
        
    def update(self):
        self.time += 1
        
        self.health -= 0.05
        
        if self.health < 0:
            self.health = 0
            self.state = 'dead'
            self.target = None
        
        if self.state == 'dead':
            return None
        
        if self.state == 'idle':
            self.y += round(math.sin(self.time /5) * 1)
            self.x += random.randint(-1,1)
            return None
           
        if self.target != None and self.target.get_health() == 0:
            self.target = None
        
        if self.target == None:
            possible_targets = [ob for ob in self.master.get_objects() 
                                if ob.get_health() > 0]
            
            # possible_targets = [ch for ch in self.master.get_characters()]

            
            if len(possible_targets) == 0:
                self.state = 'idle'
                return None
            
            self.target = self.closest_point(possible_targets)
            self.state = 'travel'
            
        distToTarget = self.distance(self.target) - self.attDist
        
        if distToTarget > self.attDist:
            stepFraction = min(self.speed/distToTarget,1)
            xChange, yChange = self.target.x - self.x, self.target.y-self.y
            self.x += xChange*stepFraction
            self.y += yChange*stepFraction
            
            self.y += round(math.sin(self.time /5) * 2)
            
            self.x = round(self.x)
            self.y = round(self.y)
        else:
            self.state = 'attack'
            self.target.damage(self.dph)
            
    def draw(self,surface):
        width,height = 10, 20
        pygame.draw.rect(surface, 
            (0,round(255 * self.health/self.maxHealth),round(255 - 255 * self.health/self.maxHealth)),   \
            pygame.Rect(self.x - width//2,self.y - height,width,height))
        if self.target != None:
            lineColor = tuple([random.randint(100,255) for i in range(3)]) \
                if self.state == 'attack' else (50,50,50)
            pygame.draw.line(surface, lineColor,self.get_pos(),
                         self.target.get_pos())
        
        
     
WIDTH,HEIGHT = 1000,700
            
STATS = (100,1,2,10) #(hp,dps,speed,attackDistance)
OBHEALTH = 300

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

world = World()

for i in range(50):
    ob = Object(
        random.randint(0,WIDTH),random.randint(0,HEIGHT),OBHEALTH,world)
    ch = Character(
        random.randint(0,WIDTH),random.randint(0,HEIGHT),STATS,world)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                        
    screen.fill((0,0,0))
    
    world.update()
    world.draw(screen)
    
    pygame.display.flip()
    clock.tick(30)