# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:49:48 2020

@author: batte
"""

##This code will use robot simulation JUST DATA.py and simulate lots of tests

import robot_simulation_JUST_DATA as rSim
import matplotlib.pyplot as plt
import random

numRobots = list(range(1,100,1))# + list(range(10,101,2))
numTicks = []    # the number of ticks it takes for x robots with the below settings to mine and deposit all resources


# maxticks, robotsInRocket, rocketWLimit, minePos, rocketPos, speed, carryOffset, mineResourses, miningSpeed, depositSpeed
maxTicks = 5000
#robots in rocket comes from the above list
rocketWeightLimit = 1000   # how much pounds of robot can be carried
# minePositions = [(x,y) for x in range (200,401,100) for y in range (200,401,100)]    #Let's keep the mines in a 3x3 grid
# rocketPositions = [(100,100), (500,500)]    #2 rockets at the edges of the grid
speed = 10    #how fast the robots move
carryOffset = 0    # how much is subtracted from a robot's carry weight
mineResourses = 1000  # how many pounds held by a single mine
miningSpeed = 10    # how fast a robot mines from a mine per tick
depositSpeed = 2    #how many ticks it takes to deposit all resources

duplicates = 3
startNumRobots = 1
endNumRobots = 11
skipCount = 2

def random_setups():
    base_setups = []
    mine_setups = []
    for x in range(startNumRobots,endNumRobots,skipCount): #How many different scenarios? 
        addToBases = []
        addToMines = []
        for numCopies in range(duplicates):
            addToBases.append([(random.randint(0,800),random.randint(0,800)) for i in range(1)])#How many bases?
            addToMines.append([(random.randint(0,800),random.randint(0,800)) for i in range(x)])#How many mines?
        base_setups.append(addToBases)
        mine_setups.append(addToMines)
    return base_setups,mine_setups

base_setups,mine_setups = random_setups()

for nRobots in numRobots:
    tickMap = []
    for setupNum in range(len(base_setups)):
        copyTicks = []
        
        for copySetup in range(len(mine_setups[setupNum])):
            copyTicks.append(rSim.simulate(maxTicks, nRobots, rocketWeightLimit, mine_setups[setupNum][copySetup], base_setups[setupNum][copySetup], speed, carryOffset, mineResourses, miningSpeed, depositSpeed))
            
        tickMap.append(sum(copyTicks)/len(copyTicks))
    numTicks.append(tickMap)#(sum(tickMap)/len(tickMap))
    
for i in range(len(numTicks[0])):
    plt.plot(numRobots, [x[i] for x in numTicks], label=str(len(mine_setups[i][0]))) #//2
    
plt.legend()
plt.ylim(ymin=0)
plt.ylabel("ticks")
plt.xlabel("robots")
plt.grid()
plt.show()