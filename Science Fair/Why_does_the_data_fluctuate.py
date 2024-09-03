# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 17:34:47 2020

@author: batte
"""

import matplotlib.pyplot as plt
import math

x = list(range(1,100))
#y = [1000//i * i for i in x]

y = [math.log(i,2) for i in x]

plt.plot(x,y)
plt.ylim(ymin=0)
plt.grid()
plt.show()