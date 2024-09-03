# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 10:46:19 2022

@author: batte
"""

import pygame
import sys
import numpy as np
import random



def is_on_right_side(x, y, xy0, xy1):
    x0, y0 = xy0
    x1, y1 = xy1
    a = float(y1 - y0)
    b = float(x0 - x1)
    c = - a*x0 - b*y0
    return a*x + b*y + c >= 0    # > means no edges

def test_point(x, y, vertices):
    num_vert = len(vertices)
    is_right = [is_on_right_side(x, y, vertices[i], vertices[(i + 1) % num_vert]) for i in range(num_vert)]
    all_left = not any(is_right)
    all_right = all(is_right)
    return all_left or all_right

def shuffled(lst):
    l = [x for x in lst]
    random.shuffle(l)
    return l

class Board:
    
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.circleArray = np.array([[random.choice([0,1]) for y in range(height)] for x in range(width)])
        self.anchorPoint = None
        
    def get_val(self,x,y):
        if x > self.width-1 or x < 0 or int(x) != x   or   y > self.height-1 or y < 0 or int(y) != y:
            return None
        return self.circleArray[int(x),int(y)]
    
    def set_val(self,x,y,value):
        self.circleArray[int(x),int(y)] = value
        
    def drop(self,x,y):
        if y < 0:
            self.set_val(x, y+1, random.choice([0,1]))
        elif self.get_val(x,y) == -1:
            self.drop(x,y-1)
        else:
            val = self.get_val(x,y)
            self.set_val(x, y, -1)
            self.set_val(x,y+1,val)
        
    def points_from_corners(self, firstPos, secondPos):
        x1,y1,x2,y2 = firstPos + secondPos
        xDif = x2-x1
        yDif = y2-y1
        newPos1 = (x1 + xDif/2 - yDif/2, y1 + yDif/2 + xDif/2)
        newPos2 = (x1 + xDif/2 + yDif/2, y1 + yDif/2 - xDif/2)
        return firstPos,newPos1,secondPos,newPos2
      
    def process_click(self,x,y):
        tileX = x // CIRCLESIZE
        tileY = y // CIRCLESIZE
        
        if self.anchorPoint == (tileX,tileY):
            self.anchorPoint = None
        elif self.anchorPoint == None:
            self.anchorPoint = (tileX,tileY)
        else:
            #check if valid
            fourCorners = self.points_from_corners(self.anchorPoint,(tileX,tileY))
            startVal = self.get_val(fourCorners[0][0],fourCorners[0][1])
            if all(self.get_val(fourCorners[i][0],fourCorners[i][1]) == startVal for i in range(4)) and startVal in [0,1]:
                for i in range(4):
                    self.set_val(fourCorners[i][0], fourCorners[i][1], -1)
                    
                print("Turn taken\n")
                    
                for x in range(self.width):
                    for y in range(self.height):
                        value = self.get_val(x,y)
                        if value == -1:
                            continue
                        
                        if test_point(x,y,fourCorners):
                            self.set_val(x,y,-1)
                     
                self.anchorPoint = None       
                     
                while True:
                    changeMade = False
                    for x in range(self.width):
                        for y in range(self.height):
                            value = self.get_val(x,y)
                            if value == -1:
                                changeMade = True
                                self.drop(x,y-1)
                                screen.fill((0,0,0))
                                self.draw(screen)
                                pygame.display.flip()
                                clock.tick(60)
                    
                    
                    if changeMade == False:
                        break
                            
                
      
    def draw(self,surface):
        for x in range(self.width):
            for y in range(self.height):
                value = self.get_val(x,y)
                if value == -1:
                    continue
                pygame.draw.circle(surface,COLORS[value],(x*CIRCLESIZE + CIRCLESIZE//2,y*CIRCLESIZE + CIRCLESIZE//2),CIRCLESIZE//2)
                
        if self.anchorPoint != None:
            mouseX,mouseY = pygame.mouse.get_pos()
                    
            for pos in self.points_from_corners(self.anchorPoint,(mouseX//CIRCLESIZE,mouseY//CIRCLESIZE)):
                pygame.draw.circle(surface,(100,100,100),[int(pos[i] * CIRCLESIZE + CIRCLESIZE//2) for i in [0,1]],CIRCLESIZE//8)
                
                
    def generate_puzzle(self, numSquares):
        self.circleArray = np.array([[-1]*self.height]*self.width)
        allCoords = []
        for x in range(self.width):
            for y in range(self.height):
                allCoords.append((x,y))
                
        swapsMade = 0
                
        for i in range(numSquares):
            changeMade = False
            swapMade = False
            for startingCorner in shuffled(allCoords):
                if changeMade:
                    break
                for endingCorner in shuffled(allCoords):
                    if changeMade:
                        break
                    
                    if startingCorner == endingCorner:
                        continue
                    
                    fourCorners = self.points_from_corners(startingCorner,endingCorner)
                    startVal = self.get_val(fourCorners[0][0],fourCorners[0][1])
                    if all(self.get_val(fourCorners[i][0],fourCorners[i][1]) == startVal for i in range(4)) and startVal == -1:
                        changeMade = True
                        chosenValue = random.choice([0,1])
                        for i in range(4):
                            self.set_val(fourCorners[i][0], fourCorners[i][1], chosenValue)
                            
                        for x in range(self.width):
                            for y in range(self.height):
                                value = self.get_val(x,y)
                                if value == -1:
                                    continue
                                
                                if test_point(x,y,fourCorners):
                                    self.set_val(x,y,abs(value-1))
                                    swapMade = True
                                    
            if swapMade:
                swapsMade += 1
                
            if not changeMade:
                self.generate_puzzle(numSquares)
                return "Could not complete- trying again"
            
        if swapsMade < SWAPSNEEDED:
            self.generate_puzzle(numSquares)
            return "Not enough swaps made- trying again"
        
        for i in range(DUMMYDOTS):
            changeMade = False
            for coord in shuffled(allCoords):
                if changeMade:
                    break
                if self.get_val(coord[0],coord[1]) == -1:
                    self.set_val(coord[0], coord[1], random.choice([0,1]))
                    changeMade = True
                

        

WIDTH = 7
HEIGHT = 7
CIRCLESIZE = 50
SWAPSNEEDED = 3
SQUARESGENERATED = 5
DUMMYDOTS = 3
COLORS= [(255,0,0),(0,0,255)]

history = []
historyIndex = -1
oldBoard = None

b = Board(WIDTH,HEIGHT)

pygame.init()
screen = pygame.display.set_mode((CIRCLESIZE * WIDTH, CIRCLESIZE * HEIGHT))
clock = pygame.time.Clock()    

while True:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if historyIndex > 0:
                            historyIndex -= 1
                            b.circleArray = history[historyIndex]
                            oldBoard = b.circleArray.copy()
                    if event.key == pygame.K_RIGHT:
                        if historyIndex < len(history) - 1:
                            historyIndex += 1
                            b.circleArray = history[historyIndex]
                            oldBoard = b.circleArray.copy()
                            
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x,y = pygame.mouse.get_pos()
                        b.process_click(x, y)
                    if event.button in [2,3]:
                        b.generate_puzzle(SQUARESGENERATED)
                  
    if not np.array_equal(b.circleArray, oldBoard):
        history[historyIndex:] = []
        history.append(oldBoard)
        oldBoard = b.circleArray.copy()
        history.append(oldBoard)
        historyIndex += 1
                  
    screen.fill((0,0,0))
    b.draw(screen)
    pygame.display.flip()
    clock.tick(30)