# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 08:47:45 2022

@author: batte
"""

#P100

# import math

# t = 10**12

# while True:
#     # x = t*(t-1)
#     # b = (1 + math.sqrt(1+2*x))/2
#     # if int(b) == b and 2*(b*(b-1)) == x:
#     #     print(b)
#     #     break

#     lower = math.floor(0.7071067811859 * t)
#     higher = math.ceil(0.707106781186694 * t)
    
#     x = t*(t-1)
    
#     for b in range(lower,higher+1):
#         if 2*(b*(b-1)) == x:
#             print(b)
#             break
    
    
#     t += 1


##############TAKEN SOLUTION FROM https://www.mathblog.dk/project-euler-100-blue-discs-two-blue/

b = 15
t = 21 
while t<10**12:
    b,t = 3 * b + 2 * t - 2, 4 * b + 3 * t - 3
print(b)