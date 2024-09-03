# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 15:08:09 2021

@author: batte
"""

# Cirle_bounce

import numpy as np
import pygame
import sys
import random

class Circle_Holder(object):
    
    def __init__(self, width, height):
        self.circles = []
        self.width = width
        self.height = height
        #####################################################
        for i in range(20):
            self.add_circle([random.randint(20,width-20), random.randint(20,height-20)], \
                            [random.randint(-2,2),random.randint(-2,2)], 10)
            
        
    def get_circles(self):
        return self.circles
        
    def add_circle(self,position, velocity, radius):
        '''Position and velocity are given as 2tuple or 2list'''
        if False:#len(self.get_circles()) > 0:
            for otherCircle in self.get_circles():
                if np.sqrt(sum((position - otherCircle.get_pos()) ** 2)) <=  \
                    radius + otherCircle.get_radius():
                    self.add_circle([random.randint(radius,self.width-radius), 
                                     random.randint(radius,self.height-radius)], 
                                [random.randint(-2,2),random.randint(-2,2)], radius)
                else: 
                    self.circles.append(circle(np.array(position), np.array(velocity), radius, self))
        else: 
            self.circles.append(circle(np.array(position), np.array(velocity), radius, self))
    def tick(self):
        for cir in self.circles:
            cir.collide()
        
        for cir in self.circles:
            cir.update(5)
            
    def drawAll(self, screen):
        for cir in self.circles:
            cir.draw(screen)

class circle(object):
    '''A circle object that can move and collide with other circles'''
    
    def __init__(self, position, velocity, radius, master):
        '''
        position = np array that holds the x,y start coordinate of the circle
        velocity = np array that holds the start velocity of the circle, like a vector
        radius = the radius of the circle
        master = some type of holder class, that holds a bunch of circles'''
        
        self.position = position
        self.velocity = velocity
        self.newVelocity = velocity
        self.radius = radius
        self.master = master
        
        self.touching = None    #debugging purposes
        
    def get_pos(self):
        return self.position
    
    def get_velocity(self):
        return self.velocity.copy()
    
    def get_radius(self):
        return self.radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, (200,200,200), self.position.astype(int), self.radius)
        pygame.draw.line(screen, (255,0,0), self.position.astype(int), \
                         (self.position + self.velocity * 10).astype(int))
        if self.touching != None:
            pygame.draw.line(screen, (0,0,255), self.position.astype(int), \
                             self.touching.get_pos().astype(int))
        
    def collide(self):        
        '''
        for every other circle:
            if touching that circle:
                (simple)
                trade velocities
                (complex)
                get a higher level math education and figure it out
                
        if touching wall:
            flip x vel if side wall, y vel if top/bot wall'''
            
        self.newVelocity = self.velocity
        self.touching = None    #debugging purposes
        
        for other in self.master.get_circles():
            if other is self:
                continue
            if np.sqrt(sum((self.get_pos() - other.get_pos()) ** 2)) <=  \
                self.get_radius() + other.get_radius():
                
                self.newVelocity = other.get_velocity()
                
                self.touching = other
                
        if self.position[0] <= 0 + self.radius \
            or self.position[0] >= self.master.width - self.radius:
                self.newVelocity *= [-1,1]
                
        if self.position[1] <= 0 + self.radius \
            or self.position[1] >= self.master.height - self.radius: 
                self.newVelocity *= [1,-1]
                
    def update(self, precision = 1):
        '''If precision is bigger than one, very small steps are taken'''
        self.velocity = self.newVelocity
        self.position = self.position / 1 + self.velocity / precision    #Deals with float + int
        
        
if __name__ == '__main__':
    
    WIDTH = 600
    HEIGHT = 600
    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    
    holder = Circle_Holder(WIDTH,HEIGHT)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                            
        screen.fill((0,0,0))
        holder.tick()
        holder.drawAll(screen)
        pygame.display.flip()
        clock.tick(300)