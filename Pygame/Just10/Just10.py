#TODO: Wrong combination case where all are not 10's and all combinations are more than 10
#Just give an option of new game

#Music from
#http://www.soundjig.com/pages/soundfx/beeps.html

#Help usage
#Usage: print(getStartingBoardDS.__doc__)
#import filename
#help(filename)

#If time needs to be used
#Time the clock and redraw new combination of tiles where you re-start
#clock = pygame.time.Clock()
#clock.tick(200)

#imports
import os
import random
import pygame
import sys
import pygame.time


#RGB
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255,200,200)
BLUE = (0,0,255)
DARKBLUE = (0,0,128)
BLUISH = (50, 50, 255)

SCREENBLUE = (50, 50, 128)
TILECOLOR = GREEN
GAMEBOARDCOLOR = BLUISH
SCREENCOLOR = SCREENBLUE
TEXTCOLOR = WHITE
MESSAGECOLOR = RED
MESSAGEBGCOLOR = BLACK

#Constants
#Width and height of screen
WIDTH = 450
HEIGHT = 650
#total Screen tuple
SCREENSIZE = (WIDTH, HEIGHT)
#Gap for the game tile from the top
COORDX = 0
COORDY = 100
#Game tile
COORDWIDTH = 450
COORDHEIGHT = 450
#Game over message position
GAMEOVERXPOS = 100
GAMEOVERYPOS = 550
#Make the tiles smaller to see margins, else all tiles merge into one another
XMARGIN = 5
YMARGIN = 5
#For the middle squares to see the margin - need margins on both sides
TILEWIDTH = 150-(2*XMARGIN)
TILEHEIGHT = 150-(2*YMARGIN)
#Game board rectangle
GAMEBOARDCOORD = (COORDX, COORDY, COORDWIDTH, COORDHEIGHT)

#combinations
JUSTTEN = 10
COMB1 = [9,1]
COMB2 = [8,2]
COMB3 = [7,3]
COMB4 = [6,4]
COMB5 = [5,5]
PAIRSIZE = 2

#font
BASICFONTSIZE = 20
#rest
BORDERWIDTH = 5
ROWCOLMAX = 3
BOARDSIZE = 3
NOBORDER = 0



