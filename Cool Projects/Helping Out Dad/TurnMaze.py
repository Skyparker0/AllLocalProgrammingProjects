# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 08:47:24 2022

@author: batte
"""

import numpy as np

class TurnMaze:
    
    def __init__(self,stringMaze):
        #/wall .empty lleft rright sstart ffinish
        self.stringMaze = stringMaze
        rows = self.stringMaze.split(" ")
        self.array = np.array([[char for char in row] for row in rows])
        self.size = self.array.shape[0]
        self.startPos = tuple(np.where(self.array == "s")[i].item() for i in [1,0])
        
        self.solutionLength = len(self.stringMaze) - self.stringMaze.count(" ") \
            - self.stringMaze.count("/")
        self.solutions = []
        self.drawnSolution = 0
        
    def get_value(self,position):
        x,y = position
        if x >= self.size or y >= self.size or x < 0 or y < 0: 
            return "out"
        return self.array[y,x]
    
    def direction(self,positionA,positionB):
        difference = np.array(positionB) - np.array(positionA)
        dx, dy = difference
        
        if dx == -1: 
            return 0
        if dx == 1:
            return 1
        if dy == -1:
            return 2
        if dy == 1:
            return 3
        
    #def __str__
    
    def solve(self,completedPath):        
        last = completedPath[-1]
        lastVal = self.get_value(last)
        
        if lastVal == "f" and len(completedPath) == self.solutionLength:
            self.solutions.append(completedPath)
            
        #handle l and r
        if lastVal == "l":
            moveDirection = self.direction(completedPath[-2], last)
            if moveDirection == 0:
                self.solve(completedPath + [(last[0],last[1]+1)])
            elif moveDirection == 1:
                self.solve(completedPath + [(last[0],last[1]-1)])
            elif moveDirection == 2:
                self.solve(completedPath + [(last[0]-1,last[1])])
            elif moveDirection == 3:
                self.solve(completedPath + [(last[0]+1,last[1])])
                
            return 0
            
        if lastVal == "r":
            moveDirection = self.direction(completedPath[-2], last)
            
            if moveDirection == 0:
                self.solve(completedPath + [(last[0],last[1]-1)])
            elif moveDirection == 1:
                self.solve(completedPath + [(last[0],last[1]+1)])
            elif moveDirection == 2:
                self.solve(completedPath + [(last[0]+1,last[1])])
            elif moveDirection == 3:
                self.solve(completedPath + [(last[0]-1,last[1])])
            
            return 0
        
            
        if lastVal == "out": #if we tried to iterate from an outside square
            return 0
        
        if last in completedPath[:-1]: #visiting an already visited square
            return 0
        
        for nextSquare in [(last[0]-1,last[1]),
                           (last[0]+1,last[1]),
                           (last[0],last[1]-1),
                           (last[0],last[1]+1)]:
            #left right up down
            
            if nextSquare in completedPath:
                continue
                        
            value = self.get_value(nextSquare)
            
            if value == "out":
                continue
            elif value == "/":
                continue
            elif value == ".":
                self.solve(completedPath + [nextSquare])
            elif value == "l":
                self.solve(completedPath + [nextSquare])
            elif value == "r":
                self.solve(completedPath + [nextSquare])
            elif value == "f":
                self.solve(completedPath + [nextSquare])
                
    def draw(self, surface):
        for x in range(self.size):
            for y in range(self.size):
                value = self.get_value((x,y))
                color = (0,0,0)
                
                if value == "out":
                    continue
                elif value == "/":
                    color = (235, 125, 52)
                elif value == ".":
                    color = (147, 150, 144)
                elif value == "l":
                    color = (0,0,200)
                elif value == "r":
                    color = (200,0,0)
                elif value == "f":
                    color = (250,250,250)
                elif value == "s":
                    color = (0,200,0)
                
                pygame.draw.rect(surface,color,pygame.Rect(
                    x*TILESIZE,y*TILESIZE,TILESIZE,TILESIZE))
                
        if self.solutions:
            solution = self.solutions[self.drawnSolution]
            oldX,oldY = [i * TILESIZE + TILESIZE//2 for i in self.startPos]
            for coord in solution:
                x,y = [i * TILESIZE + TILESIZE//2 for i in coord]
                pygame.draw.line(surface,(200,200,0),(oldX,oldY),(x,y),15)
                oldX,oldY = x,y
                    
#keep a record of positions
    
'l..l .//. .//. l.fs'
'l..l .fs. .... llll'
's... .... .... f...'
'.... f... .l.. s/..'
's... .... .... ...f'
'sr.. lr.. .f.. ....'
'...r r.f. .ll. r..s'
maze = TurnMaze('...r r.f. .ll. r..s')
maze.solve([maze.startPos])
print(maze.solutions)
print(len(maze.solutions),"solutions")


import pygame
import sys

TILESIZE = 50
WIDTH = maze.size * TILESIZE
HEIGHT = maze.size * TILESIZE

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                  
    screen.fill((0,0,0))
    maze.draw(screen)
    pygame.display.flip()
    clock.tick(1)