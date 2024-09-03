# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 16:36:12 2022

@author: batte
"""

#Star Eater
#(Like Osmos mobile game)

import pygame
import sys
import numpy as np
import random
import time


class Star:
    
    def __init__(self,x,y,radius,player=False):
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity = np.array([0,0])
        self.acceleration = np.array([0,0])
        self.isPlayer = player
        
    def distance(self,other):
        return np.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
        
    def apply_force(self,force):
        self.acceleration = self.acceleration + force/self.radius**2
    
    def change_radius(self,change):
        self.radius += change
    
    def update(self,deltaTime):
        self.velocity = self.velocity + self.acceleration
        self.acceleration *= 0 
        self.x += self.velocity[0]#  * deltaTime * 1000
        self.y += self.velocity[1]#  * deltaTime * 1000
        
        if self.x > WIDTH - self.radius:
            self.velocity *= [-1,1]
            self.x = WIDTH - self.radius
        if self.x < self.radius:
            self.velocity *= [-1,1]
            self.x = self.radius
        if self.y > HEIGHT - self.radius:
            self.velocity *= [1,-1]
            self.y = HEIGHT - self.radius
        if self.y < self.radius:
            self.velocity *= [1,-1]
            self.y = self.radius
        
    
    def draw(self,surface):
        color = (0,20,230) if self.isPlayer else (230,20,0) \
            if self.radius > player.radius else (0,100,100)
        pygame.draw.circle(surface,color,
                           (int(round(self.x)),int(round(self.y))),
                           int(round(self.radius)))
        # pygame.draw.line(surface,(200,200,200),(int(self.x),int(self.y)),
        #                  [int(x) for x in (self.velocity*15 + (self.x,self.y))],2)
        
        
class StarHolder:
    
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.stars = []
        
    def add_star(self,star):
        if star == "rand":
            radius = random.randint(5,10)
            newStar = Star(random.randint(radius,self.width-radius),
                                   random.randint(radius,self.height-radius),
                                   radius)
            
            degrees = random.randint(1,360)
            direction = np.array([np.cos(np.radians(degrees)),
                                  np.sin(np.radians(degrees))])
            
            newStar.apply_force(random.random()*100*direction)
            self.stars.append(newStar)
        else:
            self.stars.append(star)
        
    def tick(self,surface,deltaTime):
        deadStars = []
        
        for star in self.stars:
            if star in deadStars:
                    continue
            
            for otherStar in self.stars:
                if otherStar == star or star in deadStars:
                    continue
                
                distance = star.distance(otherStar)
                
                for i in range(7): #try to get to touching
                    if distance < star.radius + otherStar.radius:
                        starMass = star.radius ** 2
                        otherStarMass = otherStar.radius ** 2
                        
                        larger = 1 if star.radius > otherStar.radius else -1
                        #decides who grows
                        
                        massExchange = 0.05 * min(starMass,otherStarMass)
                        
                        star.apply_force(massExchange*star.velocity*-1)
                        otherStar.apply_force(massExchange*star.velocity)
                        
                        star.radius = np.sqrt(starMass + massExchange * larger) 
                        
                        if star.radius <= 1 and star not in deadStars:
                            deadStars.append(star)
                        
                        otherStar.radius = np.sqrt(
                            otherStarMass - massExchange * larger) 
                        
                        if otherStar.radius <= 1 and otherStar not in deadStars:
                            deadStars.append(otherStar)
                        

            star.update(deltaTime)
            
        for star in deadStars:
            self.stars.remove(star)
            del star
            
        for star in self.stars:
            star.draw(surface)
        
WIDTH = 700
HEIGHT = 700

starHolder = StarHolder(WIDTH,HEIGHT)

for i in range(150):
    starHolder.add_star("rand")

player = Star(WIDTH//2,HEIGHT//2,8,True)

starHolder.add_star(player)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

oldTime = time.time()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if pygame.mouse.get_pressed()[0] and event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            px, py = player.x, player.y

            distance = np.sqrt((mx-px)**2 + (my-py)**2)
            direction = np.array([(px-mx)/distance,(py-my)/distance])
            
            playerMass = player.radius ** 2
            ejectedMass = playerMass * 0.05
            
            playerForce = direction*ejectedMass*8
            
            ejectedStar = Star(player.x + direction[0]*player.radius*-1,
                     player.y + direction[1]*player.radius*-1,
                     np.sqrt(ejectedMass))
            starHolder.add_star(ejectedStar)
            
            ejectedStar.apply_force(playerForce*-1)
            player.apply_force(playerForce)
            player.radius = np.sqrt(playerMass-ejectedMass)
    
    screen.fill((0,0,0))
    starHolder.tick(screen,time.time() - oldTime)
    pygame.display.flip()
    
    oldTime = time.time()
    
    clock.tick(30)