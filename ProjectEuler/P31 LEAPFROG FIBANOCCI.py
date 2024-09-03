# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 08:06:20 2021

@author: batte
"""
### LEAPFROG FIBANOCCI
def ways(number):
    if number == 0:
        return 1
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    valsToCheck = [number - coin for coin in coins if number - coin >= 0]
    return sum([ways(target) for target in valsToCheck])