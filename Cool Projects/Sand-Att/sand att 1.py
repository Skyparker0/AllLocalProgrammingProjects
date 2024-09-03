# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 16:31:19 2020

@author: batte
"""

#SAND ATTEMPT

import numpy as np

class sand(object):
    '''A grain of sand that occupies a sandbox'''
    
    def __init__(self,x,y,master):
        
        self.x = x
        self.y = y
        self.master = master
        
    def get_pos(self):
        return self.x, self.y
        
    def go_to(self,x,y):
        self.master.move(self.x,self.y,x,y)
        self.x = x
        self.y = y
        
    def tick(self):
        if self.master.get_at(self.x,self.y+1) == 0:
            self.go_to(self.x,self.y+1)
        elif self.master.get_at(self.x-1,self.y+1) == 0:
            self.go_to(self.x-1,self.y+1)
        elif self.master.get_at(self.x+1,self.y+1) == 0:
            self.go_to(self.x+1,self.y+1)
            
            
class sandbox(object):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = np.zeros([width,height])
        
    def add_at()