#Had to create this since inititalization was happening multiple times
class Controller:
        board = [0]*(BOARDSIZE*BOARDSIZE)
        twoDimBoard = [[0]*BOARDSIZE]*BOARDSIZE

        def __makeText(self, text, color, bgcolor, top, left):
                """
                Surface and Rect objects for positioning any text on the screen,
                given as a parameter
                """
                textSurf = BASICFONT.render(text, True, color, bgcolor)
                textRect = textSurf.get_rect()
                textRect.topleft = (top, left)
                return (textSurf, textRect)

        def __getPixelCoordinates(self, n):
                """
                Given the position in the board's 1 dimensional array gives the position
                in x,y coordinated for the top-left point in the tile

                Returns the coordinates
                """
                #say for board[n]
                #n/3 gives row and column is n%3
                #each tile is 150*150
                #left = x =150*column
                #top = y = 150*row
                left = XMARGIN + TILEWIDTH*(n%ROWCOLMAX)
                #Imagine not typecasting here, gives different values
                top = YMARGIN + TILEHEIGHT*int(n/ROWCOLMAX)
                return (left, top)

        def __drawTile(self, tilex, tiley, adjx, adjy, tileNumber):
                """
                Draw the tiles with random numbers that mix to form 10
                1.Erase the tile (last param=0) - Make the tile the game(inner) board's color
                2.Subtraction of X,Y margins for spacing between tiles
                3.Else draw the tiles with the text within it
                """
                #Erase
                if(tileNumber == 0):
                        #NOBORDER means fill it up completely
                        pygame.draw.rect(SCREEN, GAMEBOARDCOLOR, (tilex+adjx, tiley+adjy, TILEWIDTH-XMARGIN, TILEHEIGHT-YMARGIN), NOBORDER)
                else:
                        pygame.draw.rect(SCREEN, TILECOLOR, (tilex+adjx, tiley+adjy, TILEWIDTH-XMARGIN, TILEHEIGHT-YMARGIN), NOBORDER)
                        #Render images here later with the random number
                        textSurf = BASICFONT.render(str(tileNumber), True, TEXTCOLOR)
                        textRect = textSurf.get_rect()
                        textRect.center = tilex + int(TILEWIDTH/2) + adjx, tiley + int(TILEHEIGHT/2) + adjy
                        SCREEN.blit(textSurf, textRect)
                return
        
        #Controller for drawing tiles
        def __drawBoard(self, board, message, reDraw):
                """
                Draw the board with tiles for a given filled single dimensional array-board

                1.Message - if exists means game is over and the game board screen is black with red text
                2.For each of the tiles, if redraw situation-redraw
                3.For each of the tiles if fresh game, draw the tiles, in which board position has a number(!=0)
                """
                #The gameover rect will be used in event handling           
                global MSGTEXTSURF, MSGTEXTRECT
                if message:
                        pygame.draw.rect(SCREEN, BLACK, GAMEBOARDCOORD, 0)
                        MSGTEXTSURF, MSGTEXTRECT = self.__makeText(message, RED, BLACK, 125, 325)
                        SCREEN.blit(MSGTEXTSURF, MSGTEXTRECT)
                        return
                else:
                        for i in range(len(board)):
                                (left, top) = self.__getPixelCoordinates(i)
                                #if re-drawing erase all of the board-new game situation
                                if(reDraw):
                                        #BUG resolved:Passing 0 for draw tile to erase
                                        self.__drawTile(left, top, COORDX, COORDY, 0)
                                if(board[i] != 0):
                                        #Drawing the new board position
                                        self.__drawTile(left, top, COORDX, COORDY, board[i])
                                else:
                                        continue
                        
        def __nestedListstoList(self, nestedListOfPairs):
                """
                Convert nested list to a single dim list
                Only used by __getStartingBoardDS to get the logic for pairs of combinations
                """
                singleList = [0]*(len(nestedListOfPairs)*PAIRSIZE)
                listiter = 0
                for row in range(len(nestedListOfPairs)):
                        for col in range(PAIRSIZE):
                                singleList[listiter] = nestedListOfPairs[row][col]
                                listiter = listiter + 1
                return singleList
        
        def __getStartingBoardDS(self):
                """Data structure for poupulating the board initially with random tiles and
                combination of random numbers

                Returns the data structure
                """
                #Algorithm: 
                #Randomly pick 2,4,6,8 of all 5 combinations
                
                #starting state
                #generate combinations of 10 in random
                #populate random positions max leave one square free
                
                board = [0]*(BOARDSIZE*BOARDSIZE)
                #tilesoccupied should never increae 8
                tilesoccupied = 0

                #Since we have items in pairs - gives 1/2/3/4 - a pair
                noOfPairs = random.randrange(1, int(len(board)/2))
                #sample 1st param = population, set of 5
                #2nd param = k set of items
                #2,4,6,8 tiles to occupy based on noOfPairs
                tiletooccupy = random.sample([COMB1, COMB2, COMB3, COMB4, COMB5], noOfPairs)
                
                #now i need a random sample of board positions
                tilesOccupied =  noOfPairs*PAIRSIZE
                #Turn list of lists to a list of integers
                boardlist = self.__nestedListstoList(tiletooccupy)
                #returns a number from 1 to tilesOccupied (2/4/6/8)
                for i in range(0, tilesOccupied):
                        #BUG: Unique board positions
                        boardposition = random.randint(0, ((BOARDSIZE*BOARDSIZE)-1) )
                        #Create another till you get a new one
                        while(board[boardposition] != 0):
                                boardposition = random.randint(0, ((BOARDSIZE*BOARDSIZE)-1) )
                        board[boardposition] = boardlist[i]
                        tilesoccupied += 1
                return board
        
        def __init__(self):
                """
                Constructor:
                1.Intializes pygame
                2.Sets caption and font
                3.Global SCREEN object
                4.Sets screen color
                5.Draw game board
                6.Get the board data structure
                7.Draw tiles
                8.Play sound
                """
                global SCREEN, BASICFONT
                #Pygame initiation
                os.environ["SDL_VIDEO_CENTERED"] = "1"
                pygame.init()
                #Get the font
                BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
                #set up display
                pygame.display.set_caption("Junior 10")
                #Screen to draw on
                SCREEN = pygame.display.set_mode(SCREENSIZE)

                #r,g,b
                SCREEN.fill(SCREENCOLOR)

                #last parameter if 0, the rectangle is filled
                #(x,y,width,height) is a Python tuple
                #x,y are the coordinates of the upper left hand corner
                #width, height are the width and height of the rectangle
                pygame.draw.rect(SCREEN, GAMEBOARDCOLOR, GAMEBOARDCOORD, 0)

                #inner rectangle is x = 420,y = 400 - divide the square into 9 pieces
                #450/3 = 150
                #450/3 = 150
                #draw the board
                self.board = self.__getStartingBoardDS()
                reDraw = False
                self.__drawBoard(self.board, "", reDraw)
                #Play sound
                #http://www.nerdparadise.com/programming/pygame/part3
                pygame.mixer.music.load('background.mp3')
                #Play once
                #pygame.mixer.music.play(0)
                #Play infinitely
                pygame.mixer.music.play(-1)
                
        def control(self):
                """
                1.Main game loop - a big while to check for quit
                2.For loop to receive events
                3.Check for quit all the time, the 
                4.For loop looking for specific quit event is in __checkForQuit
                5.Mouse up and game is over - black screen case
                6.   Get a new DS, redraw the board(erase all and redraw), new game starts
                7.Mouse up but post a movement of a tile
                8.   If game is over, repeat game over routine
                     Display game over message
                9.If move - get the tile clicked, if button down due to game over
                     replay the background music
                10.Update the screen
                """
                running = True
                clickedTile = -1
                movedToTile = -1
                gameOver = False
                while running:
                        self.__checkForQuit()
                        for event in pygame.event.get():
                                if(event.type == pygame.MOUSEBUTTONUP and gameOver==True):
                                        x,y = event.pos
                                        
                                        if(MSGTEXTRECT.collidepoint(x,y)):
                                                self.board = self.__getStartingBoardDS()
                                                pygame.draw.rect(SCREEN, GAMEBOARDCOLOR, GAMEBOARDCOORD, 0)
                                                reDraw = True
                                                self.__drawBoard(self.board, "", reDraw)
                                                gameOver = False
                                elif(event.type == pygame.MOUSEBUTTONUP and pygame.MOUSEMOTION and pygame.MOUSEBUTTONDOWN):
                                        #unpack the tuple
                                        x,y = event.pos
                                        movedToTile = self.__getSpotClicked(self.board, x, y)
                                        gameOver = self.__checkIfEmptyAndMove(clickedTile, movedToTile)
                                        if(gameOver):
                                                pygame.mixer.music.stop()
                                                pygame.mixer.music.load('gameover.mp3')
                                                pygame.mixer.music.play(0)
                                                reDraw = False
                                                self.__drawBoard(self.board, "Game Over. Continue?", reDraw)
                                elif(event.type ==  pygame.MOUSEBUTTONDOWN):
                                        if(gameOver):
                                                pygame.mixer.music.stop()
                                                pygame.mixer.music.load('background.mp3')
                                                pygame.mixer.music.play(-1)
                                        #set a boolean flag as to it was pressed and get the cell in which it happened
                                        x,y = event.pos
                                        clickedTile = self.__getSpotClicked(self.board, x, y)
                                        
                                #Update the screen
                                pygame.display.update()
                                

        def __slideInto(self, oldPos, newPos, newNumber):
                """
                1.From DS positions get the top left pixel coordinates for old and new tiles
                2.Erase positions of old and new tiles
                3.Draw the tile with the new number
                """
                (leftold, topold) = self.__getPixelCoordinates(oldPos)
                (left, top) = self.__getPixelCoordinates(newPos)
                #Erase old and erase where you slide into as well
                self.__drawTile(leftold, topold, COORDX, COORDY, 0)
                self.__drawTile(left, top, COORDX, COORDY, 0)
                self.__drawTile(left, top, COORDX, COORDY, newNumber)
                return
        
        def __turnBoardToTwoDim(self):
                """
                Convert single Dim DS to 2D DS just to check NEWS positions
                """
                for row in range(BOARDSIZE):
                        for col in range(BOARDSIZE):
                                self.twoDimBoard[row][col] = self.board[row*BOARDSIZE+col]
                return
        
        def __checkIfValidMove(self, oldPos, newPos):
                """
                1.None of the tiles chosen - false
                2.Empty tile chosen to move - false
                3.Re-create board positions in row,column format
                4.Check valid NORTH, EAST, SOUTH,WEST positions for the newPos, invalid ones rejected
                5.Only one move allowed, like the King in chess, if valid return true
                """
                #not one of the 9 grids
                if((newPos == None) or (oldPos == None)):
                        return False
                #If moving from an empty position
                if(self.board[oldPos] == 0):
                        return False
                self.__turnBoardToTwoDim()
                #Get row and column from BoardPosition
                oldrow = int(oldPos/BOARDSIZE)
                oldcol = oldPos%BOARDSIZE
                newrow = int(newPos/BOARDSIZE)
                newcol = newPos%BOARDSIZE

                #possible new positions
                #oldrow-1, oldcol. Position = (oldrow-1)*BOARDSIZE+col
                #oldrow+1, oldcol. Position = (oldrow+1)*BOARDSIZE+col
                #oldrow, oldcol-1. Position = oldrow*BOARDSIZE+(col-1)
                #oldrow, oldcol+1. Position = oldrow*BOARDSIZE+(col+1)
                if( ( ((oldrow-1)*BOARDSIZE+oldcol) in range(0,len(self.board))) and (newPos == ((oldrow-1)*BOARDSIZE+oldcol)) ):
                        return True
                elif( ( ((oldrow+1)*BOARDSIZE+oldcol) in range(0,len(self.board))) and (newPos == ((oldrow+1)*BOARDSIZE+oldcol)) ):
                        return True
                elif( ((oldrow*BOARDSIZE+(oldcol-1)) in range(0,len(self.board))) and (newPos == (oldrow*BOARDSIZE+(oldcol-1)))):
                        return True
                elif( ((oldrow*BOARDSIZE+(oldcol+1)) in range(0,len(self.board))) and (newPos == (oldrow*BOARDSIZE+(oldcol+1))) ):
                        return True
                else:
                        return False
                

        def __checkIfEmpty(self, oldPos, newPos):
                """
                1.Moving positions are invalid, return false
                2.If newPos-tile moving into is empty, return True
                """
                #not one of the 9 grids
                if((newPos == None) or (oldPos == None)):
                        return False
                #If moving to an empty position
                if(self.board[newPos] == 0):
                        return True
                return False

        def __checkIfValidJoinTiles(self, oldPos, newPos):
                """
                1.If clicks are invalid, return false
                2.If sum of tiles more than 10, return false
                3.If 10 return true
                4.If <10 return true
                """
                if((newPos == None) or (oldPos == None)):
                        return False
                if((self.board[oldPos]+self.board[newPos]) > 10):
                        #Erroneus move - do nothing
                        return False
                elif((self.board[oldPos]+self.board[newPos]) == 10):
                        return True
                else:
                        return True
                return False

        def __checkifGameOver(self):
                """
                For all board positions, if board positions anything other than 0 or 10
                -game is not over
                -Find all 10's and all 0's then game is over
                """
                for i in range(0, len(self.board)):
                        if((self.board[i] != 10) and (self.board[i] != 0)):
                                return False
                return True
        
        def __checkIfEmptyAndMove(self, oldPos, newPos):
                """Algorithm
                1.Check if valid move - make it simple - only one cell allowed
                2.Check if empty - move if empty
                3.If not empty add and check move is valid, if not ignore
                4.If valid, check if it is 10, return True
                5.If valid, check if not 10 return False
                """
                if(self.__checkIfValidMove(oldPos, newPos)):
                        if(self.__checkIfEmpty(oldPos, newPos)):
                                self.board[newPos] = self.board[oldPos]
                                #empty it
                                self.board[oldPos] = 0
                                self.__slideInto(oldPos, newPos, self.board[newPos])
                        else:
                                #Add board positions
                                if(self.__checkIfValidJoinTiles(oldPos, newPos)):
                                        self.board[newPos] = self.board[oldPos]+self.board[newPos]
                                        self.board[oldPos] = 0
                                        #empty it
                                        self.board[oldPos] = 0
                                        self.__slideInto(oldPos, newPos, self.board[newPos])
                                        if(self.__checkifGameOver()):
                                                return True
                                        else:
                                                return False
                                else:
                                        #do nothing
                                        #ToDO: probably show a message and stay at the same place
                                        return False
                else:
                        return False
                        
            

        def __getSpotClicked(self, board, x, y):
                """
                From the mouse click pixel coordinates, get where on the board data structure it is
                1.For each tile going through the board DS get the pixel coordinates
                2.Form a rect with those coordinates
                3.If that collides with the points received while clicking, match is found
                4.Clicks not on one of the game tiles, ignore
                """
                for i in range(len(board)):
                        #unpack the tuple
                        left, top = self.__getPixelCoordinates(i)
                        #Add the offset for get position in the inner screen
                        tileRect =  pygame.Rect(left+COORDX, top+COORDY, TILEWIDTH, TILEHEIGHT)
                        if tileRect.collidepoint(x,y):
                                #If collides, get the tile number
                                if(i in range(0, len(board))):
                                        return i
                                #else:
                                #        print("should it ever come here?")
                        else:
                                #if not inside the game tile it comes here
                                continue


        def __checkForQuit(self):
                """
                Checking for quit event, from the close button
                """
                #Same as passing a parameter
                ##    for event in pygame.event.get():
                ##    if event.type == pygame.QUIT:
                for event in pygame.event.get(pygame.QUIT):
                        terminate()

        

#Called from main, hence outside the class
def terminate():
        """
        Terminate the game and the shell
        """
        pygame.quit()
        #This is required. If you comment this and you click quit it will give
        #an error saying pygame is not initializd but am still trying to update
        #on the next line
        #if we add this, the shell will exit for the current code and the error
        #will not be seen
        sys.exit()

def main():
        """
        Instantiates controller object and calls control which has the event loop
        """
        try:
                #Do initialization once
                controller =  Controller()
                #Event loop of the game would run
                controller.control()

        except SystemExit:
                terminate()

#Decide if it can be run from the library or only from main - only from main
if __name__ == "__main__":
    main()
