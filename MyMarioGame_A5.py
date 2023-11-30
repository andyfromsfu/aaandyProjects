# MyMarioGame_A5.py
# 
# Description: Mario game has depicted in the sample runs 1, 2 and 3.
#
# Author: AL + Andy Ruozheng Wang
# Date: Nov 20 2023


#-------- Assignment 4 section --------

# Copy and paste the code of your Assignment 4 here:
# starting from the line right after the header comment block
# i.e., starting at the function "createMaze(...)"
# all the way down to the penultimate line of code in your Assignment 4
# i.e., the line of code before #  print("\n-------")

# When you copy and paste, make sure you do not overwrite
# what is below the #------ Assignment 5 starts here ------ line
# because that is where Assignment 5 starts!

import os

# -------------------------------------------------------------------

def createMaze(aMaze, aWidth, aHeight, aCell):
    ''' Create and return "aMaze" of "aWidth" by "aHeight".
        Each cell of the maze is a string set to "aCell".      
    '''
    aMaze = [ [ (aCell) for i in range(aWidth) ] for j in range(aHeight) ]
    
    return aMaze

# -------------------------------------------------------------------

def printMaze(aMaze, aHeight):
    ''' Print "aMaze" of "aHeight" - for testing and debugging purposes.
    ''' 
    for row in range(aHeight):
        print(aMaze[row])  
    return
		
# -------------------------------------------------------------------

def createBoundaryList(aWidth, bH = "---"):
    ''' Create and return a list that contains 2 lists: the first list
        is the top boundary of the maze and contains a string set to "bH".
        The second list is the bottom boundary of the maze and it also
        contains a string set to "bH".

        Other parameter:
         "aWidth" is the width of the maze.
    '''
    return list([[(bH) for number in range(aWidth)],
                 [(bH) for number in range(aWidth)]])                

# -------------------------------------------------------------------

def displayMaze(aMaze, aWidth, aHeight, hBoundary, bS = "|" ):
    ''' Display "aMaze" with column numbers at the top and row numbers
        to the left of each row along with the top and the bottom boundaries
        "hBoundary" that surround the maze.

        Other parameters:
         "aWidth" is the width of the maze.
         "aHeight" is the height of the maze.
         "bS" is the symbol used for the vertical border.
    '''
    
    offset = 3
    aString = (offset+1) * " "

    print()  
    # Display a row of numbers from 1 to aWidth
    for column in range(aWidth):
        aString = aString + str(column+1) + " "
        if len(str(column+1)) == 1 :
            aString += " "           
    print(aString)

    # Display the top boundary of maze
    print(offset * " " + "".join(hBoundary[0])) 
    
    # Display a column of numbers from 1 to aHeight
    # + left and right boundaries of the maze
    for row in range(aHeight):
        pre = str(row+1) + " " + bS

        # If the displayed row number is >= 10 - adjusting for extra digit
        if row >= 9: # Here 9 since we start at 0
           pre = str(row+1) + bS

        post = bS
        aRow = pre + ''.join(aMaze[row]) + post
        print(aRow)

    # Display the bottom boundary of maze
    print(offset * " " + "".join(hBoundary[1]))
    
    return

# -------------------------------------------------------------------

