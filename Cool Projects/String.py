# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 16:49:34 2021

@author: batte
"""

import random
import pygame
import sys
import numpy as np


class Point:
    def __init__(self,position, locked):
        self.position = np.array(position)
        self.previousPosition = position
        self.locked = locked
        
    def draw(self,surface):
        pygame.draw.circle(surface,(255,0,0),self.position.astype(int),10)
        
        
class Stick:
    
    def __init__(self,point1,point2):
        self.point1 = point1
        self.point2 = point2
        self.length = np.sqrt((point1.position - point2.position)**2)
        
    def draw(self,surface):
        pygame.draw.line(surface,(200,200,200),self.point1.position.astype(int),
                         self.point2.position.astype(int),2)


def norm(v):
    return v / (np.sqrt(np.sum(v**2)) + 0.1)

def simulate():
    if random.random() < 0.05:
        points.append(
            Point(
            np.array([random.randint(0,WIDTH),random.randint(0,HEIGHT)]),
            random.choice([False]))
            )
        if len(points) > 1: 
            sticks.append(Stick(points[0],points[-1]))
    
    for point in points:
        
        if not point.locked:
            newLastPos = np.array(point.position[:])
            point.position += point.position - point.previousPosition
            point.position[1] += GRAVITY
            if point.position[1] > HEIGHT:
                point.position[1] += -2*GRAVITY

            point.previousPosition = newLastPos

        

    for i in range(3):
        for stick in sticks:
            stickCenter = (stick.point1.position + stick.point2.position)/2
            stickDir = norm(stick.point1.position - stick.point2.position)
            
            if not stick.point1.locked:
                # pullDir = norm(-stick.point1.position + (stickCenter + stickDir * stick.length/2))
                # stick.point1.position = stick.point1.position*1.0 + pullDir * 1
                stick.point1.position = stickCenter + stickDir * (stick.length/2)
            if not stick.point2.locked:
                # pullDir = norm(-stick.point2.position + (stickCenter + stickDir * stick.length/2))
                # stick.point2.position = stick.point2.position*1.0 + pullDir * 1
                stick.point2.position = stickCenter - stickDir * (stick.length/2)
            
            
    for point in points:
        point.draw(screen)
    for stick in sticks:
        stick.draw(screen)
        
GRAVITY = 1
WIDTH, HEIGHT = 500,500

points = [Point((250,250),True)]
sticks = []

      
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()    

while True:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     if event.button == 1:
                #         x,y = pygame.mouse.get_pos()
                #         b.turn(y//WIDTH, x//WIDTH)
                        
    
    simulate()
    pygame.display.flip()
    screen.fill((0,0,0))
    clock.tick(30)