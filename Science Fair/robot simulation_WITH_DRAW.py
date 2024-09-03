# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 14:50:34 2020

@author: batte
"""

import pygame
import random
import sys


class point:
    '''__init__(self, x, y, size, color,speed)
    A single point, most likely other classes will branch off this'''
    
    def __init__(self, x, y):
        '''The point has an x and y value, and a rounded x y value for drawing'''
        self.x = x
        self.y = y
        self.roundx = round(self.x)
        self.roundy = round(self.y)
        
    def pos(self):
        return (self.x, self.y)
    
    def dist(self, other):
        (changeX, changeY) = [other.pos()[i] - self.pos()[i] for i in [0,1]]
        return (changeX**2 + changeY**2)**0.5
    
    def round_XY(self):
        self.roundx = round(self.x)
        self.roundy = round(self.y)
        
    def round_pos(self):
        self.round_XY()
        return (self.roundx,self.roundy)
        

class all_objects:
    '''Holds all the objects'''
    
    def __init__(self, drawingSurface, numRobotsPerRocket, rocketWeightLimit, minePositions, rocketPositions, speed, carryOffset, mineResourses, miningSpeed, depositSpeed):
        '''Creates lists that hold robots, mines, and rockets/bases'''
        
        self.bases = []
        self.robots = []
        self.mines = []
        self.drawingSurface = drawingSurface
        
        ######Changeable Variables
        self.speed = speed
        self.robotCarry = rocketWeightLimit // numRobotsPerRocket - carryOffset
        self.mineResourses = mineResourses
        self.mineSpeed = miningSpeed
        self.depositSpeed = depositSpeed
        ######
        
        objectPlaceholder = None
        
        for position in rocketPositions:
            objectPlaceholder = base(self, position[0],position[1])
            self.bases.append(objectPlaceholder)    #create a base at a base position
            
            for i in range(numRobotsPerRocket):
                objectPlaceholder = robot(self,position[0],position[1],self.speed, self.robotCarry)
                self.robots.append(objectPlaceholder)
        
        for position in minePositions:
            objectPlaceholder = mine(self,position[0],position[1], self.mineResourses)
            self.mines.append(objectPlaceholder)
            
    def tick(self, visualize):
        '''Ticks all robots, and draws all objects'''
        for robot in self.robots:
            robot.tick()
        
        totalResources = 0
        goalResources = len(self.mines) * self.mineResourses
        
        for base in self.bases:
            if visualize: base.draw(self.drawingSurface)
            totalResources += base.get_stored()
        for mine in self.mines:
            if visualize: mine.draw(self.drawingSurface)
        for robot in self.robots:
            if visualize: robot.draw(self.drawingSurface)
            
        return totalResources >= goalResources


class robot(point):
    '''An object for an robot. It is a child of point, so it is easier to find positions and distances'''
    
    def __init__(self, master, x, y, speed, capacity):
        '''The robot is initialized as a point.
        master = some sort of object holding class
        x,y = the start coordinate
        speed = how fast the robot moves
        capacity = how much recources can the robot carry
        cargo = how much the robot is carying'''
        
        point.__init__(self, x,y)
        # self.x = x
        # self.y = y
        # self.roundx = round(self.x)
        # self.roundy = round(self.y)
        
        self.capacity = capacity
        self.cargo = 0
        self.speed = speed
        self.goal = None
        self.master = master
        
        
    def get_speed(self):
        return self.speed
    
    def get_cargo(self):
        return self.cargo
    
    def get_capaticy(self):
        return self.capacity
    
    def get_objective(self):
        return self.objective
    
    def get_master(self):
        return self.master
    
    def draw(self, surface):
        '''robot.draw(surface)
        surface is the pygame surface getting drawn on.
        draws a circle representing the size and cargo'''
        self.round_XY()
        pygame.draw.circle(surface, (100,100,100), (self.round_pos()), round(self.capacity**0.5))
        if self.cargo > 0:
            pygame.draw.circle(surface, (0,0,255), (self.round_pos()), round(self.cargo**0.5))
        
        # color = (100,100,100)
        # size = 1
        # if type(self.goal).__name__ == 'base':
        #     color = (0,200,0)
        #     if self.goal.line_index(self) == 0:
        #         size = 5
                
        # if type(self.goal).__name__ == 'mine':
        #     color = (200,0,0)
        #     if self.goal.line_index(self) == 0:
        #         size = 2
        
        # pygame.draw.line(surface, color, self.round_pos(), self.goal.round_pos(), size)
        
    def maxGiveTake(self):
        give = self.master.depositSpeed if self.cargo >= self.master.depositSpeed else self.cargo
        take = self.master.mineSpeed if self.cargo <= self.capacity - self.master.mineSpeed else self.capacity - self.cargo
        return (give, take)
    
    def change_cargo(self, change):
        self.cargo += change
        
    def move_closer(self, other, moveDistance, spacing):
        '''robot.move_closer(other, moveDistance, spacing)
        other = target point object
        moveDistance = the ammount the robot moves
        spacing = how much distance is kept between the robot and target
        The robot moves moveDistance pixels torwards or away from other depending on spacing.
        The robot moves itself to get to a position spacing pixels away from other.'''
        dist = self.dist(other)
        goalDist = dist - spacing
        
        if goalDist == 0 or dist == 0:
            # goalDist += 0.0001 
            # dist += 0.0001
            return 'ZeroDiv'
            
        distFraction = goalDist/dist
        xChange, yChange = [(other.pos()[i] - self.pos()[i]) * distFraction for i in [0,1]]
        
        if abs(goalDist) <= moveDistance:
            self.x += xChange
            self.y += yChange
            return self.dist(other),spacing
        
        moveFraction = moveDistance/goalDist
        
        self.x += xChange * moveFraction * (-1 if moveFraction < 0 else 1)
        self.y += yChange * moveFraction * (-1 if moveFraction < 0 else 1)
        
    
    def choose_goal(self):
        '''robot.choose_goal()
        The robot chooses either to go to a mine, or go to a base'''
        
        
        if self.cargo == self.capacity or max(mine.resources for mine in self.master.mines) == 0:    #robot is full or all mines are depleted, head to a base
            #choses the base with the least line >>> and than least distance
            allBases = self.master.bases
            minLine = min([len(base.get_line()) for base in allBases])
            bestBases = [base for base in allBases if len(base.get_line()) == minLine]
            
            bestBase = None
            bestDist = 100000000
            for base in bestBases:
                distToBase = self.dist(base)
                if distToBase < bestDist:
                    bestBase = base
                    bestDist = distToBase
                    
            self.goal = bestBase
        else:    #the robot is not yet full, and there are mines with resourses. Find a good mine
            allMines = [mine for mine in self.master.mines if mine.resources > 0]
            minLine = min([len(mine.get_line()) for mine in allMines])
            bestMines = [mine for mine in allMines if len(mine.get_line()) == minLine]
            
            bestMine = None
            bestDist = 100000000
            for mine in bestMines:
                distToMine = self.dist(mine)
                if distToMine < bestDist:
                    bestMine = mine
                    bestDist = distToMine
                    
            self.goal = bestMine
        if not max(mine.resources for mine in self.master.mines) == 0 and self.cargo == 0:    
            self.goal.add_robot(self)
        
    def tick(self):
        '''This is the big important method. This will cause the robot to 
        go wait in line at either:
            A mine, where it waits untill it is at the front of the line,
            and when it is, mines until it can't
        or:
            A base, where it waits until at the front of the line, and
            deposits it's resources'''
        minSpacing = 20 + round(self.capacity**0.5)
        lineSpacing = round(self.capacity**0.5) *2
        
        if type(self.goal).__name__ == 'base':    # If the goal is a base
        
            if not self in self.goal.get_line():    #if the robot is not yet in goal's line, get in the line
                self.goal.add_robot(self)
                
            placeInLine = self.goal.line_index(self)
            
            self.move_closer(self.goal,self.speed, minSpacing + lineSpacing*placeInLine)
            
            if placeInLine == 0:    #if at the front of the line
                #self.move_closer(self.goal,self.speed, 30 + 10*placeInLine)
                if self.dist(self.goal) < minSpacing + 1:   # if in close distance
                    giveTake = self.maxGiveTake()
                    realChange = self.goal.add_resources(giveTake[0])
                    self.change_cargo(-realChange)
                    
            if self.cargo == 0:
                self.goal.remove_robot(self)
                self.goal = None
                self.choose_goal()
                
                    
            
        elif type(self.goal).__name__ == 'mine':  # If the goal is a mine
            
            if not self in self.goal.get_line():    #if the robot is not yet in goal's line, get in the line
                self.goal.add_robot(self)
                
            placeInLine = self.goal.line_index(self)
            
            self.move_closer(self.goal,self.speed, minSpacing + lineSpacing*placeInLine)
            
            if placeInLine == 0:    #if at the front of the line
                #self.move_closer(self.goal,self.speed, 30 + 10*placeInLine)
                if self.dist(self.goal) < minSpacing + 1:   # if in close distance
                    giveTake = self.maxGiveTake()
                    realChange = self.goal.mine_resources(giveTake[1])
                    self.change_cargo(realChange)
                    
            if self.cargo == self.capacity or self.goal.resources == 0:
                self.goal.remove_robot(self)
                self.goal = None
                self.choose_goal()
                
        else:
            
            self.choose_goal()
            
                    
            
    
    
class base(point):
    '''The base/spaceship that the robots arrive in, and stores resourses collected.
    Has a line'''
    
    def __init__(self,master, x, y):
        '''Initializes a base as a point x,y'''
        point.__init__(self, x,y)
        # self.x = x
        # self.y = y
        # self.roundx = round(self.x)
        # self.roundy = round(self.y)
        self.waitLine = {}
        self.orderLine = []
        self.stored = 0
        self.master = master
        
    def get_line(self):
        return self.orderLine
    
    def get_stored(self):
        return self.stored
    
    def draw(self, surface):
        '''Draws the base'''
        pygame.draw.circle(surface, (50,50,50), self.round_pos(), 20)
        if self.stored > 0:
            pygame.draw.circle(surface, (255,0,0), self.round_pos(), \
            round(20 * (self.stored/(self.master.mineResourses * len(self.master.mines)))))
        
        # pygame.font.init()

        # myfont = pygame.font.SysFont('Comic Sans MS', 10)
        
        # textsurface = myfont.render(str(len(self.orderLine)), False, (100, 0, 0))
        
        # surface.blit(textsurface,(self.x,self.y))
        
    def add_robot(self, robot):
        '''Adds a robot to the waitline and updates the ordered line'''
        self.waitLine[robot] = 0
        
        for robot in self.waitLine:
            self.waitLine[robot] = self.dist(robot)
        
        self.waitLine = {k: v for k, v in sorted(self.waitLine.items(), key=lambda item: item[1])}
        self.orderLine = [robot for robot in self.waitLine]
        
    def remove_robot(self, robot):
        '''Removes a robot from the line'''
        self.waitLine.pop(robot)
        self.orderLine = [robot for robot in self.waitLine]
        
    def line_index(self,robot):
        '''Returns the position of a robot in the line'''
        return self.orderLine.index(robot) if robot in self.orderLine else None
    
    def add_resources(self, ammount):
        '''Increases the value held by base by int ammount'''
        self.stored += int(ammount)
        return ammount
        
    
class mine(point):
    '''A mine. It can hold a certian ammount, and remove from it.
    Has a line'''
    
    def __init__(self,master,x,y, resources):
        '''x,y is an coordinate, and resources is how much the mine holds'''
        point.__init__(self, x,y)
        # self.x = x
        # self.y = y
        # self.roundx = round(self.x)
        # self.roundy = round(self.y)
        
        self.waitLine = {}
        self.orderLine = []
        self.startResources = resources
        self.resources = resources
        self.master = master
        
    def get_line(self):
        return self.orderLine
    
    def get_resources(self):
        return self.resources
    
    def draw(self, surface):
        '''Draws the mine'''
        pygame.draw.circle(surface, (150,150,150), self.round_pos(), 20)
        if self.resources > 0:
            pygame.draw.circle(surface, pygame.Color(0,255,0), self.round_pos(), round(20 * self.resources/self.startResources))
        
        # pygame.font.init()

        # myfont = pygame.font.SysFont('Comic Sans MS', 10)
        
        # textsurface = myfont.render(str(len(self.orderLine)), False, (100, 0, 0))
        
        # surface.blit(textsurface,(self.x,self.y))
        
    def add_robot(self, robot):
        '''Adds a robot to the waitline and updates the ordered line'''
        self.waitLine[robot] = 0
        
        for robot in self.waitLine:
            self.waitLine[robot] = self.dist(robot)
        
        self.waitLine = {k: v for k, v in sorted(self.waitLine.items(), key=lambda item: item[1])}
        self.orderLine = [robot for robot in self.waitLine]
        
    def remove_robot(self, robot):
        '''Removes a robot from the line'''
        self.waitLine.pop(robot)
        self.orderLine = [robot for robot in self.waitLine]
        
    def line_index(self,robot):
        '''Returns the position of a robot in the line'''
        return self.orderLine.index(robot)
    
    def mine_resources(self, ammount):
        '''Decreases the value held by the mine by int ammount or depletes the mine
        returns ammount mined'''
        if self.resources > ammount:
            self.resources -= ammount
            return ammount
        else:
            mined = self.resources
            self.resources = 0
            return mined
            
        
        
        
def simulate(visualize, ticks, surface, robotsInRocket, rocketWLimit, minePos, rocketPos, speed, carryOffset, mineResourses, miningSpeed, depositSpeed):
    global clock
    all_obs = all_objects(surface,robotsInRocket,rocketWLimit,minePos,rocketPos, speed, carryOffset, mineResourses, miningSpeed, depositSpeed)
    tickNum = 0

    for x in range(ticks):
        if visualize:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
        
                
        if visualize: surface.fill((0, 0, 0))
        done = all_obs.tick(visualize)
        if visualize: pygame.display.flip()
        if visualize: clock.tick(30)
        
        if done:
            return tickNum
        tickNum += 1
        
    return ticks
    
    pygame.quit()
    sys.exit()


def get_ticks(visualize, ticks, robotsInRocket, rocketWLimit, minePlacement, rocketPlacement, speed, carryOffset, mineResources, miningSpeed, depositSpeed):
    global clock
    
    if visualize:
        pygame.init()
        screen = pygame.display.set_mode((700, 700))
        clock = pygame.time.Clock()
    
    
    return simulate(visualize, ticks, screen if visualize else None, robotsInRocket,rocketWLimit,minePlacement,rocketPlacement,speed, carryOffset, mineResources, miningSpeed, depositSpeed)
    pygame.quit()
    sys.exit()