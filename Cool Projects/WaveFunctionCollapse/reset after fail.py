
import random
import pygame
import sys
import os

#Constants
UP, RIGHT, DOWN, LEFT = 0,1,2,3

class Tile:
    '''A tile object; holds four values, clockwise, of edge connections
    e.g. 1010 might be a downwards line'''

    def __init__(self, edgeString, imageIndex):
        self.imageIndex = imageIndex
        self.edgeString = edgeString

    def get_edge(self, whichSide):
        return self.edgeString[whichSide]
    
    def get_imgIndex(self):
        return self.imageIndex
    
    def __str__(self):
        return str(self.imageIndex)+" " +self.edgeString


class GridPos:

    def __init__(self, remainingChoices, parent):
        self.closed = False # has the final value been determined
        self.chosen = None # None unless closed, otherwise a Tile

        self.remainingChoices = remainingChoices
        self.parent = parent
        
        self.neighbors = []
        
        self.attemptedTiles = []

    def set_neighbors(self,listOfNeighbors):
        self.neighbors = listOfNeighbors

    def get_chosen(self):
        return self.chosen
    
    def is_closed(self):
        return self.closed
    
    def restart_choices(self, resetAttempts = False):
        if resetAttempts:
            self.attemptedTiles = []
        
        self.remainingChoices = [t for t in self.parent.allTileChoices \
                                 if t not in self.attemptedTiles]
        self.closed = False

    def close(self,chosenTile):
        self.closed = True
        self.chosen = chosenTile
        self.attemptedTiles.append(chosenTile)
        self.parent.add_history(self)

    def num_choices(self):
        return len(self.remainingChoices) if not self.is_closed() else -1
    
    def refresh_neighbors(self):
        for neigh in self.neighbors:
            if neigh != None:
                result = neigh.refresh()
                
                if result == "No Choices":
                    self.parent.restart()
                    # self.parent.backtrack()
                    return "restart"

    def refresh(self):
        #update remaining choices
        if self.is_closed():
            return "Closed"
            
        for direction in range(4):
            neighbor = self.neighbors[direction]

            if neighbor == None or neighbor.num_choices() == 0:
                continue

            if neighbor.is_closed() and not neighbor.num_choices() == 0:
                neighborTile = neighbor.get_chosen() # Tile object

                newChoices = []

                for choice in self.remainingChoices:
                    if choice.get_edge(direction) == neighborTile.get_edge((direction+2)%4):
                        newChoices.append(choice)

                self.remainingChoices = newChoices

        if len(self.remainingChoices) == 1:  
            self.close(self.remainingChoices[0])
            self.refresh_neighbors()
        
        if len(self.remainingChoices) == 0:
            print("tile ran out of choices")
            self.closed = True
            self.parent.add_history(self)
            return "No Choices"

    def __str__(self):
        if not self.is_closed():
            return str(self.num_choices()) + "OPN"
        return self.chosen.edgeString

                        

