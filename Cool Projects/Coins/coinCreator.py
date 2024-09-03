# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 07:23:12 2021

@author: batte
"""

import pygame
import random
from PIL import Image
import sys

image = Image.new("RGB",(30,30),100)
#image = pygame.image.load(image)

class Coin(object):
    
    def __init__(self, x,y):
        self.x = x
        self.y = y
        
        self.fallTo = random.randint(y, y+40)
        
        self.yvel = 0
        self.xvel = 0
        
        self.ticksComp = 0
        
    def throw(self, xvel, yvel):
        self.xvel = xvel
        self.yvel = yvel
    
    def update(self):
        self.x += self.xvel
        self.y += self.yvel
        
        self.xvel *= 0.8
        self.yvel += 1
        
        if self.y > self.fallTo:
            self.yvel = 0
            
        if self.yvel == 0:
            self.yvel = random.randint(-10,-20)
        
        self.ticksComp += 1
        
    def draw(self, screen):
        pygame.blit(screen, image, (round(self.x),round(self.y)))
        

def simulate(screen):
    
    coins = [Coin(350,350) for x in range(10)]
    for coin in coins:
        coin.throw(10,-10)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        screen.fill((200,200,200))
        
        for coin in coins:
            coin.update()
            
        for coin in coins:
            coin.draw(screen)



pygame.init()
screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()

# clock.tick(0.5)
simulate(screen)
pygame.quit()