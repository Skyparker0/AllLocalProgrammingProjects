# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 06:50:15 2023

@author: batte
"""

#Pythagorean prisms

import math


#a: The shorter leg on the basen shortest in prism
#b: The longer leg on the base, largest sl in prism
#h: height of the prism, between a and b

'''Strategy: Choose b, starting at 4, going to a large number
Take a from 3 -> b-1, seeing if any value works.
If a&b are a triple, start h at a+1 and go to b-1
'''


# for b in range(4, 100000):
#     for a in range(3,b):
        
#         abC = math.sqrt(a*a + b*b)
        
#         if int(abC) == abC:
#             #base is triple
            
#             for h in range(a+1,b):
#                 ahC = math.sqrt(a*a + h*h)
                
#                 if int(ahC) == ahC:
#                     #one side is triple
#                     bhC = math.sqrt(b*b + h*h)
#                     if int(bhC) == bhC:
#                         #both sides are triple
#                         print(a,h,b)

for b in range(4, 100000):
    for a in range(3,b):
        
        abC = math.sqrt(a*a + b*b)
        
        if int(abC) == abC:
            #base is triple
            
            for h in range(a+1,b):
                diag = math.sqrt(abC*abC + h*h)
                
                if int(diag) == diag:
                    #one side is triple
                    print(abC,h,diag)