class TileSpace:
    
    def __init__(self, width, height, allTileChoices):
        self.width = width
        self.height = height
        self.allTileChoices = allTileChoices

        self.grid = [[None for x in range(width)] for y in range(height)]
        self.closeHistory = []
        
        for y in range(self.height):
            for x in range(self.width):
                newGridPos = GridPos(self.allTileChoices,self)
                self.set_grid_pos(x,y,newGridPos)

        for y in range(self.height):
            for x in range(self.width):
                neighbors = [None,None,None,None]

                if y > 0:
                    neighbors[0] = self.get_grid_pos(x,y-1)
                if x < self.width-1:
                    neighbors[1] = self.get_grid_pos(x+1,y)
                if y < self.height-1:
                    neighbors[2] = self.get_grid_pos(x,y+1)
                if x > 0:
                    neighbors[3] = self.get_grid_pos(x-1,y)
                
                self.get_grid_pos(x,y).set_neighbors(neighbors)
                
    def restart(self):
        self.__init__(self.width,self.height,self.allTileChoices)

    def set_grid_pos(self,x,y,val):
        self.grid[y][x] = val

    def get_grid_pos(self,x,y):
        return self.grid[y][x]
    
    def add_history(self, posAdded):
        self.closeHistory.append(posAdded)

    def pop_history(self):
        return self.closeHistory.pop()

    def printGrid(self):
        print([[str(x) for x in row] for row in self.grid])

    def backtrack(self):
        while len(self.closeHistory) > 0:
            checkTile = self.pop_history()
            
            if len(checkTile.attemptedTiles) >= len(self.allTileChoices)-1:   #every option tried
                pass
            
            if checkTile.num_choices() <= 1:
                checkTile.restart_choices(True)
                
                # checkTile.refresh_neighbors()
            else:
                checkTile.restart_choices()
                checkTile.refresh()
                break



    def update_choices(self):    #Don't use
        for row in self.grid:
            for item in row:
                if item.refresh() == "No Choices":
                    self.restart()
                    return "Broke"

    def close_tile(self):
        leastChoices = 1000 #big num
        possibleTilesToClose = []

        for y in range(self.height):
            for x in range(self.width):
                item = self.get_grid_pos(x,y)
                
                if item.num_choices() < leastChoices and not item.is_closed():
                    leastChoices = item.num_choices()
                    possibleTilesToClose = [(x,y)]
                elif item.num_choices() == leastChoices:
                    possibleTilesToClose.append((x,y))

        if len(possibleTilesToClose) == 0:
            return None
        
        closePos = random.choice(possibleTilesToClose)
        tileToClose = self.get_grid_pos(closePos[0],closePos[1])
        tileToClose.close(random.choice(tileToClose.remainingChoices))
        self.add_history(tileToClose)
        
        tileToClose.refresh_neighbors()

    def tick(self):
        self.update_choices()  #must update first
        self.close_tile()
        self.update_choices()
        
    def draw(self, surface):
        for y in range(self.height):
            for x in range(self.width):
                item = self.get_grid_pos(x,y)
                
                xPos,yPos = (x * TILEWIDTH,y * TILEWIDTH)
                
                if item.is_closed():
                    imgIndex = item.get_chosen().get_imgIndex()
                    surface.blit(IMAGES[imgIndex], (xPos,yPos))
                else:
                    color = int(item.num_choices() / len(IMAGES)  * 255)
                    pygame.draw.rect(surface,(color,0,255-color),
                                     pygame.Rect(xPos,yPos,TILEWIDTH,TILEWIDTH))
                    
                

pygame.init()

#1920 by 1080
TILEWIDTH = 60
WIDTH,HEIGHT = (20,10) #Of the board, in tiles

# The directory containing the images
directory = "G:\My Drive\Python\Cool Projects\WaveFunctionCollapse\City"

# The list to store the images
IMAGES = []
TILES = []

# Iterate through all files in the directory
imageIndex = 0
rotate = False

for filename in os.listdir(directory):
    # Check if the file is an image
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Open the image file
        image = pygame.image.load(os.path.join(directory, filename))
        # Add the image to the list
        
        ##HANDLE ROTATION
        scaledImage = pygame.transform.scale(image, (TILEWIDTH,TILEWIDTH))
        startEdges = filename[:4]
        
        
        
        for rotateValue in range(4 if (rotate or "r" in filename) else 1):
            IMAGES.append(pygame.transform.rotate(scaledImage, rotateValue*-90))
            TILES.append(Tile(startEdges[4-rotateValue:] + startEdges[:4-rotateValue],
                              imageIndex))
            imageIndex += 1
        
    
x = random.random()
random.seed(x)

tileGrid = TileSpace(WIDTH,HEIGHT,TILES)

#To handle backtracking

# Main game loop
pygame.init()
screen = pygame.display.set_mode((WIDTH*TILEWIDTH, HEIGHT*TILEWIDTH))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                        
    screen.fill((0,0,0))
    #tileGrid.tick()
    tileGrid.close_tile()
    
    tileGrid.draw(screen)
    pygame.display.flip()
    clock.tick(15)
