# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:21:35 2020

@author: batte
"""

import numpy as np
import pickle
import random
import time

class tttBoard(object):
    '''Represents a tic tac toe board'''
    
    def __init__(self):
        """Creates a board, and a list of all game states"""
        
        self.board = np.array([[0]*3]*3)
        self.playerOneMoves = {}  # before_move_state : chosen_move
        self.playerTwoMoves = {}
        
    def place(self, player, place):
        '''
        player = 1 or 2
        place = 1 - 9,  1 is top left, 4 is middle left, 9 is bottom right'''
        
        
        if self.at_pos(place) != 0:
            raise ValueError("Tried to place on occupied square")
            
        array_place = ((place - 1) % 3, (place - 1)//3)
        
        if player == 1:
            self.playerOneMoves[str(self)] = place
        else:
            self.playerTwoMoves[str(self)] = place
            
        self.board[array_place] = player
        
    def has_won(self):
        winningPlacement = [[1,2,3],
                            [4,5,6],
                            [7,8,9],
                            [1,4,7],
                            [2,5,8],
                            [3,6,9],
                            [1,5,9],
                            [3,5,7],]
        
        for placement in winningPlacement:
            if len(set([self.at_pos(i) for i in placement])) == 1 and self.at_pos(placement[0]) != 0:
                return self.at_pos(placement[0])
            
        if not 0 in self.board:
            return "tie"
        
        return None
            
        
                
   
    def at_pos(self,pos):
        return int(self.board[(pos - 1) % 3, (pos - 1)//3])
        
    def get_all_moves(self,player):
        if player == 1:
            return self.playerOneMoves
        elif player == 2:
            return self.playerTwoMoves
        
    def get_board(self):
        return self.board
        
    def __str__(self):
        string = ""
        
        for y in range(3):
            for x in range(3):
                string += str(self.board[x,y])
            #REMOVE IF NOT PLAYING#
            #string += "\n"
                
        return string
    
    def pretty_str(self):
        string = ""
        
        for y in range(3):
            for x in range(3):
                string += str(self.board[x,y]) + " "
            string += "\n"
                
        return string
    
moveData = {}   # strings of game positions assigned to dicts with the favoribility of each move
                # "000000000":{1:0,2:0,3:0,4:0,5:10000,6:0,7:0,8:0,9:0} play in the middle :\

saveDataFile = "Cool Projects\TicTacToeMachineLearning\TTTMovesDict.pickle"

def saveTo(data, fileName):
    with open(fileName, 'wb') as handle:
        pickle.dump(data,handle)

def takeFrom(fileName):
    with open(fileName, 'rb') as handle:
        loaded = pickle.load(handle)
    return loaded

def reset(fileName):
    startingData = {}
    saveTo(startingData, fileName)
    
def next_player(boardstate):
    '''Boardstate: 9 char str
    returns 1 or 2'''
    
    if boardstate.count("1") > boardstate.count("2"):
        return 2
    else:
        return 1
    
    

def chooseMove(boardState, human_players = ()):
    '''Uses moveData to choose a move based on the boardState
    boardState = string of 9 digits: 0, 1, or 2
    returns the thing it chose'''
    
    useRandom = True   #True: picks based on probability False: picks on the max choice
    
    if next_player(boardState) in human_players: 
        chosenMove = input("Player " + str(next_player(boardState)) + " Move:  ")
        return int(chosenMove)
    
    if boardState in moveData:   #If it is already in the move data, choose based on that
        posChoices = moveData[boardState]
        
        if useRandom:
            return random.choices(list(posChoices.keys()),  
                                  weights = list(posChoices.values()))[0]   #Must be [0] spot
        else:
            maximumVal = -1
            choiceMove = 0
            for move in posChoices.keys():
                val = posChoices[move]
                if val == maximumVal:
                    choiceMove = random.choice([move,choiceMove])
                elif val > maximumVal:
                    maximumVal = val
                    choiceMove = move
                    
            return choiceMove
    else:    #Choose a random possible choice and add the boardState to the moveData
        newMoveData = {}   # zeros for impossible moves, 10s or some other number for possible moves
        
        for move in range(1,10):
            if boardState[move-1] != "0":
                newMoveData[move] = 0
            else:
                newMoveData[move] = 100
        
        moveData[boardState] = newMoveData
        
        return chooseMove(boardState)
    


def play_match_ttt(human_players = (), visuals = False):
    '''
    chosenMove is used to decide moves based off a game state.
    
    returns the moves of the winning and losing player, to be saved'''
    
    if len(human_players) > 0:
        visuals = True
    
    playBoard = tttBoard()
    
    winner = None
    currentPlayer = 1
    
    while winner == None:
        if visuals:
            print(playBoard.pretty_str())
            time.sleep(0.5)
        boardState = str(playBoard)      ########
        chosenMove = chooseMove(boardState, human_players)
        playBoard.place(currentPlayer, chosenMove)
        currentPlayer = currentPlayer % 2 + 1
        winner = playBoard.has_won()
        
    if visuals:
        print(playBoard.pretty_str())
        print("\nWinner:",winner)
        time.sleep(0.5)
        
        
    if winner == "tie":
        return "tie", {**playBoard.get_all_moves(1), **playBoard.get_all_moves(2)}
    else:
        return playBoard.get_all_moves(winner), playBoard.get_all_moves(winner % 2 + 1)
    
moveData = takeFrom(saveDataFile)
    
def train_on_ttt(numGames, human_players = (), visuals = False):
    
    
    for g in range(numGames):
        winningMoves, losingMoves = play_match_ttt(human_players,visuals)    #TAKE OUT VISUAL
        
        if winningMoves == "tie":
            for state in losingMoves.keys():
                if state not in moveData:
                    chooseMove(state)    #Cheep way of including a new state, hopefuly won't be used
                tieMove = losingMoves[state]
                moveData[state][tieMove] += 0.5 #increments the chosen "good" move for a state
            
            continue
        
        for state in winningMoves.keys():    #rewards good moves
            if state not in moveData:
                chooseMove(state)    #Cheep way of including a new state, hopefuly won't be used
            winningMoveOnState = winningMoves[state]
            # if moveData[state][winningMoveOnState] >  500:
            #     moveData[state][winningMoveOnState] = sum(moveData[state].values())//(9-list(moveData[state].values()).count(0))
            moveData[state][winningMoveOnState] += 1 #increments the chosen "good" move for a state
            
        subBy = 1
            
        for state in sorted(losingMoves.keys())[::-1]:    #Harms bad moves
            if state not in moveData:
                chooseMove(state)    #Cheep way of including a new state, hopefuly won't be used
            loserMoveOnState = losingMoves[state]
            moveData[state][loserMoveOnState] -= subBy
            if moveData[state][loserMoveOnState] < 1:
                moveData[state][loserMoveOnState] = 1
                
        #Greatly rewards winning move and greatly harms losing move
        winningState = sorted(winningMoves.keys())[-1]
        moveData[winningState][winningMoves[winningState]] = 10000
        
        losingState = sorted(losingMoves.keys())[-1]
        moveData[losingState][losingMoves[losingState]] = 0.01
        
        
    
    saveTo(moveData,saveDataFile)
    
    
if __name__ == "__main__":
    #reset(saveDataFile)
    moveData = takeFrom(saveDataFile)
    train_on_ttt(10000)
    
    # train_on_ttt(10,(1,))