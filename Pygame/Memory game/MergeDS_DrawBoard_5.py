#DAY 1
"""
New concepts-
1. Merge code
"""
###################################IMPORTS#################################
import pygame
import os
import random
###################################IMPORTS#################################


###################################CONSTANTS#################################
#colors
BLUE = (  0,   0, 255)
PINK   = (255,   0, 255)
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
###################################MODULARITY#################################
#Need only colors in pairs of 2
PAIR = 2
RANGEOFPAIRS = int((BOARDWIDTH*BOARDHEIGHT)/PAIR)

COLORRANGEMIN = 0
COLORRANGEMAX = 255

TILEWIDTH = 150
TILEHEIGHT = 150

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
    global SCREEN
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
###################################INIT#################################



###################################DRAWBOARD#################################
def drawBoard():
    """
    Draw the board with background and n*n tiles
    """
    #draw the board
    cgbackground = pygame.image.load(BGIMAGE)
    tilelogo = pygame.image.load(TILEIMAGE)

    #center the background image
    rect = (0, 0, TILEWIDTH*BOARDWIDTH, TILEHEIGHT*BOARDHEIGHT )
    rectObject = pygame.draw.rect(SCREEN,BGCOLOR,rect)
    rectObject = cgbackground.get_rect(center=rectObject.center)

    #draw a surface onto another
    SCREEN.blit(cgbackground, rectObject)

    #draw tiles
    #TODO: Move to a function drawing tiles with logo
    #Draw the board without revealed boxes
    for row in range(BOARDHEIGHT):
        for col in range(BOARDWIDTH):
            #rect starting position
            rect = ( ((col*TILEWIDTH)+XMARGIN), ((row*TILEHEIGHT)+YMARGIN),TILEWIDTH-(GAP*XMARGIN),TILEHEIGHT-(GAP*YMARGIN))
            rectObject = pygame.draw.rect(SCREEN, TILECOLOR, rect)
            #Logo to the center of the tile
            rectObject = tilelogo.get_rect(center = rectObject.center)
            SCREEN.blit(tilelogo, rectObject)
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
    #Call init
    init()
    #Call draw board
    drawBoard()
    
    #do this to display on the screen, else you see a black screen always
    pygame.display.update()
###################################MAIN#################################


if __name__ == '__main__':
    main()
