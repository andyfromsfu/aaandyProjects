
inputData = open('C:\workspace\SFUschool\CMPT120\marioGame\inputData.txt', 'r')
# import MyMarioGame_A4 # no error







# mario = # Put your code here!
# # marioLocationList must contain a list with two elements
# # (of type "str") representing the coordinates x and y of Mario's
# # location in the maze. For example: ['0', '0']
# marioLocationList = # Put your code here!

boardValue = []#ahhhh
for aline in inputData:
    boardValue.append(aline[0:3])

# Line 1 is the width of the maze.
mazeWidth = int(boardValue[0])
print(mazeWidth)
# Line 2 is the height of the maze.
mazeHeight = int(boardValue[1])
print(mazeHeight)
# Line 3 is the number of treasures (to be buried in the maze).
aNumOfTreasures = int(boardValue[2])
print(aNumOfTreasures)
# Line 4 is the number of bombs (to be buried in the maze).
aNumOfBombs = int(boardValue[3])
print(aNumOfBombs)
# Line 5 is the symbol representing an empty maze cell. Note: there is a 
# blank space before the symbol then a blank space after it. You must preserve them.
emptyCell = boardValue[4]
print(emptyCell)
# Line 6 is the symbol representing an obstacle. Note: there is a 
# blank space before the symbol then a blank space after it. You must preserve them.
obstacle = boardValue[5]
print(obstacle)
# Line 7 is the symbol representing Mario contained in a maze cell. 
# Note: there is a blank space before the symbol then a blank space after it. You must preserve them.
# Note: The reason there is a blank space before each of the above 3 symbols 
# then a blank space after each of them is because each cell of the maze is 3-character wide.
mario = boardValue[6]
print(mario)

# Line 8 is the location (row and column) of Mario, i.e., coordinates of Mario 
# in the maze at the start of the game. Careful! The row is a number between 0 and 
# mazeHeight-1 and the column is a number between 0 and mazeWidth-1.
marioLocation = boardValue[7]
print(marioLocation)
# Line 9 to Line 23 (inclusively) are the locations of the treasures, 
# one location (row and column) per line. Remember, there are a certain number 
# of treasures and this number was found on Line 3 of this file. Careful! 
# The row is a number between 0 and mazeHeight-1 and the column is a number between 0 and mazeWidth-1.

# Line 24 to Line 53 (inclusively) are the locations of the bombs, one location 
# (row and column) per line. Remember, there are a certain number of bombs and 
# this number was found on Line 4 of this file. Careful! The row is a number between 0 and 
# mazeHeight-1 and the column is a number between 0 and mazeWidth-1.

# Line 54 is the bomb to score ratio, used to set the initial value of Mario’s score. 
# We shall talk about this ratio in Assignment 5.











# ***Main part of the program

# Welcome the user and identify the game
print("""Welcome to my Mario game.\n""")

# Ask user for filename
# fileName = input("Please, enter a filename: (type: inputData.txt)") # uncomment last - - - - - - - 
fileName = "inputData.txt"
inputData = open(f"C:\workspace\SFUschool\CMPT120\marioGame\{fileName}", "r")
inputData = inputData.read()
# print(inputData.read())

# # emptyCell, obstacle, mario must be assigned a string
# emptyCell = # Put your code here!
# obstacle = # Put your code here!

# mario = # Put your code here!
# # marioLocationList must contain a list with two elements
# # (of type "str") representing the coordinates x and y of Mario's
# # location in the maze. For example: ['0', '0']
# marioLocationList = # Put your code here!
