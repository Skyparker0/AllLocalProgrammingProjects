# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 07:45:30 2021

@author: batte
"""

def compute():
    TOTAL = 200
    
    # At the start of each loop iteration, ways[i] is the number of ways to use {any copies
    # of the all the coin values seen before this iteration} to form an unordered sum of i
    ways = [1] + [0] * TOTAL
    for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
        for i in range(len(ways) - coin):
            ways[i + coin] += ways[i]
        print(ways)
    return str(ways[-1])


if __name__ == "__main__":
    print(compute())