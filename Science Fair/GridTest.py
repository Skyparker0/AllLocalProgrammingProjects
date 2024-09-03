# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 08:42:39 2020

@author: batte
"""

import matplotlib.pyplot as plt
import math
import numpy as np

def rgb_to_hex(rgb):
    hexCode = '#'
    for val in rgb:
        hexCode += hex(val)[2:]
    return hexCode

x = list(range(0,1000))
y = list(map(lambda i: i*(math.sin(i/10)), x))
#z = [255 * i//1000 for i in range(0,1000)]

#z = np.array([1,0]*500)
colors = np.array(["black", "green"])
plt.scatter(x,y, c=colors[x])

##plt.scatter(x,y, c=(['#' + hex(i)[2:] +'0000' for i in z]))

plt.xlabel('x')
plt.ylabel('y')

plt.show()