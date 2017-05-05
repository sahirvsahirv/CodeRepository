#DAY 2

"""
New concepts-
1. Estimate what you need to do to manage events
    Mouse move
    Button clicked
    Identify pairs
    Identify game over
    Identify tile clicked from event coordinates
2. Now imagine, there is lots of re-draawing of the board already done
   Split them into more functions for further re-use
3. If the boxes are revealed, need to maintain a data structure to identify those boxes
4. moved to init
    Loading of images
    Drawing of board
    Updating display
5. On movement - just highlight the tiles
    Identify which box we are on
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
#Dynamically creating now
#RED = (255, 0 , 0)
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

#margins so that tiles dont stick to each other
XMARGIN = 5
YMARGIN = 5
#On left and right and top and bottom
GAP = 2
###################################CONSTANTS#################################



###################################INIT#################################
def init():
    """
    Initialize the black screen with tile, font and screen size
    """
    global SCREEN, CGBACKGROUND, TILELOGO
    #initialize pygame - call the constructor
    pygame.init()

    
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    
    #set the font
    font = pygame.font.Font('freesansbold.ttf', 20)
    #caption
    pygame.display.set_caption("Memory game")


    #screen object to display
    #resolution = (0,0) tuple - immutable data structure
    SCREEN = pygame.display.set_mode((TILEWIDTH*BOARDWIDTH, TILEHEIGHT*BOARDHEIGHT))

    #Move loading of images to init since it need not be repeated during the game
    CGBACKGROUND = pygame.image.load(BGIMAGE)
    TILELOGO = pygame.image.load(TILEIMAGE)

    #Draw the board with tiles
    drawBoard()
    
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
def drawTiles():
    """
    Loop through and draw all the tiles, none of the tiles revealed
    """
    for row in range(BOARDHEIGHT):
        for col in range(BOARDWIDTH):
            #rect starting position
            rect = tileCoord(row, col)
            rectObject = pygame.draw.rect(SCREEN, TILECOLOR, rect)
            #Logo to the center of the tile
            rectObject = TILELOGO.get_rect(center = rectObject.center)
            SCREEN.blit(TILELOGO, rectObject)
###################################DRAWTILES################################

###################################DRAWBOARD#################################
def drawBoard():
    """
    Draw the board with background and n*n tiles
    """
    #draw the main board
    drawMainBoard()
    #draw tiles
    drawTiles()
###################################DRAWBOARD#################################

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



###################################MAIN#################################
def main():
    """
    The controller
    """
    #Call init - has draw board with tiles - has initial update of screen 
    init()

    ###################################WHILE STARTS#################################
    #continuously monitor
    while True:
        boolMouseCicked = False
        ###################################FIRST REUSE#################################
        #Draw the board again so that highlighting is gone - 
        drawBoard()
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
            elif event.type == pygame.MOUSEBUTTONUP:
                #print("clicked the mouse")
                boolMouseCicked = True
        ##########Event management OVER #######################################

        #Get row, col of tile clicked
        row, col = getTileOn(mousex, mousey)

        ##########Tile click logic #######################################
        if(row != None and col != None):
            highlightTile(row, col)
        ##########Tile click logic OVER #######################################
            
        #do this to display on the screen, else you see a black screen always
        pygame.display.update()
    ###################################WHILE ENDS#################################
    
###################################MAIN#################################


if __name__ == '__main__':
    main()
