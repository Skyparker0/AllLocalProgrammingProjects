# -*- coding: utf-8 -*-
"""
Created on Fri May 28 07:56:25 2021

@author: batte
"""

#Repulsion Circles

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
        return((mx - ox)**2 + (my-oy)**2)**0.5
    
    def normal(self,other):
        mx, my = self.get_pos()
        ox, oy = other.get_pos()
        distFactor = 1/(self.distance(other)+0.01)
        return ((ox-mx)*distFactor,(oy-my)*distFactor)

class CircleHolder:
    
    def __init__(self):
        self.circles = []
        
    def add(self,circle):
        self.circles.append(circle)
        
    def get(self):
        return self.circles
        
    def update(self):
        for circle in self.circles:
            circle.updateVelocity()
        for circle in self.circles:
            circle.updatePos()
            
    def draw(self,surface):
        for circle in self.circles:
            circle.draw(surface)

class RepulsionCircle(Point):
    
    def __init__(self,x,y,radius,master):
        self.x = x
        self.y = y
        
        self.radius = radius
        
        self.master = master
        self.master.add(self)
        
        self.velocity = (0,0)
        
    def get_mass(self):
        return self.radius**2
        
    def updateVelocity(self):
        acceleration = (0,0)
        
        
        for circle in self.master.get():
            if circle is self:
                continue
            
            dist = self.distance(circle)
            direction = self.normal(circle)#tuple_mult(self.normal(circle),-1)
            force = circle.get_mass() / (dist**2 + 0.5) * BIG_G
            forceAcceleration = tuple_mult(direction, force)
            
            acceleration = tuples_add(acceleration,forceAcceleration)
            
            
        self.velocity = tuples_add(self.velocity,acceleration)
        
        self.velocity = tuple_mult(self.velocity,0.99)    #FRICTION
            
    def updatePos(self):
        self.x,self.y = tuples_add((self.x,self.y),self.velocity)

        #Wall rep
        
        mult = -1     #WALL BOUNCE-BACK
        
        if self.x < 0 + self.radius:
            self.x = 1 + self.radius
            self.velocity = tuples_mult(self.velocity,(mult,1))
            
        if self.x > WIDTH - self.radius:
            self.x = WIDTH - self.radius - 1
            self.velocity = tuples_mult(self.velocity,(mult,1))
            
        if self.y < 0 + self.radius:
            self.y = 1 + self.radius
            self.velocity = tuples_mult(self.velocity,(1,mult))
            
        if self.y > HEIGHT - self.radius:
            self.y = HEIGHT - self.radius - 1
            self.velocity = tuples_mult(self.velocity,(1,mult))
        
    
    def draw(self,surface):
        rx,ry = round(self.x),round(self.y)
        pygame.draw.circle(surface,(200,200,200),(rx,ry),self.radius)
    
    
def tuples_add(tuple1,tuple2):
    return tuple(tuple1[i] + tuple2[i] for i in range(len(tuple1)))

def tuples_mult(tuple1,tuple2):
    return tuple(tuple1[i] * tuple2[i] for i in range(len(tuple1)))

def tuple_mult(tup,multiplier):
    return tuple(i * multiplier for i in tup)

WIDTH,HEIGHT = 500,500
BIG_G = -0.5
WALL_FORCE = 100000


pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

allCircles = CircleHolder()

for i in range(50):
    radius = random.randint(5,15)
    x,y = (random.randint(radius,WIDTH-radius), 
        random.randint(radius,HEIGHT-radius))
    newCircle = RepulsionCircle(x,y,radius,allCircles)
   
planetCenter = None
planetEdge = None 
   
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            planetCenter = pygame.mouse.get_pos()
            planetEdge = pygame.mouse.get_pos()
            radius = 0
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            planetEdge = pygame.mouse.get_pos()
            
            newCircle = RepulsionCircle(planetCenter[0],planetCenter[1],\
                                        radius,allCircles)
            
            planetCenter, planetEdge = None,None
                          
            
                        
    screen.fill((0,0,0))
    
    if planetCenter != None:
        planetEdge = pygame.mouse.get_pos()
        radius = round(Point(planetCenter[0],planetCenter[1])\
                .distance(Point(planetEdge[0],planetEdge[1])))
        radius = max(radius,10)
        pygame.draw.circle(screen,(100,100,100),planetCenter,radius)
    
    allCircles.update()
    allCircles.draw(screen)
    
    pygame.display.flip()
    clock.tick(30)