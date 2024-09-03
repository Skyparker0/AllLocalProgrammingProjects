# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 09:10:55 2021

@author: batte
"""

### 5x5 number progression game

import numpy as np
import pygame
import sys
import random

class Board:
    
    def __init__(self):
        self.board = np.array([["_"] * 5] * 5, dtype = '<U16')
        self.avaliableMoves = np.array([[0] * 5] * 5)
        self.turnNum = 1
        self.player = 1
        self.aiPlayers = [1]
        self.winner = None
        
    def __str__(self):
        s = "   1  2  3  4  5  \n"
        for row in range(5):
            s += str(row + 1) + "  "
            s += "  ".join([str(item) for item in self.board[row]])
            s += "\n"
        return s
        
    def draw(self, surface):
        for row in range(5):
            for col in range(5):
                number = self.board[row,col]
                available = self.avaliableMoves[row,col]
                
                BOR = 4
                
                mx,my = pygame.mouse.get_pos()
                mouseRow, mouseCol = my//WIDTH, mx//WIDTH
                
                mouseOnMe = mouseRow == row and mouseCol == col
                
                if number[0] == '1':
                    color = (200,0,0)
                elif number[0] == '2':
                    color = (0,0,200)
                elif available != -1 and mouseOnMe:
                    if self.player == 1:
                        color = (200,100,100)
                    else:
                        color = (100,100,200)
                else:
                    color = (100,100,100)
                    
                    
                    
                # color = (200,0,0) if number[0] == '1' else (0,0,200) if number[0] == '2' \
                #     else (200,100,100) if available != -1 and self.player == 1 \
                #         else (100,100,200) if available != -1 and self.player == 2\
                #             else (100,100,100)
                
                x, y = col * WIDTH + BOR, row * WIDTH + BOR
                pygame.draw.rect(surface, color, pygame.Rect(x,y,WIDTH-BOR,WIDTH-BOR))
                
                if available == -1:
                    text, txtcolor = number[1:], (0,0,0)
                elif mouseOnMe:
                    text, txtcolor = str(available), (150,150,150)
                else:
                    text, txtcolor = "", (0,0,0)

                textsurface = myfont.render(text, False, txtcolor)
                surface.blit(textsurface,(col * WIDTH + 40, row * WIDTH + 25))
                
                
        if self.winner != None:
            pygame.draw.rect(surface, (100,255,100), pygame.Rect(0,250-WIDTH//2,500,WIDTH))
            
            text = "Tie!" if self.winner == "Tie" else "Player " + self.winner + " has won!"
            
            textsurface = myfont.render(text, False, txtcolor)
            surface.blit(textsurface,(0, 250-WIDTH//2))
        else:
            if self.player in self.aiPlayers:
                r, c = self.aiTurn()
                self.turn(r,c)
    
    def aiTurn(self):
        if self.player not in self.aiPlayers:
            return (0,0)
        
        highestNum = -1
        bestRowCol = (0,0)
        for row in range(5):
            for col in range(5):
                number = self.avaliableMoves[row,col]
                if  number > highestNum:
                    highestNum = number
                    bestRowCol = (row,col)
                elif number == highestNum:
                    myPlaceVal = ((row-2)**2 + (col-2)**2)/8
                    lastPlaceVal =  ((bestRowCol[0]-2)**2 + (bestRowCol[1]-2)**2)/8
                    
                    if myPlaceVal < lastPlaceVal:
                        bestRowCol = (row,col)
                    # if random.random() > mustBeAbove:
                    #     bestRowCol = (row,col)
                    
        return bestRowCol
        
    
    def turn(self, row, col, wereNoMoves = False, aiPlayer = False):
        # print(self)
        # row, col, num = input("Player " + str(self.player) + " enter (with spaces) row column number; ").split()
        # print("  ")
        
        if self.winner != None:
            return None
        
        if not wereNoMoves:
            
            if self.avaliableMoves[row,col] == -1:
                return None
            
    
            self.board[row, col] = str(self.player) + str(self.avaliableMoves[row,col])
            
            self.turnNum += 1
            
            if self.turnNum < 3:
                self.player = 0 + self.turnNum
            else:
                self.player = 1 + self.turnNum % 2
            
        ### Adjust self.avaliableMoves
        
        if self.turnNum < 3:
            for row in range(5):
                for col in range(5):
                    self.avaliableMoves[row,col] = 0 if self.board[row,col] == "_" else -1
        else:
            for row in range(5):
                for col in range(5):
                    if self.board[row,col] != "_":
                        self.avaliableMoves[row,col] = -1
                        continue
                    biggestPair = -1
                    for checkRow in range(row-1, row+2):
                        if checkRow < 0 or checkRow > 4:
                            continue
                        for checkCol in range(col-1, col+2):
                            if checkCol < 0 or checkCol > 4:
                                continue
                            check = self.board[checkRow,checkCol]
                            if check != "_" and check[0] == str(self.player) and int(check[1:]) > biggestPair:
                                biggestPair = int(check[1:])
                                
                    if biggestPair != -1:
                        self.avaliableMoves[row,col] = biggestPair + 1
                    else:
                        self.avaliableMoves[row,col] = -1
                        
        noMovesFlag = True                
        
        for row in range(5):
            for col in range(5):
                if self.avaliableMoves[row,col] != -1:
                    noMovesFlag = False
        
        if noMovesFlag:
            if wereNoMoves:
                #Both players have no moves
                self.winner = "Tie"
                bestNum = 0
                for row in range(5):
                    for col in range(5):
                        number = int(self.board[row,col][1:])
                        if number > bestNum:
                            self.winner = self.board[row,col][0]
                            bestNum = number
                        elif number == bestNum:
                            if not self.winner == self.board[row,col][0]:
                                self.winner = "Tie"
                            bestNum = number
            self.turnNum += 1
        
            if self.turnNum < 3:
                self.player = 0 + self.turnNum
            else:
                self.player = 1 + self.turnNum % 2
                
            
            self.turn(0,0, True)



pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()    
 
b = Board()
   
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 40)

WIDTH = 100

while True:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x,y = pygame.mouse.get_pos()
                        b.turn(y//WIDTH, x//WIDTH)
                        
    
    b.draw(screen)
    pygame.display.flip()
    clock.tick(20)