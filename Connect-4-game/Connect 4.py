# Python Class 2231
# Lesson 12 Problem 1
# Author: Skyparker (464417)

board = []
for w in range(42):
  board.append(".")
#print(board)

while True:
  reEnter = False
  players = []
  players.clear()
  players.append(["X", input("Player X, enter your name:")])
  players.append(["O", input("Player O, enter your name:")])
  for lists in players:
    if "" in lists:
      print("Re-enter names")
      reEnter = True
  if reEnter == False:
    break
#print(players)

def get_row_column(row, column):
  return board[row*7+column]

#print(get_row_column(0,0))

def print_board():
  print("0 1 2 3 4 5 6 ")
  for start in range(0, 40, 7):
    for item in range(start, start+7):
      print(board[item], end = " ")
    print("")

#print_board()

def insert(player, column):
  for row in range(5,-1,-1):
    if get_row_column(row, column) == ".":
      board[row*7+column] = player
      break

#insert("@", 4)
#print_board()

def check_vert_win():
  for row in range(3):
    for column in range(7):
      items = board[row*7+column:row*7+column+22:7]
      if items[0] == items[1] == items[2] == items[3] and items[0] != ".":
        return items[0]
      
def check_horizontal_win():
  for row in range(6):
    for column in range(4):
      items = board[row*7+column:row*7+column+5]
      if items[0] == items[1] == items[2] == items[3] and items[0] != ".":
        return items[0]

def check_backslash_win():
  for row in range(3):
    for column in range(4):
      items = board[row*7+column:row*7+column+25:8]
      if items[0] == items[1] == items[2] == items[3] and items[0] != ".":
        return items[0]


def check_forwardslash_win():
  for row in range(3):
    for column in range(3,7):
      items = board[row*7+column:row*7+column+22:6]
      if items[0] == items[1] == items[2] == items[3] and items[0] != ".":
        return items[0]

#print(check_backslash_win())
#print(check_forwardslash_win())
#print(check_horizontal_win())

def check_win():
  win = check_vert_win()
  if win != None:
    return win
  
  win = check_horizontal_win()
  if win != None:
    return win
  
  win = check_forwardslash_win()
  if win != None:
    return win
  
  win = check_backslash_win()
  if win != None:
    return win



winner = None
while "." in board:
  for item in players:
    print_board()
    column = "7"
    
    while True:
      column = input(item[1] + ", You are " + item[0] + ", what column do you want to play in?")
      try:
        column = int(column)
        if column < 0 or column >6:
          pass
        else:
          if get_row_column(0, column) == ".":
            break
      except ValueError:
        pass
      
    
    insert(item[0], int(column))
    winner = check_win()
    current_player = item[1]
    if winner != None:
      break
  if winner != None:
    break

if "." in board or check_win() != None:
  print_board()
  print("Player " + winner + ", " + current_player + ", Won!")
else:
  print("It's a tie!")