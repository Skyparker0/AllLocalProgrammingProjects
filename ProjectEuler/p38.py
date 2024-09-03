# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 07:38:29 2021

@author: batte
"""

for x in range(10001,1000, -1):
    if all([number in str(x) + str(x*2) for number in "123456789"]):
        biggest = str(x) + str(x*2)
        break
print(biggest)