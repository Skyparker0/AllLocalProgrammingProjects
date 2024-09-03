import pygame
import sys
import random
import math
import numpy as np


        
        
        
        
pygame.init()
screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()

# points = [point(x+random.randint(-100,100),y+random.randint(-100,100),random.randint(10,30),[random.randint(0,255),\
#         random.randint(0,255),random.randint(0,255)],10) for x in range (0,600,100) for y in range (0,600,100)]

while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                        pygame.quit()
                        sys.exit()
        
                
        screen.fill((0, 0, 0))
        
        for p in points:
            p.round_pos()
            p.draw()
            p.move_closer(pygame.mouse.get_pos(),1000,5*points.index(p) + 30)
            if round(distance(p.get_pos(), pygame.mouse.get_pos())) == 5*points.index(p) + 30:
                pygame.draw.line(screen,(0,0,255),(p.get_pos()), pygame.mouse.get_pos(),1)
            else:
                p.move_closer(pygame.mouse.get_pos(),1000,5*points.index(p) + 30)

            # for move_to in points:
            #     # pygame.draw.line(screen,p.color,(p.x, p.y), move_to.get_pos(),1)
            #     p.move_closer(move_to.get_pos(),3,100)
        
        pygame.display.flip()
        clock.tick(30)
        
        
