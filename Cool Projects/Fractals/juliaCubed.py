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

def inSet(complexNum, startingComplex, iterations=20):
    currNum = startingComplex
    
    for i in range(iterations):
        currNum *= currNum * currNum
        currNum += complexNum
        if abs(currNum) > 2:
            return i
        
    return -1

startTime = time.time()

WIDTH, HEIGHT = [1920,1080]
ITERATIONS = 100
CONSTANT = complex(-0.3, -0.6)

colorMap = [((29 + 79 * x)%256,(61 - 13 * x)%256,(11 + 31 * x)%256) for x in range(ITERATIONS)]
#[tuple(random.randint(0,255) for i in range(3)) for x in range(ITERATIONS)]

startR,midI = -2,0
iSpread = 2.5
rSpread = iSpread * WIDTH/HEIGHT

manSet = Image.new("RGB",(WIDTH,HEIGHT),color=(255,0,255))

#Put Pixels
for px in range(WIDTH):
    for py in range(HEIGHT):
        a = startR + rSpread * px/WIDTH
        b = (midI + iSpread * py/HEIGHT - iSpread/2)
        
        complexPixel = complex(a,b)
        
        setValue = inSet(CONSTANT, complexPixel, iterations = ITERATIONS) #True or int
        if setValue == -1:
            color = (0,0,0)
        else:
            color = colorMap[setValue]
            #color = tuple([round(255 - setValue*(255/ITERATIONS) % 256)]*3)
            
        manSet.putpixel((px,py),color)
        
        
endTime = time.time()

print("Width {}, Height {}, Iterations {},\nTook {} seconds to render".format(
    WIDTH,HEIGHT,ITERATIONS, endTime-startTime))

manSet.show()
manSet.save(my_path + "/Renders/juliaSetCubed_W{}_H{}_Itr{}".format(WIDTH,HEIGHT,ITERATIONS)+".png")