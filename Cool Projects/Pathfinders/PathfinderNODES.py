# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 15:06:13 2022

@author: batte
"""

#Pathfinder

import pygame
import sys
import random
import math

"""

.

"""

class Node:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def pos(self):
        return self.x,self.y
    
    def dist(self,point):
        return math.sqrt((self.x - point[0])**2 + (self.y - point[1])**2)
    
    def draw(self,surface):
        pygame.draw.circle(surface,(200,200,200),
                           (int(self.x),int(self.y)),NODESIZE)

class Edge:
    
    def __init__(self,N1,N2):
        self.N1 = N1
        self.N2 = N2
        
    def draw(self,surface):
        pygame.draw.line(surface,(0,0,200),self.N1.pos(),self.N2.pos(),LINETHICK)

class Graph:
    
    def __init__(self):
        self.allNodes = []
        self.allEdges = []
    
    def addNode(self,node):
        self.allNodes.append(node)
        
    def addEdge(self,edge):
        self.allEdges.append(edge)
        
    def draw(self,surface):
        for n in self.allNodes:
            n.draw(surface)
            
        for e in self.allEdges:
            e.draw(surface)


WIDTH,HEIGHT = 500,500
NODESIZE = 30
LINETHICK = 5

nodeGraph = Graph()

for i in range(4):
    newNode = Node(random.randint(0,WIDTH-1),random.randint(0,WIDTH-1))
    nodeGraph.addNode(newNode)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

newEdgeStart = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if pygame.mouse.get_pressed()[0] and event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            
            for node in nodeGraph.allNodes:
                if node.dist((mx,my)) < NODESIZE:
                    newEdgeStart = node
                    break
        if event.type == pygame.MOUSEBUTTONUP:
            if newEdgeStart:
                mx, my = pygame.mouse.get_pos()
                
                for node in nodeGraph.allNodes:
                    if node.dist((mx,my)) < NODESIZE:
                        nodeGraph.addEdge(Edge(newEdgeStart,node))
                        break
                
                newEdgeStart = None
                
                
    screen.fill((0,0,0))

    nodeGraph.draw(screen)
    #draw new edge
    if newEdgeStart:
        pygame.draw.line(screen,(0,200,0),newEdgeStart.pos(),
                         pygame.mouse.get_pos(),LINETHICK)
    pygame.display.flip()
    
    clock.tick(60)