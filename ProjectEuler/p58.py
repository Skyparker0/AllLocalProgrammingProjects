# -*- coding: utf-8 -*-
"""
Created on Fri May 21 07:32:00 2021

@author: batte
"""

#p58

# def diagonals(sideLength):
#     num = 1
#     diagList = [1]
    
#     for addr in range(1,(sideLength-1)//2 + 1):
#         for i in range(4):
#             num += addr*2
#             diagList.append(num)
    
#     return diagList

def is_prime(x):
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, int(x**0.5) + 1, 2):
			if x % i == 0:
				return False
		return True
    
sideLength = 3

diags = 5
primes = 3

number = 9

while primes/diags > 0.1:
    sideLength += 2
    diags += 4
    
    for i in range(4):
        number += sideLength-1
        if is_prime(number):
            primes += 1
    
print(sideLength)