# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 18:59:16 2020

@author: batte
"""

import pygame
import random
import sys


class point:
    '''__init__(self, x, y, size, color,speed)
    A single point, most likely other classes will branch off this'''
    
    def __init__(self, x, y):
        '''The point has an x and y value, and a rounded x y value for drawing'''
        self.x = x
        self.y = y
        self.roundx = round(self.x)
        self.roundy = round(self.y)
        
    def pos(self):
        return (self.x, self.y)
    
    def dist(self, other):
        (changeX, changeY) = [other.pos()[i] - self.pos()[i] for i in [0,1]]
        return (changeX**2 + changeY**2)**0.5
    
    def round_XY(self):
        self.roundx = round(self.x)
        self.roundy = round(self.y)
        
    def round_pos(self):
        self.round_XY()
        return (self.roundx,self.roundy)
    
    def draw(self, surface):
        '''robot.draw(surface)
        surface is the pygame surface getting drawn on.
        draws a circle representing the size and cargo'''
        
        self.round_XY()
        drawPos = [round((self.round_pos()[i] - cameraPos[i])//cameraDist)  + 400 for i in range(2)]
        pygame.draw.circle(surface, pygame.Color(100,100,100,a = 10), drawPos, round(20//cameraDist))
        
    def move_closer(self, other, moveDistance, spacing):
        '''robot.move_closer(other, moveDistance, spacing)
        other = target point object
        moveDistance = the ammount the robot moves
        spacing = how much distance is kept between the robot and target
        The robot moves moveDistance pixels torwards or away from other depending on spacing.
        The robot moves itself to get to a position spacing pixels away from other.'''
        dist = self.dist(other)
        goalDist = dist - spacing
        
        if goalDist == 0 or dist == 0:
            # goalDist += 0.0001 
            # dist += 0.0001
            return 'ZeroDiv'
            
        distFraction = goalDist/dist
        xChange, yChange = [(other.pos()[i] - self.pos()[i]) * distFraction for i in [0,1]]
        
        if abs(goalDist) <= moveDistance:
            self.x += xChange
            self.y += yChange
            return self.dist(other),spacing
        
        moveFraction = moveDistance/goalDist
        
        self.x += xChange * moveFraction * (-1 if moveFraction < 0 else 1)
        self.y += yChange * moveFraction * (-1 if moveFraction < 0 else 1)
        


class food(point):
    
    def __init__(self, x, y):
        point.__init__(self, x, y)
        self.hidden = False
        
    def is_touching(self,other,space):
        if self.dist(other) < space:
            self.hidden = True
            return True
        
    def draw(self, surface):
        if not self.hidden:
            self.round_XY()
            drawPos = [round((self.round_pos()[i] - cameraPos[i])//cameraDist)  + 400 for i in range(2)]
            pygame.draw.circle(surface, (255,255,0), drawPos, round(5//cameraDist))
        


def tick(surface):
    global cameraPos
    global cameraDist
    global num_points
    
    cameraPos = points[0].round_pos()
    
    
    surface.fill((0,0,0))
    
    draw_grid(surface)
    
    for x in range(len(points)):
        if x == 0:
            mouseDifferences = [pygame.mouse.get_pos()[i] - 400 for i in range(2)]
            goalPoint = [points[x].round_pos()[i] + mouseDifferences[i] for i in range(2)]
            points[x].move_closer(point(goalPoint[0],goalPoint[1]),0 + points[x].dist(point(goalPoint[0],goalPoint[1]))/30,15)
            cameraPos = points[x].round_pos()
        else:
            points[x].move_closer(points[x-1],10000,15)
            #pygame.draw.line(surface, (100,100,100), points[x].round_pos(), points[x-1].round_pos(),20)
            
        points[x].draw(surface)
        
    for foo in meals:
        if not foo.hidden:
            foo.draw(surface)
            if foo.is_touching(points[0], 30):
                num_points += 1
        
   
def draw_grid(surface):
    for x in range(-10000,10000,1000):
        for y in range(-10000,10000,1000):
            x1,y1 =[round(((x,y)[i] - cameraPos[i])//cameraDist)  + 400 for i in range(2)]
            pygame.draw.line(surface, (100,150,200), (x1,y1+8000//cameraDist), (x1,y1-10000//cameraDist), 5)
            pygame.draw.line(surface, (100,150,200), (x1+8000//cameraDist,y1), (x1-10000//cameraDist,y1), 5)
   
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()    
 
cameraDist = 1

points = []
num_points = 50
meals = []
num_food = 100
   
while True:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 5:
                        cameraDist = min(cameraDist + 0.2, 5)

                    elif event.button == 4:
                        cameraDist = max(cameraDist - 0.2, 0.4)
                        
    while len(points) < num_points:
        points.append(point(100,100))
        
    while len([foo for foo in meals if not foo.hidden]) < num_food:
        meals.append(food(random.randint(-1000,1000), random.randint(-1000,1000)))
    
    tick(screen)
    pygame.display.flip()
    clock.tick(60)