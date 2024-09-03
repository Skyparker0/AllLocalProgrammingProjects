# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 18:31:25 2020

@author: batte
"""

from PIL import Image
import noise
import random

newImage = Image.new("RGBA", (255,255))

zoom = 50
baseZ = 1
zChange = 0

for x in range(newImage.size[0]):
    for y in range(newImage.size[1]):
        pixColor = []
        
        for layer in range(4):
            c = noise.pnoise3(x/zoom,y/zoom,baseZ + zChange*layer)
            c = round((c+1)/2 * 255)
            pixColor.append(c)
        
        
        newImage.putpixel((x,y),tuple(pixColor))
        
        
        
newImage.show()


filePath = "C:/Users/batte/OneDrive/_Parker/Python/Carcassonne/Image Examples/15X15_Fog_Test.PNG"

targetImage = Image.open(filePath)
#targetImage = targetImage.resize((255,255))
# testAlpha = Image.new("RGBA",(255,255), (0,0,0,127))

newImage = newImage.resize(targetImage.size)

targetImage.paste(newImage,(0,0),newImage)

targetImage.show()