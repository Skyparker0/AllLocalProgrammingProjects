# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 13:12:07 2021

@author: batte
"""

#Image Filter Thing 

from PIL import Image
import numpy as np
import random
import noise



def splotch(inputImage,time):
    inputImage = inputImage.convert("HSV").resize(np.array(inputImage.size)//3)
    width = inputImage.size[0]
    height = inputImage.size[1]
    outputImage = Image.new("HSV",inputImage.size)
    
    for x in range(width):
        for y in range(height):
            h,s,v = inputImage.getpixel((x,y))
            noiseV = round(noise.pnoise3(x/(width/10), y/(height/10),time/100)*255)
            outputImage.putpixel((x,y),(0,0,64*round(((v-noiseV))/64)))#(0,0,0) if v < noiseV else (0,0,255))
    ###ChangeImageHere###
    return outputImage.resize(np.array(inputImage.size)*3)

img = Image.open("Cool Projects\ImageToText\sketch.JPG")
splotch(img,10).show()
