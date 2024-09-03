# -*- coding: utf-8 -*-
"""
Created on Wed May  5 08:20:40 2021

@author: batte
"""

import pygame
import sys
import random

class CircleHolder(object):
    
    def __init__(self):
        self.circles = []
        
    def get(self):
        return self.circles
        
    def add(self, circle):
        self.circles.append(circle)
        
    def take(self,circle):
        self.circles.remove(circle)
        
    def update(self):
        for circle in self.circles:
            circle.update()
            
    def draw(self, surface):
        for circle in self.circles:
            circle.draw(surface)
            
class Circle(object):
    #self.radius = min(distancesToAllOthercircles)/2
    def __init__(self,position,velocity,master):
        self.position = list(position)
        self.velocity = list(velocity)
        self.radius = 1
        self.master = master
        self.maxYet = False
        self.lifeTime = 0
        
        self.color = tuple([random.randint(0,255) for i in range(3)])
        
        flag = False
        for other in master.get():
            if self.distance(other) <= other.radius:
                flag = True
        if not flag:
            self.master.add(self)

    def distance(self,other):
        myX, myY = self.position
        otX, otY = other.position
        return ((myX-otX)**2 + (myY-otY)**2)**0.5
        
    def draw(self,surface):
        pygame.draw.circle(surface,self.color,self.position,self.radius)
        
    def unLock(self):
        self.maxYet = False
        if x - self.radius < 0 or x + self.radius > WIDTH or y-self.radius < 0 or y + self.radius > HEIGHT:
            self.maxYet = True
        for other in self.master.get():
                if other == self:
                    continue
                if self.distance(other) <= self.radius + other.radius:
                    self.maxYet = True
        
    def baby(self):
        newCircle = Circle(self.position, (0,0), circles)
        
    def update(self):
        self.lifeTime += 1
        
        if self.lifeTime > self.radius ** 2 + time/10:
            self.master.take(self)
            # if self.radius > 20:
            #     self.baby()
            for other in self.master.get():
                if self.distance(other) <= self.radius + other.radius:
                    other.unLock()
                    
            return None
        
        if self.maxYet:
            return None
        
        self.radius += 1
        
        x,y = self.position
        
        if x - self.radius < 0 or x + self.radius > WIDTH or y-self.radius < 0 or y + self.radius > HEIGHT:
            self.maxYet = True
            return None
        
        for other in self.master.get():
            if other == self:
                continue
            if self.distance(other) < self.radius + other.radius:
                self.maxYet = True
                return None
        
        

WIDTH = 500
HEIGHT = 500

time = 0

circles = CircleHolder()

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    time += 1
    
    screen.fill((0,0,0))
    
    x = random.randint(1,WIDTH-1)
    y = random.randint(1,HEIGHT-1)
    xVel = random.randint(-2,2)
    yVel = random.randint(-2,2)
    
    newCircle = Circle((x,y), (xVel,yVel), circles)

    circles.update()
    circles.draw(screen)
    pygame.display.flip()
    clock.tick(30)