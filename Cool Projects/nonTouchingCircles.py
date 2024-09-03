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
        self.radius = 10
        self.master = master
        self.master.add(self)

    def distance(self,other):
        myX, myY = self.position
        otX, otY = other.position
        return ((myX-otX)**2 + (myY-otY)**2)**0.5
        
    def draw(self,surface):
        pygame.draw.circle(surface,(255,255,255),self.position,self.radius)
        
    def update(self):
        x,y = self.position[0], self.position[1]
        minDist = min([self.distance(other) for other in self.master.get() if other is not self]
                      + [self.position[0] * 2,self.position[1] * 2,(WIDTH - self.position[0])*2,(HEIGHT - self.position[1])*2])
        self.radius = max(round(minDist/2),0)
        
        if self.position[0] > WIDTH or self.position[0] < 0:
            self.velocity[0] *= -1
            self.position[0] += self.velocity[0]
            
        if self.position[1] > HEIGHT or self.position[1] < 0:
            self.velocity[1] *= -1
            self.position[1] += self.velocity[1]
            
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        
        
        

WIDTH = 500
HEIGHT = 500

circles = CircleHolder()
for i in range(10):
    x = random.randint(1,WIDTH-1)
    y = random.randint(1,HEIGHT-1)
    xVel = random.randint(-2,2)
    yVel = random.randint(-2,2)
    newCircle = Circle((x,y), (xVel,yVel), circles)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                        
    screen.fill((0,0,0))
    circles.update()
    circles.draw(screen)
    pygame.display.flip()
    clock.tick(30)