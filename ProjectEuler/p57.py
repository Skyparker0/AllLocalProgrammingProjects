# -*- coding: utf-8 -*-
"""
Created on Tue May 18 07:41:29 2021

@author: batte
"""

#P57


def rootTwo2(depth):
    frac = (1,1)
    for i in range(depth):
        numer,denom = frac
        frac = (denom + numer + denom, numer + denom)
    return frac

def special(depth):
    numer,denom = rootTwo2(depth)
    return len(str(numer)) > len(str(denom))


specials = sum([1 for i in range(1,1001) if special(i)])

print(specials)

# evaledFracs = {(1,1,2) : (3,2),
#                 (2,1,2) : (5,2)}

# def evalFrac(adder,numer,denom):
#     if (adder, numer, denom) in evaledFracs:
#         return evaledFracs[(adder,numer,denom)]
    
#     if type(denom) == tuple and len(denom) == 3:
#         a,n,d = denom
#         newDenom = evalFrac(a,n,d)
#     else:
#         newDenom = denom
    
#     newDenom = newDenom[0] / newDenom[1]
#     newNumer = float(numer)
    
#     oldDenom = float(newDenom)
#     oldNumer = float(numer)
#     multiplier = 1
    
#     while int(newDenom) != round(newDenom,3):
#         multiplier += 1
#         newDenom = oldDenom * multiplier
#         newNumer = oldNumer * multiplier
        
#     createdFraction = (int(newNumer + adder * newDenom), int(newDenom))
#     evaledFracs[(adder,numer,denom)] = createdFraction
    
#     return createdFraction
    


# def rootTwo(depth):
#     denom = 2
#     print(denom)
#     for i in range(depth-1):
#         denom = evalFrac(2,1,denom)
#         print(denom)
        
#     return evalFrac(1, 1, denom)


# for i in range(1,1001):
#     print(rootTwo(i))