import pygame

#initialize pygame - call the constructor
pygame.init()

#colors
BLUE = (  0,   0, 255)
RED = (255, 0 , 0)
YELLOW = (255, 255,   0)
 

#set the font
font = pygame.font.Font('freesansbold.ttf', 20)
#caption
pygame.display.set_caption("Memory game")


#screen object to display
#resolution = (0,0) tuple - immutable data structure
BOARDWIDTH = 2
BOARDHEIGHT = 2
TILEWIDTH = 150
TILEHEIGHT = 150
SCREEN = pygame.display.set_mode((TILEWIDTH*BOARDWIDTH, TILEHEIGHT*BOARDHEIGHT))

