#DAY 4

"""
New concepts-
Game over screen
"""
###################################IMPORTS#################################
import pygame
import os
import random
import sys
###################################IMPORTS#################################


###################################CONSTANTS#################################
#colors
BLUE = (  0,   0, 255)
PINK   = (255,   0, 255)
GRAY   = (100,   100, 100)
BLACK = (0, 0, 0)
#Dynamically creating now
RED = (255, 0 , 0)
#YELLOW = (255, 255,   0)
###################################MODULARITY#################################
#change it to 3 and check
BOARDWIDTH = 2
BOARDHEIGHT = 2
#so that changing BGCOLOR to CYAN say, will require only changes
#in this section and not elsewhere
BGCOLOR = BLUE
TILECOLOR = PINK
HIGHLIGHTCOLOR = GRAY
GAMEOVER = BLACK
GAMEOVERTEXT =  RED
###################################MODULARITY#################################
#Need only colors in pairs of 2
PAIR = 2
RANGEOFPAIRS = int((BOARDWIDTH*BOARDHEIGHT)/PAIR)

COLORRANGEMIN = 0
COLORRANGEMAX = 255

TILEWIDTH = 150
TILEHEIGHT = 150
TILEBORDER = 4

BGIMAGE = 'cglogobg.png'
TILEIMAGE = 'soccer-icon.png'
BGMUSIC = 'background.mp3'
GOMUSIC = 'gameover.mp3'

TILEHIDDEN = 0
TILEREVEALED =  1

#margins so that tiles dont stick to each other
XMARGIN = 5
YMARGIN = 5
#On left and right and top and bottom
GAP = 2

#Music
INFINITE = -1
ONCE = 0
###################################CONSTANTS#################################

###################################PLAY MUSIC#################################
def playMusic(time):
    """
    Play music - infinite or once parameter
    """
    pygame.mixer.music.play(time)
###################################PLAY MUSIC#################################

###################################INIT#################################
def init(revealedBoxes, board):
    """
    Initialize the black screen with tile, font and screen size
    """
    #made BASICFONT global for game over screen drawing
    global SCREEN, CGBACKGROUND, TILELOGO, BASICFONT
    #initialize pygame - call the constructor
    pygame.init()

    
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    
    #set the font
    BASICFONT = pygame.font.Font('freesansbold.ttf', 20)
    #caption
    pygame.display.set_caption("Memory game")


    #screen object to display
    #resolution = (0,0) tuple - immutable data structure
    SCREEN = pygame.display.set_mode((TILEWIDTH*BOARDWIDTH, TILEHEIGHT*BOARDHEIGHT))

    #Move loading of images to init since it need not be repeated during the game
    CGBACKGROUND = pygame.image.load(BGIMAGE)
    TILELOGO = pygame.image.load(TILEIMAGE)

    #Draw the board with tiles
    drawBoard(revealedBoxes, board)

    #Music
    pygame.mixer.music.load(BGMUSIC)
    playMusic(INFINITE)
    
    #do this to display on the screen, else you see a black screen always
    pygame.display.update()
###################################INIT#################################

###################################BOARDRECT#################################
def rectCoord(left, top):
    """
    Board coordinates, sizes of TILEWIDTH, TILEHEIGHT
    """
    rect = (left, top, TILEWIDTH*BOARDWIDTH, TILEHEIGHT*BOARDHEIGHT)
    return rect
###################################BOARDRECT#################################
    
###################################DRAWMAINBOARD#################################
def drawMainBoard():
    """
    Draw the board with the back ground image
    """
    #center the background image
    rect = rectCoord(0, 0)
    rectObject = pygame.draw.rect(SCREEN,BGCOLOR,rect)
    rectObject = CGBACKGROUND.get_rect(center=rectObject.center)

    #draw a surface onto another
    SCREEN.blit(CGBACKGROUND, rectObject)
###################################DRAWMAINBOARD#################################

###################################TILERECT#################################
def tileCoord(row, col):
    """
    Leave a margin of XMARGIN and YMARGIN, so that it does not merge with the corners
    And make the tile smaller than TILEWIDTH and TILEHEIGHT symmetrically
    By giving a gap of XMARGIN and YMARGIN on both sides - *2
    """
    rect = ( ((col*TILEWIDTH)+XMARGIN), ((row*TILEHEIGHT)+YMARGIN),TILEWIDTH-(GAP*XMARGIN),TILEHEIGHT-(GAP*YMARGIN))
    return rect
###################################TILERECT#################################

###################################RECOGNIZE TILE ON#################################
def getTileOn(mousex, mousey):
    """
    Given mouse coordinates return row, col of the tile clicked
    Return None if no tile clicked
    """
    for row in range(BOARDHEIGHT):
        for col in range(BOARDWIDTH):
            #Same used while drawing the logo
            #REUSE - 2
            rect = tileCoord(row, col)
            #REUSE - 2
            rectObject = pygame.Rect(rect)
            if rectObject.collidepoint(mousex, mousey):
                return(row, col)
    return (None, None)
