"""
New concepts-
1. Move "main" to a function
2. __main__ call for execution from command line and not imported from a library
3. global: declare global inside the function, so that it is visible throughout the program
4. Nested loops
5. Tile should be smaller than the tile size by XMARGIN and YMARGIN
    Get the point left, top
    ((col*TILEWIDTH)+XMARGIN), ((row*TILEHEIGHT)+YMARGIN),TILEWIDTH-(GAP*XMARGIN),TILEHEIGHT-(GAP*YMARGIN))
6. SCREEN.blit - to redraw on the image, logo already drawn
7. center the logo
8. Update the display for the tiles to be seen
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

BOARDWIDTH = 2
BOARDHEIGHT = 2
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




###################################MAIN#################################
def main():
    """
    The controller
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
###################################MAIN#################################


if __name__ == '__main__':
    main()


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

#do this to display on the screen, else you see a black screen always
pygame.display.update()
