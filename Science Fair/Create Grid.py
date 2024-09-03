# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 17:55:53 2020

@author: batte
"""

import objects as o
import matplotlib.pyplot as plt 
import pygame
import random

minePlacement = []
while len(minePlacement) < 1:
    x = random.randint(200,500)
    y = random.randint(200,500)
    #if 150 > (abs(x-350) ** 2 + abs(y-350)** 2)**0.5 > 0:
    minePlacement.append([x,y])
            
rocketPlacement = [(100,100),(600,600)]

x = list(range(1,100))
y = [o.get_ticks(False, 1000, numRobots, 1000, minePlacement, rocketPlacement, 10, 5, 1000, 10,10) for numRobots in x]

#get_ticks(visualize, ticks, robotsInRocket, rocketWLimit, minePlacement, rocketPlacement, speed, carryOffset, mineResources, miningSpeed, depositSpeed):

plt.plot(x,y)

plt.show()