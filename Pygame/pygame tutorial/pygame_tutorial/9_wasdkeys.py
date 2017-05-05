#Import statements are to enable the code to use the functions from the library
import pygame
import sys
import os
import random
from pygame.locals import *

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

X = 40
Y = 40
CIRCLEPOS = (X, Y)
COLOR = (random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY))
circlerect = pygame.draw.circle(SCREEN, COLOR, CIRCLEPOS, RADIUS)
pygame.display.update(circlerect)

BLACK = (0,0,0)

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Here for any commands inside the for loop
        #if (events.type == pygame.KEYDOWN) and (events.key == pygame.K_SPACE):
        if (events.type == pygame.MOUSEBUTTONDOWN):
            COLOR = (random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY))
            #note- we have skipped the last parameter and by default, 0 is taken
            circlerect = pygame.draw.circle(SCREEN, COLOR, CIRCLEPOS, RADIUS)
            pygame.display.update(circlerect)
    #beware of the positioning of this line. It should be inside the while
    #for all the commands that need to be executed inside the while

    user_input = pygame.key.get_pressed()
    
    if(user_input[pygame.K_UP] or user_input[pygame.K_w]):
        Y=Y-1
        if(Y<0):Y=SCREENHEIGHT
    elif(user_input[pygame.K_DOWN] or user_input[pygame.K_s]):
        Y=Y+1
        if(Y>SCREENHEIGHT):Y=0
    elif(user_input[pygame.K_LEFT] or user_input[pygame.K_a]):
        X=X-1
        if(X<0):X=SCREENWIDTH
    elif(user_input[pygame.K_RIGHT] or user_input[pygame.K_d]):
        X=X+1
        if(X>SCREENWIDTH):X=0
    CIRCLEPOS = (X,Y)
    #exits the borders reposition

    SCREEN.fill(BLACK)
    circlerect = pygame.draw.circle(SCREEN, COLOR, CIRCLEPOS, RADIUS)
    pygame.display.update()
