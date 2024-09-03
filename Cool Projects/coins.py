def coinsUsedChange(coinValues, goal):
    if goal < min(coinValues): #just pennies
        return goal

    best = 100
    for coinValue in coinValues:  #check each coin taken using recursion
        if coinValue > goal:
            continue

        coinsUsed = 1 + coinsUsedChange(coinValues, goal-coinValue)
        if coinsUsed < best:
            best = coinsUsed

    return best

def coinsUsedDollar(coinValues):
    return sum([coinsUsedChange(coinValues,goal) for goal in range(1,101)])

#print(coinsUsedChange([15,25],30))
coinTypes = 3
for coinA in range(2,5):#102-coinTypes):
    for coinB in range(coinA+1,6):#103-coinTypes):
        for coinC in range(coinB+1,7):#104-coinTypes):
            coins = coinsUsedDollar([coinA,coinB,coinC])
            print(coinA,)