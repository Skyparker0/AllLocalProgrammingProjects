# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 07:35:41 2021

@author: batte
"""

##
## https://www.youtube.com/watch?v=-L-WgKMFuhE
##

import numpy as np

class Node:
    
    def __init__(self, parent, fCost, walkCost, pos):
        self.parent = parent
        self.fCost = fCost
        self.walkCost = walkCost
        self.pos = list(pos)
        
    def set_fCost(self, new):
        self.fCost = new
    
    def get_parent(self):
        return self.parent
    
    def get_fCost(self):
        return self.fCost
    
    def get_walkCost(self):
        return self.walkCost
    
    def get_pos(self):
        return self.pos   ###Bookmark- working on new_fCost###

class Grid:
    
    def __init__(self, array):
        self.npArray = np.array(array) #each of the values is a number, representing weight, or -1, for wall
        
    def get_value(self, x, y):
        '''X = 0, Y = 0 is the top left'''
        
        if x < 0 or y < 0 or x >= self.npArray.shape[1] or y >= self.npArray.shape[0]:
            return None
        
        return self.npArray[y,x]
        
    
class AStar:
    
    def __init__(self, grid, start, end):
        '''
        Parameters
        ----------
        grid : Grid
            The grid to be solved
        start : Tuple
            The (x,y) coordinate on the grid where pathfinding starts
        end : Tuple
            The (x,y) coordinate on the grid the pathfinding is trying to reach

        Returns
        -------
        None.
        '''
        
        self.grid = grid
        self.start = start
        self.end = end
        
        self.openNodes = []     
        self.closedNodes = {}    #pos:node   
        
        self.openNodes.append(Node(None, 1, 0, self.start))
        
    def new_walkCost_fCost(self, oldPos, newPos, oldWalkCost):
        distFromGoalCost = sum((np.array(list(newPos)) - np.array(list(self.end)))**2)**0.5
        stepCost = sum((np.array(oldPos) - np.array(newPos))**2)**0.5 * self.grid.get_value(newPos[0], newPos[1])
        newWalkCost = stepCost + oldWalkCost
        newFCost = distFromGoalCost + newWalkCost
        return newWalkCost,newFCost
    
    def solve(self):
        '''Returns the list of nodes that is the shortest path'''
        
        while len(self.openNodes) >= 1:
            lowestFCost = self.openNodes[0].get_fCost()
            bestNode = self.openNodes[0]
            
            for openNode in self.openNodes:
                if openNode.get_fCost() < lowestFCost:
                    bestNode = openNode
                    lowestFCost = openNode.get_fCost()
                    
            self.openNodes.remove(bestNode)
            self.closedNodes[tuple(bestNode.get_pos())] = bestNode
            
            if tuple(bestNode.get_pos()) == self.end:
                nodePath = []
                currentNode = bestNode
                nodePath.insert(0, currentNode)
                while currentNode.get_parent() != None:
                    currentNode = currentNode.get_parent()
                    nodePath.insert(0, currentNode)
                return nodePath
            
            directions = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
                
            #directions = [(0,-1), (-1,0),(1,0),(0,1)]
            
            for posChange in directions:
                x, y = np.array(bestNode.get_pos()) + np.array(posChange)
                if (x,y) in self.closedNodes or self.grid.get_value(x, y) == -1 or self.grid.get_value(x, y) == None:
                    continue
                

                walkCost, fCost = self.new_walkCost_fCost(bestNode.get_pos(), (x,y), bestNode.get_walkCost())
                
                alreadyOpen = False
                for node in self.openNodes:
                    if tuple(node.get_pos()) == (x,y):
                        alreadyOpen = True
                        if node.get_fCost() > fCost:
                            node.fCost = fCost
                            node.walkCost = walkCost
                
                if not alreadyOpen:
                    newNode = Node(bestNode, fCost, walkCost, (x,y))
                    self.openNodes.append(newNode)
                    
        return "None Found"
                
            
            
                    


nArray = np.array([[1] * 10] * 10)
nArray[8,0] = 100

grid = Grid(nArray)

A = AStar(grid, (0,0), (0,9))

for node in A.solve():
    print(node.get_pos())

print(nArray)