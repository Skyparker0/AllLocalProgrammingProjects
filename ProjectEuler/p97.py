# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 10:11:35 2022

@author: batte
"""

#P97

# only need to keep the last ten digits of the number

number = 1

for i in range(7830457):
    number *= 2
    number %= 10000000000
    
number *= 28433
number += 1
number %= 10000000000

print(number)

#8739992577