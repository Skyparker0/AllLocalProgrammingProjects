# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 16:21:16 2022

@author: batte
"""

#Pool Physics 

import random
import pygame
import sys
import time as TIME
import math

class Ball:
    
    def __init__(self,x,y,radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.oldX = x
        self.oldY = y
        self.accX = 0
        self.accY = 0
        
    def get_pos(self):
        return self.x,self.y
    
    def get_velocity(self):
        return self.x - self.oldX, self.y - self.oldY
    
    def change_acc(self,accXChange,accYChange):
        self.accX += accXChange
        self.accY += accYChange
    
    def update_position(self,time):
        #get velocity
        vX, vY = self.get_velocity()
        #set old position
        self.oldX,self.oldY = self.x,self.y
        #update new position
        self.x = self.x + vX + self.accX * time * time
        self.y = self.y + vY + self.accY * time * time
        #reset acceleration
        self.accX,self.accY = 0,0
        
    def draw(self,surface):
        pygame.draw.circle(surface,(255,255,255),(round(self.x),round(self.y)),
                           self.radius)
        
        
        
class PoolTable:
    
    def __init__(self):
        self.allBalls = []
        self.width = WIDTH
        self.height = HEIGHT
        
    def new_ball(self,ball):
        self.allBalls.append(ball)
        
    def gravity(self):
        gravConstant = 500
        for ball in self.allBalls:
            ball.change_acc(0,gravConstant)
            
    def apply_constraints(self):
        for ball in self.allBalls:
            r = ball.radius
            
            ball.x = max(r,ball.x)  #left edge
            ball.x = min(self.width-r,ball.x)   #right edge
            
            ball.y = max(r,ball.y) #top edge
            ball.y = min(self.height-r,ball.y) #bottom edge
            
        return True
            
        boundCircleX = self.width/2
        boundCircleY = self.height/2
        boundCircleR = self.width/3
        
        pygame.draw.circle(screen,(255,0,0),
                           (round(boundCircleX),round(boundCircleY)),
                           round(boundCircleR))
        
        for ball in self.allBalls:
            r = ball.radius
            
            xDif = ball.x - boundCircleX
            yDif = ball.y - boundCircleY
            
            distance = math.sqrt(xDif*xDif + yDif*yDif)
            #if the ball is out of the bounding circle
            if distance > boundCircleR - r:
                nX = xDif/distance
                nY = yDif/distance
                
                ball.x = boundCircleX + nX * (boundCircleR-r)
                ball.y = boundCircleY + nY * (boundCircleR-r)
                
    def collisions(self):
        totalBalls = len(self.allBalls)
        for ballOneIndex in range(totalBalls):
            ballOne = self.allBalls[ballOneIndex]
            for ballTwoIndex in range(ballOneIndex+1,totalBalls):
                ballTwo = self.allBalls[ballTwoIndex]
                
                xDif = ballOne.x - ballTwo.x
                yDif = ballOne.y - ballTwo.y
                
                distance = math.sqrt(xDif*xDif + yDif*yDif)
                if distance < ballOne.radius + ballTwo.radius:
                    nX = xDif/(distance+0.001)
                    nY = yDif/(distance+0.001)
                    
                    movementNeeded = (ballOne.radius + ballTwo.radius) - distance

                    rTot = ballOne.radius + ballTwo.radius

                    ballOne.x += movementNeeded * (ballTwo.radius/rTot) * nX
                    ballOne.y += movementNeeded * (ballTwo.radius/rTot) * nY
                    ballTwo.x -= movementNeeded * (ballOne.radius/rTot) * nX
                    ballTwo.y -= movementNeeded * (ballOne.radius/rTot) * nY
                    
        
    def update(self,time):
        steps = 3
        dividedTime = time/steps
        for i in range(steps):
            self.gravity()
            self.apply_constraints()
            self.collisions()
            for ball in self.allBalls:
                ball.update_position(dividedTime)
    
    def draw(self, surface):
        for ball in self.allBalls:
            ball.draw(surface)
    
    
    
    
WIDTH = 700
HEIGHT = 700

table = PoolTable()
for x in range(30):
    table.new_ball(Ball(250+random.randint(-5,300),250+random.randint(-5,5),
                        random.randint(5,10)))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

lastTime = TIME.time()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            table.new_ball(Ball(pygame.mouse.get_pos()[0],
                                pygame.mouse.get_pos()[1],30))
    
    screen.fill((0,0,0))
    table.update(clock.get_time()/1000)#TIME.time() - lastTime)
    lastTime = TIME.time()
    table.draw(screen)
    pygame.display.flip()
    clock.tick(50)