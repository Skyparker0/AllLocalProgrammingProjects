# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 10:47:31 2020

@author: batte
"""

'''
Perlin Notes:
    
    scale: number that determines at what distance to view the noisemap
    
    octaves: the number of levels of detail
    
    lacunarity: number that determines how much detail is added or removed at each octave
    
    persistence: number that determines how much each octave contributes to the overall shape
'''

import noise
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

shape = (100,100)
scale = 15.0
octaves = 2
persistence = 0.5
lacunarity = 2.0

world = np.zeros(shape)
for i in range(shape[0]):
    for j in range(shape[1]):
        world[i][j] = noise.pnoise2(i/scale, 
                                    j/scale, 
                                    octaves=octaves, 
                                    persistence=persistence, 
                                    lacunarity=lacunarity, 
                                    repeatx=1024, 
                                    repeaty=1024, 
                                    base=0)
        
        
#plt.imshow(world,origin='upper')

newImg = Image.new('RGB', shape)
#newImgTerrain = Image.new('RGB', shape)

for x in range(shape[0]):
    for y in range(shape[1]):
        noiseVal = world[x,y]
        
        color = int((noiseVal + 1) * 125)
        color = np.array([color]*3)
        
        stepDir = np.array([0,-1])
        position = [x,y]
        
        steps = 0
        while True:
            steps += 1
            try:
                position += stepDir
                
                if noiseVal < world[int(position[0]),int(position[1])]:
                    color = color//(2+(1/steps))
                    break
            except:
                #color = (255,255,255)
                break
       
        newImg.putpixel((x,y), tuple([int(i) for i in color]))
         

        
        #newImgTerrain.putpixel((x,y), color)
        
newImg = newImg.resize((500,500),resample=Image.NEAREST)
newImg.show()
#newImgTerrain = newImgTerrain.resize((500,500),resample=Image.NEAREST)
#newImgTerrain.show()
