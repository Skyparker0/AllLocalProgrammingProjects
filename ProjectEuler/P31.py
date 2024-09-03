# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 07:54:50 2021

@author: batte
"""

worths = [1,2,5,10,20,50,100,200]    #1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p)

coinSets = [[200]]

queue = [[200]]

def greedy_break(coin):
    dictionary = {200:[100,100],
                  100:[50,50],
                  50:[20,20,10],
                  20:[10,10],
                  10:[5,5],
                  5:[2,2,1],
                  2:[1,1],
                  1:[1]}
    
    return dictionary[coin]
    # createdSet = []
    # coinRemaining = coin
    # while coinRemaining > 0:
    #     if coinRemaining == 1:
    #         createdSet.append(1)
    #         coinRemaining = 0
    #         break
    #     for worth in worths[::-1]:
    #         if worth < coinRemaining:
    #             coinRemaining -= worth
    #             createdSet.append(worth)
    #             break
            
    # return createdSet
    

while len(queue) >= 1:
    currentSet = queue.pop(0)
    for index in range(len(currentSet)):
        if currentSet[index] == 1:
            continue
        copy = list(currentSet)
        newCoins = greedy_break(copy.pop(index))
        createdSet = sorted(copy + newCoins)
        if createdSet not in coinSets:
            coinSets.append(createdSet)
            queue.append(createdSet)
    

# currentSet = [200]

# coinSets.add(currentSet)

# def break_down(coinSet, minOrMax):
    

# while currentSet != [1] * 200:
    