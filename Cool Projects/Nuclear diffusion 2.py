# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 18:02:56 2022

@author: batte
"""

import pygame
import sys
import random
import math

# class Quotient:
    
#     def __init__(self,top,bottom):
#         self.top = top
#         self.bottom = bottom
    
#     def get(self):
#         """Only used for drawing, mapping to color"""
#         return self.top/self.bottom

class Node:
    
    def __init__(self,value,neighbors,x,y):
        self.value = value 
        self.newGivenValue = value
        self.neighbors = set(neighbors)
        self.x = x
        self.y = y
        
    def add_neighbor(self,other):
        self.neighbors.add(other)
        other.neighbors.add(self)
        
    def give_value(self,given):
        self.newGivenValue += given
        
    def reset_value(self):
        self.value = self.newGivenValue
        self.newGivenValue = 0
        
    def update(self):
        # validNeighbors = [other for other in self.neighbors if other.value < self.value]
        # for other in validNeighbors:
        #     other.give_value(self.value/(len(validNeighbors)+1))
        # self.give_value(self.value/(len(validNeighbors)+1))
        # self.value = 0
        givenAway = 0
        validNeighbors = [other for other in self.neighbors if other.value < self.value]
        
        for other in validNeighbors:
            other.give_value((self.value-other.value)/10)
            givenAway += (self.value-other.value)/10
            
        self.give_value(self.value-givenAway)
        self.value = 0
        
    def draw(self,surface):
        pygame.draw.circle(surface,(255,255,max(0,255-int(255 * math.sqrt(self.value)/10))),(self.x,self.y),0 + int(10*math.sqrt(self.value)))
        for other in self.neighbors:
            pygame.draw.line(surface,(255,255,max(0,255-int(255 * math.sqrt(self.value)/10))),(self.x,self.y),(other.x,other.y),1)
        
    
class NodeNetwork:
    
    def __init__(self,nodes):
        self.nodes = nodes
        
    def make_neighbors(self,lowDist,hiDist):
        for startNode in self.nodes:
            for otherNode in self.nodes:
                if otherNode == startNode:
                    continue
                dist = math.sqrt((startNode.x - otherNode.x)**2 + (startNode.y - otherNode.y)**2)
                if dist >= lowDist and dist <= hiDist:
                    startNode.add_neighbor(otherNode)
        
    def tick(self,surface):
        for node in self.nodes:
            node.update()
        for node in self.nodes:
            node.reset_value()
        for node in self.nodes:
            node.draw(surface)
            
            
            
allNodes = []

for i in range(6):
    n = Node(0,[],random.randint(10,490),random.randint(10,490))
    allNodes.append(n)

for i in range(1):    
    n = Node(100,[],random.randint(10,490),random.randint(10,490))
    allNodes.append(n)        
    
nodeNet = NodeNetwork(allNodes)
nodeNet.make_neighbors(0, 200)

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))
    
    nodeNet.tick(screen)
    
    pygame.display.flip()
    clock.tick(4)