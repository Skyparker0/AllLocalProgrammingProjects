# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 08:07:34 2021

@author: batte
"""

string = ""
for i in range(1,1000001):
    string += str(i)
nums = [string[10 ** x - 1] for x in range(7)]
prod = 1
for num in nums:
    prod *= int(num)
print(prod)