###################################RECOGNIZE TILE ON#################################

###################################HIGHLIGHT RECT#################################
def highlightCoord(row, col):
    """
    Highlight rect given row, col
    """
    left = ((col*TILEWIDTH))
    top = ((row*TILEHEIGHT))
    width = TILEWIDTH
    height = TILEHEIGHT
    rectHighlight = (left, top, width, height)
    return rectHighlight
###################################HIGHLIGHT RECT#################################

###################################HIGHLIGHT TILE#################################
def highlightTile(row, col):
    """
    Highlight the box
    """
    rectHighlight = highlightCoord(row, col)
    pygame.draw.rect(SCREEN, HIGHLIGHTCOLOR, rectHighlight, TILEBORDER)
###################################HIGHLIGHT TILE#################################
    
###################################DRAWTILES#################################
def drawTiles(revealedBoxes, board):
    """
    Loop through and draw all the tiles, none of the tiles revealed
    No error till revealed tiles are being flipped
    drawRevealTiles is called - and drawBoard is called in the while
    And it re-flips all - need to flip only only not revealed
    """
    for row in range(BOARDHEIGHT):
        for col in range(BOARDWIDTH):
            #rect starting position
            rect = tileCoord(row, col)

            if revealedBoxes[row][col]:
                rectObject = pygame.draw.rect(SCREEN, board[row][col], rect)
            else:
                rectObject = pygame.draw.rect(SCREEN, TILECOLOR, rect)
                #Logo to the center of the tile
                rectObject = TILELOGO.get_rect(center = rectObject.center)
                SCREEN.blit(TILELOGO, rectObject)
###################################DRAWTILES################################

###################################DRAWBOARD#################################
def drawBoard(revealedBoxes, board):
    """
    Draw the board with background and n*n tiles
    """
    #draw the main board
    drawMainBoard()
    #draw tiles
    drawTiles(revealedBoxes, board)
###################################DRAWBOARD#################################

###################################REVEALTILES#################################
def drawRevealTiles(board, row, col):
    """
    Reveal the tile clicked - Update since tile needs to be redrawn 
    """
    rect = tileCoord(row, col)
    print("Revealed tile rect = {}".format(rect))
    print("color of tile  = {}".format(board[row][col]))
    pygame.draw.rect(SCREEN, board[row][col], rect, 0)
    #update it when - you need to display for a second before flipping
    pygame.display.update()
    pygame.time.wait(1000)
###################################REVEALTILES#################################

###################################BOARD DATA STRUCTURE#################################
def createRandomBoardDS():
    """
    Create board data structure
    """

    ###################################Works only for 2*2#################################
    colorarr = []
    #need 2 distinct random colors - sample will give me two
    #range does not use the upper limit 0 to < RANGEOFPAIRS
    ##color1, color2 = random.sample(range(0, RANGEOFPAIRS), 2)
    ##colorarr.append(ALLCOLORS[color1])
    ##colorarr.append(ALLCOLORS[color2])
    ###################################Works only for 2*2#################################

    ###################################Works for all#################################
    #How do you make color1, color2 and colorn dynamic? 
    #Returns a list of 3 unique colors
    colormap = random.sample(range(0, RANGEOFPAIRS), RANGEOFPAIRS)
    print(colormap)
    ###################################Works only for all#################################
    
    #highly unlikely that all three colors are the same
    colorlist = []
    for colors in colormap:
        colorlist.append((random.randint(COLORRANGEMIN,COLORRANGEMAX), random.randint(COLORRANGEMIN,COLORRANGEMAX), random.randint(COLORRANGEMIN,COLORRANGEMAX)))
    print(colorlist)
    

    #Pair it up to make BOARDWIDTH*BOARDHEIGHT
    #colorlist has RANGEOFPAIRS
    copylist = list(colorlist)
    #merge both into colorarr
    colorlist = colorlist + copylist
    print("Non - Random array of {} colors = {}".format(BOARDWIDTH*BOARDHEIGHT, colorlist))
    random.shuffle(colorlist)
    print("Random array of {} colors = {}".format(BOARDWIDTH*BOARDHEIGHT, colorlist))

    #data structure 2 dim - list of lists
    #2 image for 4 tiles - randomly distribute
    #new DS to store 2 copies of 2 randomly generated images/colors
    #nested loop will just pick from this new array
    board = []
    colorcount = 0
    for col in range(BOARDWIDTH):
        columnarr = []
        for row in range(BOARDHEIGHT):
            columnarr.append(colorlist[colorcount])
            colorcount+=1
        board.append(columnarr)
    return board
