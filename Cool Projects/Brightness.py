# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 17:05:12 2020

@author: batte
"""

import pygame
import sys
import random

class lightObject:
    '''Has methods to calculate if a position should be lit up'''
    
    def __init__(self, coord, brightness):
        self.coord = coord
        self.brightness = brightness
        
    def get_pos(self):
        return self.coord
    
    def get_brightness(self):
        return self.brightness
        
    def light_level(self, pixelPos):
        myPos = list(self.coord)
        myPos.extend(pixelPos)
        myX,myY,oX,oY = myPos
        dist = ((myX-oX)**2 + (myY-oY)**2)**0.5
        
        if dist > self.brightness:
            return 0
        else:
            return round(100 * (1 - (dist/self.brightness)))
            
    
lightObjects = [lightObject((x,y), random.randint(100,300)) for x in [100, 400] for y in [200,600]]

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()    

update = True
cameraDist = 1

def tick():
    step = 20
    for x in range(0, 800, step):
        for y in range(0, 800,step):
            light_levels = [round(255 * light.light_level((x,y)) / 100) for light in lightObjects]
            lightSum = sum(light_levels)
            pixelBrightness = lightSum if lightSum < 255 else 255
            pygame.draw.circle(screen, (pixelBrightness,pixelBrightness,pixelBrightness),(x,y),step)
   
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
                    elif event.button == 1:
                        lightObjects.append(lightObject(pygame.mouse.get_pos(), 100))
                        update = True
    if update:
        tick()
        update = False
        pygame.display.flip()
    clock.tick(10)