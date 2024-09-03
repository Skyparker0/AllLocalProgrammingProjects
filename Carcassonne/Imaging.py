# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 17:55:17 2020

@author: batte
"""

'''File search'''

import os
from PIL import Image


def find_all(path, firstletters = ''):
    '''
    path = The path to the folder containing the files wanted
    firstletters = int or a string containing int
    
    returns a list of file's (paths and names) in a path that have names starting 
    with firstletters '''
    
    
    result = []
    names = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.startswith(str(firstletters)):
                result.append(os.path.join(root, name))
                names.append(name)
    return result, names

tilePaths, names = find_all('C:/Users/batte/OneDrive/_Parker/Python/Carcassonne/RealTilepics')

newImg = Image.new('RGB', (50*len(tilePaths), 50))

xPos = 0

for img in tilePaths:
    tile = Image.open(img)
    tile = tile.resize((50,50))
    tile = tile.rotate(0)
    newImg.paste(tile,(xPos,0))
    xPos += 50
    
newImg.show()
