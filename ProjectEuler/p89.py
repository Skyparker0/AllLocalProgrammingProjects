# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 09:46:13 2021

@author: batte
"""

#P89

romanNumerals = []
with open("non-code-files/p089_roman.txt") as handle:
    for line in handle:
        romanNumerals.append(line.strip("\n"))


Rconversion = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000}

def roman_to_normal(roman):
    total = 0
    
    for index,character in enumerate(roman):
        charVal = Rconversion[character]
        
        if any(Rconversion[nextLetter] > charVal for nextLetter in roman[index+1:]):
            total -= charVal
        else:
            total += charVal
            
    return total
    

Nconversion = {
    0:"",
    1:"I",
    2:"II",
    3:"III",
    4:"IV",
    5:"V",
    6:"VI",
    7:"VII",
    8:"VIII",
    9:"IX",
    10:"X",
    20:"XX",
    30:"XXX",
    40:"XL",
    50:"L",
    60:"LX",
    70:"LXX",
    80:"LXXX",
    90:"XC",
    100:"C",
    200:"CC",
    300:"CCC",
    400:"CD",
    500:"D",
    600:"DC",
    700:"DCC",
    800:"DCCC",
    900:"CM",
    1000:"M",
    2000:"MM",
    3000:"MMM",
    4000:"MMMM",
    }

def normal_to_roman(num):
    string = ""
    numStr = str(num)
    for index,digit in enumerate(numStr):
        string += Nconversion[int(digit + '0' * (len(numStr)-index-1))]
    return string

savedCharacters = 0

for roman in romanNumerals:
    realNumber = roman_to_normal(roman)
    betterRomanNumber = normal_to_roman(realNumber)
    savedCharacters += len(roman)-len(betterRomanNumber)
    
print(savedCharacters)