# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 08:13:24 2021

@author: batte
"""

#Timer

import time

def timer(function,values):
    st = time.time()
    for value in values:
        a = function(value)
    et = time.time()
    return et-st