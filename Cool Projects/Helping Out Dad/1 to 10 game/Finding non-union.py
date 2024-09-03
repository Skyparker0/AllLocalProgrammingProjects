# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 19:43:44 2022

@author: batte
"""

noDoubles = []

with open("C:/Users/batte/OneDrive/_Parker/Python/Cool Projects/Helping Out Dad/1 to 10 game/Solutions 1-10.txt") as handle:
    for line in handle:
        noDoubles.append(line.strip("\n"))

doublesAndSingles = []

with open("C:/Users/batte/OneDrive/_Parker/Python/Cool Projects/Helping Out Dad/1 to 10 game/Solutions 1-10 no 0, Doubles.txt") as handle:
    for line in handle:
        doublesAndSingles.append(line.strip("\n"))
        
onlyDoublesAndSingles = [x for x in doublesAndSingles if x not in noDoubles]