# -*- coding: utf-8 -*-
"""
Created on Tue May 25 15:12:33 2021

@author: batte
"""

import turtle as tu

t = tu.Turtle()

wn = tu.Screen

t.speed(0)

def ser_tri(depth,size,turtle):
    if depth == 1:
        for i in range(3):
            turtle.forward(size)
            turtle.left(120)
    else:
        ser_tri(depth-1, size//2,turtle)
        
        turtle.forward(size//2)
        ser_tri(depth-1, size//2,turtle)
        
        turtle.left(120)
        turtle.forward(size//2)
        turtle.left(-120)
        ser_tri(depth-1, size//2,turtle)
        
        turtle.left(-120)
        turtle.forward(size//2)
        turtle.left(120)


for i in range(1000):
    
    t.goto(i%100,i//10)
t.goto(0,0)
# ser_tri(1,100,t)
    
tu.bye()