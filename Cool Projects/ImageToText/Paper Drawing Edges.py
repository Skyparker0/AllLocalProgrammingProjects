# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 08:06:56 2021

@author: batte
"""

from PIL import Image

def baseFilter(inputImage):
    inputImage = inputImage.convert("HSV")
    width = inputImage.size[0]
    height = inputImage.size[1]
    outputImage = Image.new("HSV",inputImage.size)
    ###ChangeImageHere###
    return outputImage


def edgeFilter(inputImage):
    width = inputImage.size[0]
    height = inputImage.size[1]
    outputImage = Image.new("RGB",inputImage.size,(255,255,255))
    
    tolerance =10
    
    oldRGB = (255,255,255)
    for y in range(height):
        for x in range(width):
            r,g,b = inputImage.getpixel((x,y))
            if max([abs(oldRGB[i]-(r,g,b)[i]) for i in range(3)]) > tolerance:
                outputImage.putpixel((x,y), (0,0,0))
            oldRGB = (r,g,b)
         
    oldRGB = (255,255,255)
    for x in range(width):
        for y in range(height):
            r,g,b = inputImage.getpixel((x,y))
            if max([abs(oldRGB[i]-(r,g,b)[i]) for i in range(3)]) > tolerance:
                outputImage.putpixel((x,y), (0,0,0))
            oldRGB = (r,g,b)
    
    return outputImage

def lineFilter(inputImage):
    width = inputImage.size[0]
    height = inputImage.size[1]
    outputImage = Image.new("RGB",inputImage.size)
    
    for y in range(height):
        for x in range(width):
            r,g,b = inputImage.getpixel((x,y))
            if (r+g+b)/3 < 150:
                outputImage.putpixel((x,y), (0,0,0))
            else:
                outputImage.putpixel((x,y), (255,255,255))
            
    
    return outputImage

def blackAndWhiteFilter(inputImage):
    outputImage = Image.new("HSV", inputImage.size)
    for y in range(inputImage.size[1]):
        for x in range(inputImage.size[0]):
            h,s,v = inputImage.getpixel((x,y))
            if v < 180:
                outputImage.putpixel((x,y), (0,0,0))
            else:
                outputImage.putpixel((x,y), (0,0,255))
    return outputImage




img = Image.open("Cool Projects\ImageToText\sketch.JPG")
edgeFilter(img).show()