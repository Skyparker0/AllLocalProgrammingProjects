# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 08:20:38 2021

@author: batte
"""

### 48

digits = 000000000000

for x in range(1, 1001):
    digits += int(str(x**x)[-10:])
    
print(str(digits)[-10:])