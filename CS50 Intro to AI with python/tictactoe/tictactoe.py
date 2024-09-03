"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    flatBoard = [a for b in board for a in b]
    if flatBoard.count(X) > flatBoard.count(O):
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()
    
    for i in range(3):      #X
        for j in range(3):  #Y
            if board[j][i] == EMPTY:
                possibleActions.add((i,j))
                
    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    x = action[0]
    y = action[1]
    
    if board[y][x] is not EMPTY:
        raise ValueError("Tried to place in an occupied spot")
    
    boardCopy = copy.deepcopy(board)
    
    currentPlayer = player(board)
    
    boardCopy[y][x] = currentPlayer
    
    return boardCopy
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winningPlacement = [[1,2,3],
                        [4,5,6],
                        [7,8,9],
                        [1,4,7],
                        [2,5,8],
                        [3,6,9],
                        [1,5,9],
                        [3,5,7],]
    
    def atPos(pos):
        return board[(pos-1)//3][(pos-1)%3]
    
    for placement in winningPlacement:
        if atPos(placement[0]) != EMPTY and len(set([atPos(pos) for pos in placement])) == 1:
            return atPos(placement[0])
        
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or EMPTY not in [a for b in board for a in b]


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    WINNER = winner(board)
    if WINNER == X:
        return 1
    elif WINNER == O:
        return -1
    else:
        return 0

def scoreMINIMAX(board):
    if terminal(board):
        return (utility(board), None)
    
    # Get the value for every move, chooses the best
    PLAYER = player(board)
        
    bestScore = -2 if PLAYER is X else 2
    bestMove = None
    
    for move in actions(board):
        value = scoreMINIMAX(result(board,move))[0]
        
        if PLAYER is X:    #maximize score
            if value == 1:
                return (value, move)
            if value > bestScore:
                bestScore = value
                bestMove = move
        else:              #minimize score
            if value == -1:
                return (value, move)
            if value < bestScore:
                bestScore = value
                bestMove = move
                
    return (bestScore, bestMove)
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    return scoreMINIMAX(board)[1]
