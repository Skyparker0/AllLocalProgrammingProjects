# -*- coding: utf-8 -*-
"""
Created on Sat May 15 07:57:53 2021

@author: batte
"""

import random

class Tester(object):
    
    def __init__(self):
        self.level = 1
        
    def set_level(self,newLevel):
        self.level = newLevel
        
    def multiplication_fact(self):
        a = random.randint(1,int(self.level) * 5)
        b = random.randint(1,int(self.level) * 2)
        
        answer = ""
        while True:
            answer = input("What is " + str(a) + " * " + str(b) + ": ")
            
            try:
                answer = int(answer)
                break
            except ValueError:
                continue
        
        if answer == a*b:
            print("Correct")
            self.level += 0.1
        else:
            print("Incorrect")
            self.level -= 0.1
            self.level = max(0.5,self.level)

t = Tester()

while True:
    t.multiplication_fact()
        