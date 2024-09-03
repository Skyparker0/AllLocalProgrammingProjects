# -*- coding: utf-8 -*-
"""
Created on Sat May  1 07:31:29 2021

@author: batte
"""

import random

def choose(lst,num):
    '''Chooses and returns all combonations of num items from lst;
    choose([1,2,3],2) -> [[1,2],[1,3],[2,3]]'''
    
    if num == 1:
        return [[i] for i in lst]

    reTerms = []
    
    for start in range(0,len(lst)-num+1):
        for end in choose(lst[start+1:],num-1):
            reTerms.append([lst[start]] + end)

    return reTerms
    
    

class Player(object):
     
    def __init__(self):
        self.score = 0
        
    def __str__(self):
        return str(self.score)
    
    def play_turn(self, vis = False):
        hand = [random.randint(1,6) for i in range(4)]
        
        if vis:
            print("- - - - - - -")
            print(hand)
            
        handCombonations = choose(hand,2) + choose(hand,3) + choose(hand,4)
            
        if any([sum(combo) == 10 for combo in handCombonations]):
            self.score -= 1
            
            if vis:
                print("Makes ten, subtracting 1 point and re-rolling")
                print("Score: " + str(self.score))
                
            scores = self.play_turn(vis)
            return [-1] + scores            
        else:
            points = max(hand)
            self.score += points
            
            if vis:
                print("Does not make ten, adding " + str(points) + " points")
                print("Score: " + str(self.score))
                
            return [points]
                

# Expected value and number of 10s rolled

# p = Player()

# allScores = []

# for i in range(10):
#     allScores += p.play_turn(True)

# print('expectedValue = ' + str(sum(allScores)/len(allScores)))
# print('ten prec = ' + str(allScores.count(-1)/len(allScores)))



# Length of a match, and number of losses and wins,
# going to -10 (loss) or 10 (win)

# def ten_or_minus_ten():
#     p = Player()
#     roundsPlayed = 0
    
#     while p.score > -10 and p.score < 10:
#         p.play_turn()
#         roundsPlayed += 1
        
#     if p.score > 10:
#         return (10, roundsPlayed)
    
#     return (-10, roundsPlayed)

# results = [ten_or_minus_ten() for i in range(1000)]

# totalGames = len(results)
# wins = [result[0] for result in results].count(10)
# losses = [result[0] for result in results].count(-10)

# turnsToWin = [result[1] for result in results if result[0] == 10]

# print(sum(turnsToWin)/wins)



# How many rolls per turn

numberOfRolls = []

p = Player()

for i in range(10000):
    numberOfRolls.append(len(p.play_turn()))
    
print(sum(numberOfRolls)/len(numberOfRolls))