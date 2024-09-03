# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 14:47:53 2021

@author: batte
"""

import random

path = "C:/Users/batte/OneDrive/_Parker/Python/ProjectEuler/non-code-files/p096_sudoku.txt"

lines = []

with open(path) as handle:
    for line in handle:
        lines.append(line.strip("\n"))
        
        
class Sudoku:
    
    def __init__(self,text):
        self.numbers = [[text[9*y + x] for x in range(9)] for y in range(9)]
        
        #        #INITIAL LOGIC 
        # while True:
        #     changeMade = False
            
        #     for x in range(9):
        #         for y in range(9):
        #             if self.get(x, y) != "0":
        #                 continue
                    
        #             unusables = self.row(y) + self.column(x) + self.box(x,y)
        #             usables = [i for i in "123456789" if i not in unusables]
                    
        #             if len(usables) == 1:
        #                 changeMade = True
        #                 self.put(x,y,usables[0])
                        
                        
        #     if not changeMade:
        #         break
        
        self.lockedCells = []
        for y in range(9):
            for x in range(9):
                if self.get(x,y) != '0':
                    self.lockedCells.append([x,y])
        
        
    def get(self,x,y):
        return self.numbers[y][x]
    
    def put(self,x,y,value):
        self.numbers[y][x] = value
    
    def column(self,x):
        nonZeroes = []
        for y in range(9):
            value = self.get(x,y)
            if value != "0":
                nonZeroes.append(value)
        return nonZeroes
    
    def row(self,y):
        nonZeroes = []
        for x in range(9):
            value = self.get(x,y)
            if value != "0":
                nonZeroes.append(value)
        return nonZeroes
    
    def box(self,x,y):
        """Accepts the position of the value that you want to find its box for
        ex. containing_box(2,2) would give the values of the top left box"""
        
        boxX, boxY = x//3 * 3, y//3 * 3
        
        nonZeroes = []
        for valueX in range(boxX,boxX + 3):
            for valueY in range(boxY,boxY+3):
                value = self.get(valueX,valueY)
                if value != "0":
                    nonZeroes.append(value)
        return nonZeroes
    
    def solve(self):
        
        def jump_forward(px,py):
            px += 1
            while py <= 8:
                if px > 8:
                    px = 0
                    py += 1
                if py > 8:
                    break
                if [px,py] in self.lockedCells:
                    px += 1
                    if px > 8:
                        px = 0
                        py += 1
                else:
                    return px,py
                
            return "DONE","DONE"
            
        def jump_back(px,py):
            original = [px,py]
            px -= 1
            while py >= 0:
                if px < 0:
                    px = 8
                    py -= 1
                if py < 0:
                    break
                if [px,py] in self.lockedCells:
                    px -= 1
                    if px < 0:
                        px = 8
                        py -= 1
                else:
                    return px,py
            return "aa"
            
        
        pointerX,pointerY = jump_forward(-1,0)
        if pointerX == "DONE":
            return self.numbers
        
        
        while True:
            if self.get(pointerX, pointerY) == "0":
                self.put(pointerX, pointerY, "1")
                
            if list(self.row(pointerY) + self.column(pointerX) + self.box(pointerX, pointerY)).count(self.get(pointerX,pointerY)) == 3:
                pointerX,pointerY = jump_forward(pointerX,pointerY)
                if pointerX == "DONE":
                    return self.numbers
            else:
                self.put(pointerX, pointerY, str(int(self.get(pointerX, pointerY))+1))
            
            while True:
                if int(self.get(pointerX, pointerY)) > 9:
                    self.put(pointerX, pointerY, "0")
                    pointerX,pointerY = jump_back(pointerX,pointerY)
                    self.put(pointerX, pointerY, str(int(self.get(pointerX, pointerY))+1))
                else:
                    break
    def __str__(self):
        finStr = ""
        for y in range(9):
            for x in range(9):
                finStr += self.get(x,y) 
                finStr += "." if [x,y] in self.lockedCells else " "
            finStr += "\n"
        
        return finStr
    
puzzles = []
        
for i in range(0,len(lines),10):
    puzzles.append(Sudoku("".join(lines[i+1:i+10])))
    
total = 0
    
for puzzle in puzzles:
    puzzle.solve()
    total += int("".join(puzzle.numbers[0][0:3]))
    
print(total)