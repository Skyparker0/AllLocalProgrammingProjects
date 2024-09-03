# Python Class 2256
# Lesson 11 Problem 1
# Author: Skyparker (464417)

from tkinter import *
import random
####Notes
'''
#When a player clicks a square: Call board.try_click(coord). If that Coordinate has a checker and the correct player is playing,
highlight it. If it is an empty square see if the highlighted square can make that move
'''
####


class CheckerBoard:
    '''Handels all rules and gameplay'''

    def __init__(self,master):
        '''creates a board-dictionary like in reversi'''

        
        self.board = {}
        #create the board by
        for row in range(8):    #cycling through all the rows
            column = 0

            #and creating keys as coordinates, with noplay, None, 0, or 1 as values
            
            if row % 2 == 0:    #even rows start with green
                self.board[(row,0)] = 'noplay'
                column = 1
                
            for square in [None,'noplay'] * 3 + [None]:
                #chooses if the square should be a checker or nothing
                if square == None and row < 3:
                    self.board[(row,column)] = 0
                elif square == None and row > 4:
                    self.board[(row,column)] = 1
                else:
                    self.board[(row,column)] = square
                
                column += 1
                
            if row % 2 == 1:    #odd rows end with green
                self.board[(row,column)] = 'noplay'

        self.current_player = 1     #The bottop player starts
        self.game_over = None       #The winner of the game (yes, not great naming)
        self.highlighted = None     #The coordinate that is currently highlighted
        self.mustJump = False       #If the player has jumps available: they mutsJump
        self.master = master        #Never used this: If I wanted to, I could call self.master.update_display() but there was no need.
        self.continueJump = False   #If a peice makes a jump and still has jumps available, they jump again.
        self.continueJumpPos = None #for the computer

    def try_computer_turn(self):
        '''CheckerBoard.try_computer_turn()
        The computer player randomly plays one of it's
        legal moves, without any intelligence'''
        
        if self.continueJump:   #if there has been a continued jump
            moves = self.get_move(self.continueJumpPos,True)    #What moves can the peice that's already jumped make
            self.move_square(self.continueJumpPos, random.choice(moves))    #choose a random one of those moves, and move there
            if not self.continueJump:   #next player if the jump is not continued again
                self.next_player()
        else:
            moveableSquares = []    #the squares that can be moved

            #For every coordinate
            for row in range(8):
                for column in range(8):
                    coord = (row,column)
                    
                    if self.get_coord_val(coord) in range(self.current_player,4,2) \
                       and self.get_move(coord,True) != []:    #If that coordinate belongs to the current player And has moves
                        
                        moveableSquares.append(coord)        #add it, it can be moved

            chosenSquare = random.choice(moveableSquares)           #choose a random moveable square
            move = random.choice(self.get_move(chosenSquare,True))  #choose a random move
            
            self.move_square(chosenSquare,move)    #move the square to the chosen move
            
            if not self.continueJump:   #next player if the jump is not continued
                self.next_player()
                        
                

        

    def try_click(self,coord):
        '''CheckerBoard.try_click(coord)
        A square has been clicked- the board reacts according to the rules'''

        if self.get_player() in self.master.computerPlayers:
            return ''

        #Can highlight a square if it is the current player's peice, and if the player isn't continuing their jump.
        if self.get_coord_val(coord) in range(self.current_player,10,2) and not self.continueJump:
            self.highlight(coord)
        elif self.highlighted != None:    #if a peice is highlighted
            if coord in self.get_move(self.highlighted,True):    #if the square clicked is an option of the highlighted square
                self.move_square(self.highlighted, coord)        #move the highlighted square to the click
                if not self.continueJump:                        #next player if the jump is not continued
                    self.next_player()
            
        

    def next_player(self):
        '''CheckerBoard.next_player()
        Moves on to the next player
        resets the highlighted square and continueJump as
        well as initializing other variables for the new player'''
        self.highlighted = None
        self.continueJump = False
        self.current_player = 1 - self.current_player    # 1-0 = 1   1-1 = 0
        self.check_all()     #checks for wins, and checks if the player must jump
    
    def highlight(self,coord):
        '''CheckerBoard.highlight(coord)
        coord is now the highlighted square'''
        self.highlighted = coord
                
    def string(self):
        '''CheckerBoard.string()
        Prints out the board. I used this to make sure the grid
        creation worked'''
        
        for row in range(8):
            for column in range(8):
                print(self.board[(row,column)], end = '|')
            print('')

    def get_highlighted(self):
        '''CheckerBoard.get_highlighted() >>> tuple
        returns the coord of the highlighted square'''
        return self.highlighted

    def get_player(self):
        '''CheckerBoard.get_player() >>> int
        returns the current player'''
        return self.current_player

    def get_winner(self):
        '''CheckerBoard.get_winner() >>> None or int
        returns the winner'''
        return self.game_over

    def get_coord_val(self,coord):
        '''CheckerBoard.get_coord_val(coord) >>> 'noplay',None, or int
        returns the value of a coord in the board'''
        return self.board[coord]

    def get_move(self,coord, getMoves = False):                          
        '''CheckerBoard.get_move(coord, getMoves) >>> step, None, or jump, or a list of coordinates

        if getMoves is false: it returns the sorts moves a checker can make
        if getMoves is true, it returns a list of the coordinates a checker
        can move to.'''
        
        player = self.get_coord_val(coord)    #what color the checker is

        moveDirs = []    #the directions the player can move in

        #if the player is 2 or 3, they can move both dirrections
        
        if player in [0,2,3]:          #going down the screen:  +row
            moveDirs += [[1,-1],[1,1]]

        if player in [1,2,3]:          #going up the screen:  -row
            moveDirs += [[-1,-1],[-1,1]]

        output = None           #no moves possible (yet)
        possibleMoves = []      #no moves fount (yet)
        
        for direction in moveDirs:         #for each of the directions the peice can move
            try:    #so we don't have to check for off-the-board cases, they simply are skipped
                squareCoord = (coord[0]+direction[0],coord[1]+direction[1])  # the coord we are trying to move to
                square = self.get_coord_val(squareCoord)

                if square == None and output != 'jump':    #if the square we are trying to move to is blank and 
                    output = 'step'                        #the output is not jump
                    if not self.mustJump:                  #add the coordinate if the charecter does not need to jump
                        possibleMoves.append(squareCoord)

                if square in [0,1,2,3] and square % 2 != player % 2:    #enemy square
                    #if the square along the diagonal, past the enemy square, is blank...
                    if self.get_coord_val((coord[0]+ 2*direction[0],coord[1]+ 2*direction[1])) == None:
                        output = 'jump'   #jump is the output and the coordinate of the blank square is added.
                        possibleMoves.append((coord[0]+ 2*direction[0],coord[1]+ 2*direction[1]))
            except:
                continue

        if getMoves:    #if  we want a list of coordinates,
            if player%2 == self.current_player:    #if the correct player is playing
                return possibleMoves               #give the list of coords
            #but if the wrong player is playing, don't let them move the other player's peices,
            return [x for x in range(len(possibleMoves))]    #return a list the length of the number of moves possible
        
        return output    #if we didn't want the coordinates, return None, step, or jump

    def move_square(self,start,end):
        '''CheckerBoard.move_square(start,end)
        Moves the value of start to end,
        deals with jumping, king crowning, and continued jumps'''
        
        oldValue = self.get_coord_val(start)        #value of start
        change = [end[x]-start[x] for x in [0,1]]   #the change in row and column, used for jump-checking
        if not self.get_player() in self.master.computerPlayers:
            self.highlighted = end                      #highlight the end peice
        self.board[start] = None
        self.board[end] = oldValue                  #the end value is now what the start value was
        jumped = False                              #initialize jumped and continueJump- we will figure those now
        self.continueJump = False
        if change[0] in [-2,2]:    #the move was a jump
            jumped = True
            self.board[(start[0]+change[0]//2,start[1]+change[1]//2)] = None     #this is the peice that was jumped

        if end[0] in [0,7] and oldValue < 2:    #become king- they got to one end
            self.board[end] = oldValue + 2
        elif jumped:    #check for aditional jumps, the point of the elif is that you cannot continue jumping after becoming a king
            if self.get_move(end) == 'jump':
                self.continueJump = True
                self.continueJumpPos = end

    def check_all(self):
        '''CheckerBoard.check_all()
        Checks for a winner, and checks if the player must jump.
        adjusts attribues accordingly'''
        
        player = self.current_player
        playerHasMoves = False
        playerHasCheckers = False
        self.mustJump = False

        #check every square
        for row in range(8):
            for column in range(8):
                pos = (row,column)
                val = self.get_coord_val(pos)

                if val in [0,1,2,3] and val%2 == player:    #the player has checkers
                    playerHasCheckers = True

                    if self.get_move(pos) != None:          #the player has moves
                        playerHasMoves = True

                    if self.get_move(pos) == 'jump':
                        self.mustJump = True                #the player must jump

        if not playerHasMoves or not playerHasCheckers:     #this player has lost
            self.game_over = 1 - player                     #the other player has won
        
            

class CheckerSquare(Canvas):
    '''A single checker display of the Checkers game
    Almost identical to ReversiSquare'''

    def __init__(self,master,r,c, playable):
        '''CheckerSquare(master,r,c, playable)
        creates a new blank Checker square at coordinate (r,c)
        playable detirmines color and click-ability'''
        
        self.playable = playable
        if playable:
            #playable squares are white and can be clicked
            Canvas.__init__(self,master,width=50,height=50,bg='AntiqueWhite2')
            self.bind('<Button>',master.get_click)
        else:
            #non playable squares are green and cannot be clicked
            Canvas.__init__(self,master,width=50,height=50,bg='dark sea green')
            
        self.grid(row=r,column=c)
        self.position = (r,c)

    def get_position(self):
        '''CheckerSquare.get_position() -> (int,int)
        returns (row,column) of square'''
        return self.position

    def make_color(self,color,isKing=False, isHighlight=False):
        '''CheckerSquare.make_color(color)
        changes the color of piece on square to specified color, can also makes them highlighted
        and a king'''
        
        self.erase()

        if color != None:
            self.create_oval(10,10,44,44,fill=color)

        if isHighlight:
            self['highlightbackground'] = 'orange'
        if isKing:
            self.create_text(25,25, text = "*", font=('Arial',18))

    def erase(self):
        '''CheckerSquare.erase()
        Erases all items on the canvas'''
        
        self['highlightbackground'] = 'white'

    
        itemList = self.find_all()  # remove existing pieces
        for item in itemList:
            self.delete(item)
        
        
        
class CheckerGame(Frame):
    '''Holds the game of checkers'''

    def __init__(self,master,computerPlayers):
        '''CheckerGame(master)
        Creates a game of checkers'''
        
        Frame.__init__(self,master,bg='white')    
        self.grid()
        self.board = CheckerBoard(self)    #create a checker board, which runs most of the game
        self.colors = ('red','white')

        self.squares = {}    #dictionary with coords as keys and CheckerSquares as values

        #make a checker square for every position
        for row in range(8):
            for column in range(8):
                self.squares[(row,column)] = CheckerSquare(self, row, column, self.board.board[(row,column)] != 'noplay')


        #set up turn label, turn indicator, and announcement label
        self.turnLable = Label(self,text="Turn:")
        self.turnLable.grid(row = 8, column = 1)
        
        self.turnIndicator = CheckerSquare(self,8,2, False)
        
        self.announcement = Label(self,text="")
        self.announcement.grid(row = 8,column = 3, columnspan = 5)

        self.computerPlayers = [x for x in [0,1] if computerPlayers[x]]    #which players are computers
        self.update_display()    #update the display, start the game

    def update_display(self):
        '''CheckerGame.update_display()
        Updates the display of all the squares so they match the board's values
        also updates things like the highlighted square, turn indicator, and announcement.
        if a computer is playing, they get a turn.''' 
        
        highlightCoord = self.board.highlighted    #coord, or None
        self.turnIndicator.make_color(self.colors[self.board.current_player])    #the turn indicator updates

        if self.board.game_over != None:    #someone has lost!
            self.announcement['text'] = 'Player ' + self.colors[self.board.game_over] + ' has won!'
            self.announcement.configure(font=('Arial',16, "bold"))
            self.turnIndicator.make_color(self.colors[self.board.game_over])
            self.end_game()
        elif self.board.continueJump:       #the jump must be continued
            self.announcement['text'] = 'Must continue jump'
        elif self.board.mustJump:           #the player must jump
            self.announcement['text'] = 'Must jump'
        else:                               #there is nothing to announce
            self.announcement['text'] = ''
            
        #for every position    
        for row in range(8):
            for column in range(8):
                square = self.squares[(row,column)]
                squareValue = self.board.board[(row,column)]
                square.erase()
                color = None
                king = False
                highlighted = False
                if not squareValue in [None, 'noplay']:    #if the value of the square is a number
                    color = self.colors[squareValue % 2]   #the color should relate to the number

                if squareValue in [2,3]:    #if the square is a king, 
                    king = True             #there will be a mark to show that
                    
                if highlightCoord != None and highlightCoord == (row,column):    #If this square is the highlighted square, it will get highlighted
                    highlighted = True

                square.make_color(color,king,highlighted)    #update the square's appearance according to the information gathered

        if self.board.game_over == None and self.board.get_player() in self.computerPlayers:    #if the player has not lost and it's the computer's turn
            self.after(1000,self.computer_turn)   #computer gets a turn, after a second
            

    def get_click(self,event):
        '''CheckerGame.get_click(event)
        Event handler for clicking a square'''
        
        coord = event.widget.get_position()    #coord of the square clicked
        self.board.try_click(coord)            #tell the board that the coord was clicked
        self.update_display()                  #update the display

    def computer_turn(self):
        '''CheckerGame.computer_turn()
        The computer player takes it's turn'''
        self.board.try_computer_turn()    #Tell board to try a computer turn
        self.update_display()             #update the display

    def end_game(self):
        '''CheckerGame.end_game()
        Disables all click listeners'''
        for row in range(8):
            for column in range(8):
                self.squares[(row,column)].unbind('<Button>')    #removes the click binding from every square
        


def play_checkers(red,white):
    '''play_checkers(red,white)
    starts a new game of Checkers, red and white can each be true or false
    false means the color is not AI
    true means the color is AI'''
    root = Tk()

    #kept having the problem of the game being behind everything, found a confusing solution that works
    #root.lift
    root.lift()
    root.attributes('-topmost',True)
    root.after_idle(root.attributes,'-topmost',False)
    
    root.title('Checkers')
    RG = CheckerGame(root,(red,white))    #create the checkers game
    RG.mainloop()

#asks for user input on what players should be AI
white = input('Is white AI?   y/n ') == 'y'    #it only maters if they wrote y
red = input('Is red AI?   y/n ') == 'y'    

play_checkers(red,white)
