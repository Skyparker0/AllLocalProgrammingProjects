# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 06:53:55 2022

@author: batte
"""

#mandlebrot set
import PIL.Image as Image
import math
import time
import random

import os

# get the directory path of the current python file
my_path = os.path.dirname(__file__)

class Complex:
    
    def __init__(self, real, imaginary):
        self.a = real
        self.b = imaginary
        
    def __str__(self):
        return str(self.a) + ("+" if self.b >= 0 else "") + str(self.b) + "i"
    
    def __add__(self,other):
        newComplex = Complex(self.a+other.a, self.b+other.b)
        return newComplex
    
    def __mul__(self,other):
        a,b,c,d = self.a,self.b,other.a,other.b
        newComplex = Complex(a*c - b*d, a*d + b*c)
        return newComplex
    
    def __abs__(self):
        # distance from (0,0)
        return math.sqrt(self.a*self.a + self.b*self.b)


def inSet(complexNum, iterations=20):
    currNum = complex(0,0)
    
    for i in range(iterations):
        currNum *= currNum
        currNum += complexNum
        if abs(currNum) > 2:
            return i
        
    return -1

startTime = time.time()

WIDTH, HEIGHT = [1920,1080]
ITERATIONS = 100

colorMap = [tuple(random.randint(0,255) for i in range(3)) for x in range(ITERATIONS)]
colorMap = [tuple(int(255/ITERATIONS * x) for i in range(3)) for x in range(ITERATIONS)]

startR,midI = -3.5,0
iSpread = 2.5
rSpread = iSpread * WIDTH/HEIGHT

manSet = Image.new("RGB",(WIDTH,HEIGHT),color=(255,0,255))

#Put Pixels
for px in range(WIDTH):
    for py in range(HEIGHT):
        a = startR + rSpread * px/WIDTH
        b = (midI + iSpread * py/HEIGHT - iSpread/2)
        
        complexPixel = complex(a,b)
        
        setValue = inSet(complexPixel,iterations = ITERATIONS) #True or int
        if setValue == -1:
            color = (0,0,0)
        else:
            color = colorMap[setValue]#tuple([round(255 - setValue*(255/ITERATIONS) % 256)]*3)
            
        manSet.putpixel((px,py),color)
        
        
endTime = time.time()

print("Width {}, Height {}, Iterations {},\nTook {} seconds to render".format(
    WIDTH,HEIGHT,ITERATIONS, endTime-startTime))

manSet.show()
manSet.save(my_path + "/Renders/manSet_W{}_H{}_Itr{}".format(WIDTH,HEIGHT,ITERATIONS)+".png")