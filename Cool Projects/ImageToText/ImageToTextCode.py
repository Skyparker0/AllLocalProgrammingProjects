# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 14:55:19 2021

@author: batte
"""
from PIL import Image
import random
import numpy as np

img = Image.open("Cool Projects\ImageToText\Test_Image_Me.jpg")

TEXT_CHARACTERS = """ .:-=+*#%@"""   #least to most bright

def alter_image(inputImage):
    width = inputImage.size[0]
    height = inputImage.size[1]
    outputImage = Image.new("HSV",inputImage.size)
    inputImage = inputImage.convert("HSV")
    for x in range(width):
        for y in range(height):
            h,s,v = inputImage.getpixel((x,y))
            outputImage.putpixel((x,y), (0,0,v))
    return outputImage

def alter_image_to_text(inputImage, shrinkAmm):
    inputImage = inputImage.convert("HSV").resize(np.array(inputImage.size)//shrinkAmm)
    width = inputImage.size[0]
    height = inputImage.size[1]
    outputImage = ""
    for y in range(height):
        for x in range(width):
            h,s,v = inputImage.getpixel((x,y))
            outputImage += " " + TEXT_CHARACTERS[-round(v/255 * len(TEXT_CHARACTERS))] 
        outputImage += "\n"
    return outputImage

if __name__ == "__main__":
    print(alter_image_to_text(img,20))
    
    #alter_image(img).show()