#DAY 1
"""
New concepts-
1. Split into smaller functions
2. main will call init and drawboard
3. Initially move drawboard to a function and don't call it
    Call wont happen
    Call it from main()
    Move update to main - since display.update needs to happen always.
      It was happening always since the it was called directly before
4. Move all definitions before the function call
5. HOMEWORK: WChange BOARDWIDTH and BOARDHEIGHT to 3 and check
6. Advanced Homework: Check BOARDWIDTH*BOARDHEIGHT = should be even
    2*2 = 2 pairs = 4
    2*3 = 3 pairs = 6
    2*4 = 4 pairs = 8
    3*4 = 6 pairs = 12
    3*6 = 9 pairs = 18
    TODO: Use ASSERT
    Can't be 3*3
"""
###################################IMPORTS#################################
import pygame
import os
###################################IMPORTS#################################


###################################CONSTANTS#################################
#colors
BLUE = (  0,   0, 255)
RED = (255, 0 , 0)
YELLOW = (255, 255,   0)
PINK   = (255,   0, 255)

###################################MODULARITY#################################
#change it to 3 and check
BOARDWIDTH = 2
BOARDHEIGHT = 2
###################################MODULARITY#################################

TILEWIDTH = 150
TILEHEIGHT = 150

#so that changing BGCOLOR to CYAN say, will require only changes
#in this section and not elsewhere
BGCOLOR = BLUE
TILECOLOR = PINK
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
