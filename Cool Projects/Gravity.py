# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:51:41 2020

@author: batte
"""

###Gravity Simulation

import numpy as np
import pygame
import sys

class universe:
    '''Holds Space objects'''

    def __init__(self, objectPositions, objectVelocities, objectMasses, surface):
        '''
        objectPositions holds the places where objects start,
        objectVelocities holds their initial velocities, and 
        objectMasses holds their masses
        '''
        
        self.bigG = 6.67 * 10**-2 
        
        self.objects = []
        for i in range(len(objectPositions)):
            self.objects.append(spaceObject(objectMasses[i], objectVelocities[i], objectPositions[i], self))
            
        self.surface = surface
            
    def tick(self, timeFactor):
        '''Ticks through all objects, updates their velocities and positions, and draws them'''
        global cameraPosition
        
        for spaceOb in self.objects:
            spaceOb.update_velocity(self.objects,timeFactor)        
         
        cameraPosition = (0,0)
        #cameraPosition = self.objects[1].position() - 350
        cameraPosition = np.array(cameraPosition) + cameraOffset
        
        for spaceOb in self.objects:
            spaceOb.update_position(timeFactor)
            spaceOb.draw(self.surface)
            
    def create_planet(self, mass, startVelocity, position):
        '''Creates a new space object with the args'''
        
        self.objects.append(spaceObject(mass, startVelocity, position, self))


class spaceObject:
    '''Has a mass, starting velocity, and current velocity'''
    
    def __init__(self, mass, startVelocity, coord, master):
        '''Takes in
        mass - how heavy/large the planet is.
        startVelocity - the starting velocity of the object
        coord - where the planet begins '''
        self.mass = mass
        self.currentVelocity = np.array(startVelocity)
        self.coord = np.array(coord)
        self.master = master
        
        self.color = [np.random.randint(255) for i in range(3)]
        
    def position(self):
        return self.coord
    
    def velocity(self):
        return self.currentVelocity
    
    def mass(self):
        return self.mass
    
    def distance(self, other):
        myPos = np.array(self.position())
        otPos = np.array(other.position())
        return np.sqrt(sum((myPos-otPos)**2)) +1
    
    def force_dir(self,other):
        myPos = np.array(self.position())
        otPos = np.array(other.position())
        vector2 = otPos - myPos
        dist = self.distance(other)
        vector2 = vector2/dist
        return list(vector2)
        
    def update_velocity(self, allObjects, timeFactor):
        for spaceOb in allObjects:
            if spaceOb is self:
                continue
            distanceSquared = self.distance(spaceOb)
            forceDir = np.array(self.force_dir(spaceOb))
            force = forceDir * self.master.bigG * self.mass * spaceOb.mass / distanceSquared
            # if self.distance(spaceOb) < np.sqrt(spaceOb.mass):
            #     force *= -1
            acceleration = force/self.mass
            self.currentVelocity = self.currentVelocity + acceleration * timeFactor
            
            
    def update_position(self, timeFactor):
        self.coord = self.coord + self.velocity()*timeFactor
        
    def draw(self, surface):
        drawPos = [int((self.coord[x] - cameraPosition[x] - 350)//cameraDist) + 350 for x in range(2)]
        #min(255,abs(int(round(np.prod(self.velocity())))))
        pygame.draw.circle(surface, self.color, drawPos, int(round(np.sqrt(self.mass)/cameraDist)))
        

def simulate(screen):
    #objectPositions, objectVelocities, objectMasses, surface
    objectPositions = [(350,350)]#,(350,350)]#, (100,100),(600,600)] 
    objectVelocities = [(0,0)]#,(0,0)]#,(-10,-40),(20,-30)]
    objectMasses = [4000]#,4000]#,50,500]
    surface = screen
    
    # global cameraPosition
    global cameraDist
    global cameraOffset
    # cameraPosition = [0,0]
    cameraDist = 1
    cameraOffset = [0,0]
    
    newMass = 100
    mousePositionStart = None
    mousePositionStartMass = None
    paused = False
    
    uni = universe(objectPositions, objectVelocities, objectMasses, surface)
    
    while True:
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         cameraOffset[0] -= 50
            #     if event.key == pygame.K_RIGHT:
            #         cameraOffset[0] += 50
            #     if event.key == pygame.K_UP:
            #         cameraOffset[1] -= 50
            #     if event.key == pygame.K_DOWN:
            #         cameraOffset[1] += 50
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 5:
                    cameraDist = min(cameraDist + cameraDist/10, 10)

                elif event.button == 4:
                    cameraDist = max(cameraDist - cameraDist/10, 0.4)
                
                   
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousePositionStart = pygame.mouse.get_pos()
                mousePositionEnd = None
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mousePositionEnd = pygame.mouse.get_pos()
                
                uni.create_planet(newMass, (np.array(mousePositionEnd)-np.array(mousePositionStart))*cameraDist/5, np.array(cameraPosition) + 350 + (np.array(mousePositionStart)-350) * cameraDist)
                mousePositionStart = None
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button in [2,3]:
                mousePositionStartMass = pygame.mouse.get_pos()
                mousePositionEndMass = None
            elif event.type == pygame.MOUSEBUTTONUP and event.button in [2,3]:
                mousePositionEndMass = pygame.mouse.get_pos()
                #newMass = (sum((np.array(mousePositionEndMass)-np.array(mousePositionStartMass))**2))
                mousePositionStartMass = None

        surface.fill((0,0,0))
        uni.tick(0.5 if not paused else 0)
        
        if mousePositionStart != None:
            pygame.draw.circle(surface, (100,100,100), mousePositionStart, int(round(np.sqrt(newMass)/cameraDist)))
            pygame.draw.line(surface, (100,0,0), mousePositionStart, pygame.mouse.get_pos(), 3)
            
        if mousePositionStartMass != None:
            mousePositionEndMass = pygame.mouse.get_pos()
            newMass = cameraDist*cameraDist*(sum((np.array(mousePositionEndMass)-np.array(mousePositionStartMass))**2))
            pygame.draw.circle(surface, (50,50,50), mousePositionStartMass, int(round(np.sqrt(newMass)/cameraDist)))
            pygame.draw.line(surface, (0,0,100), mousePositionStartMass, pygame.mouse.get_pos(), 3)
            
        pygame.display.flip()
        
        clock.tick(30)
        
        keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[pygame.K_UP]:
            cameraOffset[1] -=  50* cameraDist/3
        if keys[pygame.K_DOWN]:
            cameraOffset[1] += 50* cameraDist/3
        if keys[pygame.K_LEFT]:
            cameraOffset[0] -=  50* cameraDist/3
        if keys[pygame.K_RIGHT]:
            cameraOffset[0] += 50 * cameraDist/3
        if keys[pygame.K_SPACE] and not wait:
            paused = not paused
            wait = True
        if not keys[pygame.K_SPACE]:
            wait = False
pygame.init()
screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()

# clock.tick(0.5)
simulate(screen)
pygame.quit()