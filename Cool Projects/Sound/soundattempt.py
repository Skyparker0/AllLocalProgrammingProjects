# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 18:45:02 2021

@author: batte
"""

import pygame
import random
import time
import sys


pygame.mixer.init(frequency = 44100, size = -16, channels = 1, buffer = 2**12) 

rain_sound = pygame.mixer.Sound("Rain.wav")
thunder_sound = pygame.mixer.Sound("bgNoise.wav")


# channel1 = pygame.mixer.Channel(0) # argument must be int
# channel2 = pygame.mixer.Channel(1)

# channel1.play(rain_sound, loops = -1)


pygame.init()
screen = pygame.display.set_mode((300,200))
clock = pygame.time.Clock()    

while True:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        
    ch = thunder_sound.play()
    while ch.get_busy():
        pygame.time.delay(1)
                        
    pygame.display.flip()
    screen.fill((random.randint(0,10),0,0))
    clock.tick(30)