#Import statements are to enable the code to use the functions from the library
import pygame
import sys
import os
import random

#instructions to windows to center the game window in the center of
#the screen, which it might ignore
os.environ["SDL_VIDEO_CENTERED"] = "1"

#initialize pygame
pygame.init()

#Right way
SCREENWIDTH = 500
SCREENHEIGHT = 500
SCREENSIZE = [SCREENWIDTH, SCREENHEIGHT]
SCREEN = pygame.display.set_mode(SCREENSIZE)

#caption for the game
pygame.display.set_caption("My first game in pygame")

RADIUS = 20
ZEROINTENSITY = 0
MAXINTENSITY = 255

COLOR = (random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY))
YPOS = 40
XPOS = 40
POS = (XPOS, YPOS)
circlerect = pygame.draw.circle(SCREEN, COLOR, POS, RADIUS)
pygame.display.update(circlerect)

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Here for any commands inside the for loop  
        if (events.type == pygame.KEYDOWN) and (events.key == pygame.K_SPACE):
            COLOR = (random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY))
            #note- we have skipped the last parameter and by default, 0 is taken
            pygame.draw.circle(SCREEN, COLOR, POS, RADIUS)
            pygame.display.update(circlerect)
    #beware of the positioning of this line. It should be inside the while
    #for all the commands that need to be executed inside the while
    