###################################BOARD DATA STRUCTURE#################################

###################################REVEALED BOX DATA STRUCTURE#################################
def revealedBoxesDS(revealedOrNot):
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        #0 is that it is not revealed
        revealedBoxes.append([revealedOrNot] * BOARDHEIGHT)
    return revealedBoxes
###################################REVEALED BOX DATA STRUCTURE#################################

###################################CHECK GAME OVER#################################
def gameOver(revealedBoxes):
    print("in game over func")
    boolWon = True
    #Check if all have been revealed
    for col in range(BOARDWIDTH):
        for row in range(BOARDHEIGHT):
            if(revealedBoxes[row][col] == False):
                boolWon = False
    return boolWon
###################################CHECK GAME OVER#################################

###################################GAME OVER SCREEN#################################
def gameOverScreen(revealedBoxes, board):
    pygame.mixer.music.stop()
    
    print("drawing game over screen")
    #Draw the game over screen and handle clicks here
    drawMainBoard()

    sprite = pygame.sprite.Sprite()
    sprite.image = CGBACKGROUND
    sprite.rect = CGBACKGROUND.get_rect()
    
    print("drawing text")
    textSurf = BASICFONT.render("Game Over!Continue?", True, GAMEOVERTEXT, GAMEOVER)
    
    sprite.image.blit(textSurf, sprite.rect)        
    print("drawing text")
    #Display and play - it is not doing anything till it plays
    #Playing music behaves like a wait - long wait
    pygame.mixer.music.load(GOMUSIC)
    playMusic(ONCE)
    print("play music once is over")
    pygame.time.wait(100000)
    pygame.mixer.music.stop()
    
###################################GAME OVER SCREEN#################################

###################################MAIN#################################
def main():
    """
    The controller
    """
    #Form the data structures
    board = createRandomBoardDS()
    revealedBoxes = revealedBoxesDS(TILEHIDDEN)

    #recognise game over, for identifying the event for game over continue click
    isGameOver =  False 
    
    #Call init - has draw board with tiles - has initial update of screen 
    init(revealedBoxes, board)

    #To know if the tile is the first selection
    firstSelection = None
    
    ###################################WHILE STARTS#################################
    #continuously monitor
    while True:
        boolMouseCicked = False
        ###################################FIRST REUSE#################################
        #Draw the board again so that highlighting is gone - 
        drawBoard(revealedBoxes, board)
        ###################################FIRST REUSE#################################
        
        ##########Event management#######################################
        for event in pygame.event.get():
            #(quit and mouse) up or (esc and key up)
            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key==pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                #print("mouse moved to another tile")
                mousex,mousey = event.pos
            elif event.type == pygame.MOUSEBUTTONUP and isGameOver == True:
                mousex,mousey = event.pos
                #set game over to false here before drawing the new board
                isGameOver =  False 
                drawBoard(revealedBoxes, board)
                #Start background music again
                print("load the bg music")
                pygame.mixer.music.load(BGMUSIC)
                playMusic(INFINITE)
                isGameOver = False
            elif event.type == pygame.MOUSEBUTTONUP:
                #print("clicked the mouse")
                boolMouseCicked = True
        ##########Event management OVER #######################################

        #Get row, col of tile clicked
        row, col = getTileOn(mousex, mousey)

        ##########Tile click logic #######################################
        if(row != None and col != None):
            #If not revealed - highlight
            if not revealedBoxes[row][col]:
                highlightTile(row, col)
            if not revealedBoxes[row][col] and boolMouseCicked:
                drawRevealTiles(board, row, col)
                #update data structure
                revealedBoxes[row][col] = TILEREVEALED
                
                if firstSelection ==  None:
                    #The current tile clicked is the first selection
                    firstSelection = (row, col)
                else:
                    #This is the second
                    #Check if game is over or need to flip it back
                    if(board[firstSelection[0]][firstSelection[1]] == board[row][col]):
                        #If the second selction is same as first selection's color
                        #Check if Game is over
                        if(gameOver(revealedBoxes) == True):
                            #Game over display and music
                            #Not required till play music and all come into picture
                            revealedBoxes = revealedBoxesDS(TILEHIDDEN)
                            board = createRandomBoardDS()
                            isGameOver = True
                            gameOverScreen(revealedBoxes, board) 
                        #else:
                            #Just let the flip remain
                    else:
                        #Flip it back
                        #Reset revealed DS
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[row][col] = False
                    #This is the second selection
                    #Reset first selection
                    firstSelection =  None

        ##########Tile click logic OVER #######################################

            
        #do this to update display on the screen
        pygame.display.update()
    ###################################WHILE ENDS#################################
    
###################################MAIN#################################


if __name__ == '__main__':
    main()
