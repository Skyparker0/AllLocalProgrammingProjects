# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 08:35:12 2021

@author: batte
"""

#P80

from decimal import Decimal,getcontext


def root_sum(num):
    getcontext().prec = 103
    rootStr = str(Decimal(num).sqrt()).replace(".","")[:100]
    return sum([int(i) for i in rootStr]) if len(rootStr) == 100 else 0

print(sum([root_sum(x) for x in range(1,101)]))