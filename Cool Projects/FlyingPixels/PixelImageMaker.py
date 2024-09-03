# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 07:37:08 2020

@author: batte
"""

import numpy as np
import pygame
from PIL import Image
import sys

class flyingPixel(object):
    maxSpeed = 50
    maxForce = .2
    mouseDist = 1#100
    
    def __init__(self,desiredx,desiredy,startx,starty,color,size):
        self.desX, self.desY, self.x, self.y, self.color, self.size = desiredx,desiredy,startx,starty,color,size
        self.velocity = np.array([0,0])
        self.acceleration = np.array([0,0])
        
    def get_color(self):
        return self.color
        
    def set_desired(self,x,y):
        self.desX, self.desY = x,y
        
    def appForce(self,force):
        self.acceleration = np.float32(self.acceleration) + np.float32(force)
        
    def arrive(self):
        desired = np.array([self.desX,self.desY]) - np.array([self.x,self.y])
        dist = np.linalg.norm(desired)
        speed = flyingPixel.maxSpeed/ (800/(dist + 0.001))
        desired = desired / dist * speed
        steer = desired - self.velocity
        steer = steer / np.linalg.norm(steer) * min(flyingPixel.maxForce, np.linalg.norm(steer))
        return steer
    
    def flee(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        mouseX, mouseY = mouseX // self.size, mouseY // self.size
        desired = np.array([mouseX,mouseY]) - np.array([self.x,self.y])
        dist = np.linalg.norm(desired)
        if dist < flyingPixel.mouseDist/self.size:
            speed = flyingPixel.maxSpeed
            desired = desired / dist * speed
            desired *= -1
            steer = desired - self.velocity
            steer = steer / np.linalg.norm(steer) * min(flyingPixel.maxForce, np.linalg.norm(steer))
            return steer
        else:
            return np.array([0,0])
        
    def behaviors(self):
        arriveForce = self.arrive()
        fleeForce = self.flee()
        
        self.appForce(arriveForce)
        self.appForce(fleeForce)
        
    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.velocity = np.float32(self.velocity) + np.float32(self.acceleration)
        self.acceleration *= 0
        
    def show(self,surface):
        #print(self.color,(int(self.x * self.size),int(self.y * self.size)), self.size)
        pygame.draw.circle(surface,self.color,(int(self.x * self.size),int(self.y * self.size)), self.size//2)
        #pygame.draw.rect(surface,self.color,(int(self.x * self.size),int(self.y * self.size), self.size, self.size))






imDirectory = "Test_My_Face"
imOne = Image.open(imDirectory)
imOne.convert("RGB")
width = imOne.size[0]
height = imOne.size[1]
pixelRatio = 10

smallimage1 = imOne.resize((width//pixelRatio, height//pixelRatio), Image.BILINEAR)
smallwidth = smallimage1.size[0]
smallheight = smallimage1.size[1]
smallimage1Data = smallimage1.getdata()

imDirectory2 = "Test_My_Face_3"


flyingPixels = []
for x in range(smallwidth):
    for y in range(smallheight):
        flyingPixels.append(flyingPixel(x,
                                        y,
                                        np.random.rand() * smallwidth,
                                        np.random.rand() * smallheight, 
                                        smallimage1Data[x + y*smallwidth],
                                        pixelRatio))
        
        
def tick(pixels,surface):
    for pix in pixels:
        pix.behaviors()
        pix.update()
        pix.show(surface)
        

def colorDif(color1, color2):
    '''calculates the difference in color between 2 tuple colors'''
    
    return sum((np.array(color1) - np.array(color2)) ** 2)

def closestColor(color, imageData):
    bestIndex = 0
    smallestDif = 200000
    for index, imgColor in enumerate(imageData):
        dif = colorDif(color, imgColor)
        if dif < 300:
            return index
        if dif < smallestDif:
            smallestDif = dif
            bestIndex = index
            
    return bestIndex

def imageSwap(flyingPixels, imageDirectory):
    im = Image.open(imageDirectory)
    im.convert("RGB")
    smallim = im.resize((width//pixelRatio, height//pixelRatio), Image.BILINEAR)
    smallimData = list(smallim.getdata())
    for pixel in flyingPixels:
        indexChosen = closestColor(pixel.get_color(),smallimData)
        smallimData[indexChosen] = (1000,1000,1000) # so the same position cant be chosen again
        pixel.set_desired(indexChosen%smallwidth, indexChosen//smallwidth)

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
        
while True:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        
    screen.fill((0,0,0))
    tick(flyingPixels, screen)
    pygame.display.flip()
    clock.tick(40)
    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_SPACE]:
        imageSwap(flyingPixels, imDirectory2)