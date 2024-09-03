# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 17:41:00 2021

@author: batte
"""

###Filters

from PIL import Image
import numpy as np
import random

COMPRESSION_FACTOR = 1

def baseFilter(inputImage):
    inputImage = inputImage.convert("HSV")
    width = inputImage.size[0]
    height = inputImage.size[1]
    outputImage = Image.new("HSV",inputImage.size)
    ###ChangeImageHere###
    return outputImage

def downscaleFilter(inputImage,divisor):
    outputImage = inputImage.resize(np.array(inputImage.size)//divisor)
    return outputImage


def upscaleFilter(inputImage,multiplier):
    outputImage = inputImage.resize(np.array(inputImage.size) * multiplier, Image.NEAREST)
    return outputImage


def pixelateFilter(inputImage,divisor):
    return upscaleFilter(downscaleFilter(inputImage,divisor),divisor)

def blackAndWhiteFilter(inputImage):
    smallImage = downscaleFilter(inputImage,COMPRESSION_FACTOR).convert("HSV")
    outputImage = Image.new("HSV", smallImage.size)
    for y in range(smallImage.size[1]):
        for x in range(smallImage.size[0]):
            h,s,v = smallImage.getpixel((x,y))
            outputImage.putpixel((x,y), (0,0,v))
    return upscaleFilter(outputImage,COMPRESSION_FACTOR)
            
def tintFilter(inputImage):
    smallImage = downscaleFilter(inputImage,COMPRESSION_FACTOR).convert("HSV")
    outputImage = Image.new("HSV", smallImage.size)
    for y in range(smallImage.size[1]):
        for x in range(smallImage.size[0]):
            h,s,v = smallImage.getpixel((x,y))
            darkTint = 0#-round(abs(100 + x - smallImage.size[0]//2) ** 0.5 * abs(100 + y - smallImage.size[1]//2) ** 0.5)
            outputImage.putpixel((x,y), (100,1000,300-v + darkTint))
    return upscaleFilter(outputImage,COMPRESSION_FACTOR)


def comicBookFilter(inputImage):
    ###
    def HUECHART(hsv):
        hue,saturation,value = h,s,v
        
        return (hue//10 * 10, 300, value//100 * 100)
        
        if hue < 100:
            return (0,300,255)
        elif hue < 200:
            return (100,300,100)
        elif hue < 300:
            return (200,300,255)
        elif hue < 400:
            return (300,300,255)
    ###
    smallImage = downscaleFilter(inputImage,COMPRESSION_FACTOR).convert("HSV")
    outputImage = Image.new("HSV", smallImage.size)
    for y in range(smallImage.size[1]):
        lastHue = None
        for x in range(smallImage.size[0]):
            h,s,v = smallImage.getpixel((x,y))
            
            # if lastHue != None and abs(lastHue - h) > 20:
            #     outputImage.putpixel((x,y), (0,0,0))
            # else:
            #     outputImage.putpixel((x,y), (h,s,v))
            
            outputImage.putpixel((x,y), HUECHART(h))
            
                
            lastHue = h
    return upscaleFilter(outputImage,COMPRESSION_FACTOR)

def comicBookRGBFilter(inputImage):
    ###
    def COLORCHART(rgb):
        r,g,b = rgb
        DIVIDE = 30
        return r//DIVIDE * DIVIDE, g//DIVIDE * DIVIDE, b//DIVIDE * DIVIDE
    ###
    smallImage = downscaleFilter(inputImage,COMPRESSION_FACTOR).convert("RGB")
    outputImage = Image.new("RGB", smallImage.size)
    for y in range(smallImage.size[1]):
        lastColor = None
        for x in range(smallImage.size[0]):
            r,g,b = smallImage.getpixel((x,y))
            
            # if lastHue != None and abs(lastHue - h) > 20:
            #     outputImage.putpixel((x,y), (0,0,0))
            # else:
            #     outputImage.putpixel((x,y), (h,s,v))
            
            # avgColor = (r,g,b) if lastColor == None else \
            # tuple((np.array((r,g,b)) + np.array(lastColor)) // 2)
            
            outputImage.putpixel((x,y), COLORCHART((r,g,b)))
            lastColor = (r,g,b)
    return upscaleFilter(outputImage,COMPRESSION_FACTOR)

def ditherFilter(inputImage):
    random.seed(0)
    smallImage = downscaleFilter(inputImage,COMPRESSION_FACTOR).convert("HSV")
    outputImage = Image.new("RGB", smallImage.size, (255,255,255))
    for lowerlimit in range(0,255,10):
        for i in range(int(1000 * (1.5- lowerlimit/255))):
            #RANDOM PIXEL, CHECK BRIGHTNESS
            x, y = random.randint(0, smallImage.size[0] - 1), random.randint(0, smallImage.size[1] - 1)
            h,s,v = smallImage.getpixel((x,y))
            if v < lowerlimit:
                outputImage.putpixel((x,y), (v,) * 3)
    return upscaleFilter(outputImage,COMPRESSION_FACTOR)


def edgeFilter(inputImage):
    smallImage = downscaleFilter(inputImage,COMPRESSION_FACTOR)
    width = smallImage.size[0]
    height = smallImage.size[1]
    outputImage = Image.new("RGB",smallImage.size,(255,255,255))
    
    tolerance =10
    
    oldRGB = (255,255,255)
    for y in range(height):
        for x in range(width):
            r,g,b = smallImage.getpixel((x,y))
            if max([abs(oldRGB[i]-(r,g,b)[i]) for i in range(3)]) > tolerance:
                outputImage.putpixel((x,y), (0,0,0))
            oldRGB = (r,g,b)
         
    oldRGB = (255,255,255)
    for x in range(width):
        for y in range(height):
            r,g,b = smallImage.getpixel((x,y))
            if max([abs(oldRGB[i]-(r,g,b)[i]) for i in range(3)]) > tolerance:
                outputImage.putpixel((x,y), (0,0,0))
            oldRGB = (r,g,b)
    
    return upscaleFilter(outputImage,COMPRESSION_FACTOR)


