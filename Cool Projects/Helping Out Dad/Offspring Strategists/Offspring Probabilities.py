# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 09:41:56 2022

@author: batte
"""

import random
import matplotlib as plt

def probabability_survive(tokens, nurture, rounds = 1000):   
    #probability of one offspring surviving
    survived = 0
    for r in range(rounds):
        nurtureRemaining = nurture
        won = True
        for turn in range(tokens):
            while True: #use nurture if necessary
                if random.randint(1,6) > tokens:
                    if nurtureRemaining == 0:
                        won = False
                    else:
                        nurtureRemaining -= 1
                else:
                    break
        if won:
            survived += 1
    return survived,rounds, survived/rounds


def strategy_compare(nurturePoints,totalTokens = 15,smallBabyTokens=1,
                     bigBabyTokens=5,rounds=10000):
    #avg number and std dev of survivng ofspring comparison between lots of babies 
    #and few babies
    smallResults = []  #number of offspring survived
    bigResults = []
    
    smallBabyPopulation = totalTokens//smallBabyTokens
    bigBabyPopulation = totalTokens//bigBabyTokens
    
    for r in range(rounds):
        
        #start with the small babies
        nurtureRemaining = nurturePoints
        smallWinners = [True] * smallBabyPopulation #all start winning till elim
        
        for turn in range(smallBabyTokens): #have to survive for your # of tokens
            for babyIndex in range(smallBabyPopulation):
                while True: #use nurture as long as necessary
                    if random.randint(1,6) > smallBabyTokens:
                        if nurtureRemaining == 0:
                            smallWinners[babyIndex] = False
                        else:
                            nurtureRemaining -= 1
                    else:
                        break
                    
        smallResults.append(sum(smallWinners))
        
        #next the big babies
        nurtureRemaining = nurturePoints
        bigWinners = [True] * bigBabyPopulation #all start winning till elim
        
        for turn in range(bigBabyTokens): #have to survive for your # of tokens
            for babyIndex in range(bigBabyPopulation):
                while True: #use nurture as long as necessary
                    if random.randint(1,6) > bigBabyTokens:
                        if nurtureRemaining == 0:
                            bigWinners[babyIndex] = False
                        else:
                            nurtureRemaining -= 1
                    else:
                        break
                    
        bigResults.append(sum(bigWinners))
        
    #find averages and things
    
    smallAvg = sum(smallResults)/rounds
    bigAvg = sum(bigResults)/rounds
    smallDeviation = (sum([(x-smallAvg)**2 for x in smallResults])/(rounds-1))**0.5
    bigDeviation = (sum([(x-bigAvg)**2 for x in bigResults])/(rounds-1))**0.5
    
    print(f"using {nurturePoints} nurture\n")
    print(f"""smallAvg {smallAvg},\nbigAvg {bigAvg},
          \nsmallDeviation {smallDeviation},\nbigDeviation {bigDeviation}""")
        
    #plot the data
        
    plt.pyplot.hist(smallResults,bins = list(range(0,max(smallResults))),
                    label = f"small (avg {smallAvg})")
    plt.pyplot.hist(bigResults,bins = list(range(0,max(smallResults))),
                    label = f"big (avg {bigAvg})",rwidth = 0.5)
    plt.pyplot.xticks(range(max(smallResults)))
    plt.pyplot.legend()
    
    plt.pyplot.show()
    

for nurture in range(0,7):   
    strategy_compare(nurture)