def placeExitGate(aWidth, aHeight, rowMario, columnMario, hBoundary,
                  exitGate = " = "):
    ''' Place the "exitGate" at the opposite corner of Mario's location.
	In other words, place the "exitGate" either in the top boundary or 
	in the bottom boundary whichever is at the opposite corner of
	Mario's location at coordinates ("columnMario","rowMario").

        Other parameters:
         "aWidth" is the width of the maze.
         "aHeight" is the height of the maze.
         "hBoundary" is a list of 2 lists: the first list is the top boundary
                                   and the second list is the bottom boundary.

        Returned value:
         "hBoundary" updated.
         "exitGateLocationList" contains coordinates x and y of the "exitGate".
    '''
    
    exitGateRight = False
    exitGateBottom = False

    # Create "exitGateLocationList" with initial location of "exitGate"
    # at the top left of maze
    exitGateLocationList.insert(0, 0)   
    exitGateLocationList.insert(1, 0)
    
    # Where is Mario?
    # If Mario is top left then exit gate is bottom right
    if columnMario <= ((aWidth) // 2) : # Mario on the left?
        exitGateLocationList[1] = aWidth - 1  # Yes, then "exitGate" on right
        exitGateRight = True
    # No, then assumption holds -> exit gate on the left
    if rowMario <= ((aHeight) // 2) :   # Mario at the top?
        exitGateLocationList[0] = aHeight - 1  # Yes, then "exitGate" at bottom
        exitGateBottom = True
        # No, then initial position of "exitGate" holds at the top left of maze

    # Place "exitGate" in appropriate top/bottom boundary
    if exitGateBottom :
        del hBoundary[1][exitGateLocationList[1]]
        hBoundary[1].insert(exitGateLocationList[1], exitGate)
    else:
        del hBoundary[0][exitGateLocationList[1]]
        hBoundary[0].insert(exitGateLocationList[1], exitGate)       

    # Can return a tuple -> elements separated by a coma
    return hBoundary, exitGateLocationList  

# -------------------------------------------------------------------


# ***Main part of the program- - - - - - - - - - - - - - - - - - - - -

# Welcome the user and identify the game
print("""Welcome to my Mario game.\n""")

# Ask user for filename
print("Please, enter a filename: type 'InputData.txt')")
inputDataName = input("enter: ")
inputDataName = inputDataName.strip()

# # Open file for reading
# new_dir = os.getcwd()
# os.chdir("marioGame")
# new_dir = os.getcwd()
# # print(new_dir)

# inputData = open(f'{new_dir}\{inputDataName}', 'r')
inputData = open(f'{inputDataName}', 'r')

# Assign values
boardValue = []
for aline in inputData:
    boardValue.append(aline[0:3])
mazeWidth = int(boardValue[0])

mazeHeight = int(boardValue[1])
aNumOfTreasures = int(boardValue[2])
aNumOfBombs = int(boardValue[3])
emptyCell = boardValue[4]
obstacle = boardValue[5]
mario = boardValue[6]
marioLocationList = list(boardValue[7].split(" "))
marioLocationList[0] = int(marioLocationList[0])
marioLocationList[1] = int(marioLocationList[1])
marioLocationList = int(marioLocationList[0]),int(marioLocationList[1])

# marioLocation = []
# marioLocation.append(int(marioLocationList[0]))
# marioLocation.append(int(marioLocationList[1]))


treasuresLocation = []
for i in range(8, 23):
    temp = list(boardValue[i].split(" "))
    temp = int(temp[0]),int(temp[1])
    treasuresLocation.append(temp)

bombsLocation = []
for i in range(23, 53):
    temp = list(boardValue[i].split(" "))
    temp = int(temp[0]),int(temp[1])
    bombsLocation.append(temp)

bombScoreRatio = int(boardValue[53])

# bombScoreRatio must be assigned an integer value
exitGateLocationList = list()


obstacleLocationDict = {}
# Put your code here!
for i in range(8,53):
    coords = boardValue[i]
    bombOrTreasure = -1 # bombs
    if i <= 22:
        bombOrTreasure = 1 # treasure
    # obstacleLocationDict
    obstacleLocationDict["(" + coords + ")"] = bombOrTreasure
print(obstacleLocationDict)

# close the file
inputData.close()
# # Create a maze =============================================================
theMaze = list()
theMaze = createMaze(theMaze, mazeWidth, mazeHeight, emptyCell)

for location in obstacleLocationDict:
    obstacleCoords = location[1:4].split(" ")
    theMaze[int(obstacleCoords[0])][int(obstacleCoords[1])] = obstacle


# Create the top and bottom boundaries of the maze
# These boundaries are not part of the maze
hBoundary = list()
hBoundary = createBoundaryList(mazeWidth)

# Place the character (string) "obstacle" in the maze
# This is how we hide the treasures and bombs from the player
# Put your code here!



# Place Mario in the maze
# Put your code here!
theMaze[marioLocationList[0]][marioLocationList[1]] = mario

# print(theMaze)
# Call the appropriate function which computes the location of the
# exit gate and places it in either the top or the bottom boundary
# # Put your code here!
placeExitGate(mazeWidth, mazeHeight, marioLocationList[0], \
              marioLocationList[1], hBoundary, exitGate = " = ")


# # Call the appropriate function to display the maze 
# # Put your code here!
# displayMaze(theMaze, mazeWidth, mazeHeight, hBoundary, bS = "|" )

# print("\n-------")

#------ Assignment 5 starts here ------========================================
      
# Set Mario's score - Done!
# Setting Mario's score has already been done for you
# so you do not have to add any code to the following line:
marioScore = aNumOfBombs // bombScoreRatio # 30 // 3 = 10

#--- The Algorithm for Assignment 5 starts here ---
# This is the algorithm of the game engine, expressed as comments.
# Your task is to convert these comments into corresponding Python code.

# Set the condition variables for your loop
stillPlaying = True
# As long as the player is playing AND marioScore > 0 AND
# Mario has not reached the exit gate, loop i.e., play:

#Calculate the exit gate
exitGateLocationTuple = tuple(exitGateLocationList)
exitUpOrDown = True #True = up, False = down
if exitGateLocationTuple == (0,0) or exitGateLocationTuple == (0,9):
    exitUpOrDown = True # up
else: 
    exitUpOrDown = False # down


# function to replace Mario and update MarioScore
def placeMario(marioLocationList, newMarioLocationList):
    global marioScore, emptyCell, mario, obstacleLocationDict
    theMaze[marioLocationList[0]][marioLocationList[1]] = emptyCell
    theMaze[newMarioLocationList[0]][newMarioLocationList[1]] = mario

    tempMarioLocation = "(" + str(newMarioLocationList[0]) + " " + \
                        str(newMarioLocationList[1]) + ")"
    if tempMarioLocation in obstacleLocationDict:
        if obstacleLocationDict[tempMarioLocation] == -1:
            marioScore -= 1
            obstacleLocationDict[tempMarioLocation] = 0
        elif obstacleLocationDict[tempMarioLocation] == 1:
            marioScore += 1
            obstacleLocationDict[tempMarioLocation] = 0

    if marioScore == 0:
        print("Mario's score is now down to 0! Sorry! You have lost!")
        stillPlaying = False
        pass




while stillPlaying and marioScore > 0:

  # Display the maze 
    displayMaze(theMaze, mazeWidth, mazeHeight, hBoundary, bS = "|" )
  	
  # Display Mario's score (see Sample Runs)
    print(f"Mario's score -> {marioScore}.")
  
  # Display instructions to the player (see Sample Runs)
  # Ask the player (user) to enter either 'r' for right, 'l' for left,
  # 'u' for up and 'd' for down, 'x' to exit the game.
  # Error check: if nothing or anything else is intended,
  # just reprint the prompt to player.
    userInput = input("Move Mario by entering the letter 'r' for right, \
'l' for left, 'u' for up and 'd' for down, 'x' to exit the game: ")
    userInput = userInput.strip()
    userInput = userInput.lower()
    if userInput == 'x':
        stillPlaying = False
        pass
    
    # going right
    if userInput == 'r':
        newMarioLocationList = marioLocationList[0], marioLocationList[1]+1
        # call function
        if newMarioLocationList[1] < mazeWidth:
            placeMario(marioLocationList, newMarioLocationList)
            marioLocationList = newMarioLocationList

    # going left
    if userInput == 'l':
        newMarioLocationList = marioLocationList[0], marioLocationList[1] - 1
        # call function
        if newMarioLocationList[1] >= 0:
            placeMario(marioLocationList, newMarioLocationList)
            marioLocationList = newMarioLocationList

    # going up
    if userInput == 'u':
        if exitGateLocationTuple == marioLocationList and exitUpOrDown == True:
            print(f"Mario has reached the exit gate with a score of \
{marioScore}! Yay! You win!")
            stillPlaying = False
            pass
        newMarioLocationList = marioLocationList[0] - 1, marioLocationList[1]
        # call function
        if newMarioLocationList[0] >= 0:
            placeMario(marioLocationList, newMarioLocationList)
            marioLocationList = newMarioLocationList
    
    # going down
    if userInput == 'd':
        if exitGateLocationTuple == marioLocationList \
            and exitUpOrDown == False:
            print(f"Mario has reached the exit gate with a score of \
{marioScore}! Yay! You win!")
            stillPlaying = False
            pass
        newMarioLocationList = marioLocationList[0] + 1, marioLocationList[1]
        # call function
        if newMarioLocationList[0] < mazeHeight:
            placeMario(marioLocationList, newMarioLocationList)
            marioLocationList = newMarioLocationList
# end of while loop           

print("\nBye!")
print("\n-------!")
