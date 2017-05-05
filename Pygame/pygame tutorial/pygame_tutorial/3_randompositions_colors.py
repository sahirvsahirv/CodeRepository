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

#500, 500 = width and height of the square shaped window on which the game can be played
#putting [500,500] in square brackets means that it is a list.
#A list is a data structure. In layman terms, it is a bag in which you can
#store the width and height of the rectangle together.

#"screen", is the handle that you always use to draw on the window. Hence remember the name

#The width and height ideally should be variables and assigned values in the
#beginning of the code. If later you need to use the same [500,500] again or
#want to change it to [300, 550], you can do it by changing the value of the
#variable at one location, instead of changing the number 500 to 300 at multiple
#places.
#And ideally these are constants, whose values you dont change during in the code
#Hence the variables are written in capital letters
#There is no "const" keyword in python (keywords are special words recognised by the
#programming language like "for", "if", "while" etc)

#Not the right way
#screen = pygame.display.set_mode([500, 500])

#Right way
SCREENWIDTH = 500
SCREENHEIGHT = 500
SCREENSIZE = [SCREENWIDTH, SCREENHEIGHT]
SCREEN = pygame.display.set_mode(SCREENSIZE)

#caption for the game
pygame.display.set_caption("My first game in pygame")

#arc, circle, line, polygon etc
#The left top corner of the screen is considered to be the position for (0,0)
#With respect to that we give the left, top coordinates
LENGTH = 20
WIDTH = 20
RADIUS = 20

LOOPCOUNT = 100
MINPOS = 0
MAXPOS = 480

ZEROINTENSITY = 0
MAXINTENSITY = 255

SOLID = 0
for i in range(LOOPCOUNT):
    LEFT = random.randint(MINPOS,MAXPOS)
    TOP = random.randint(MINPOS,MAXPOS)
    rect1 = pygame.Rect(LEFT, TOP, LENGTH, WIDTH)

    COLOR = (random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY))
    
    pygame.draw.rect(SCREEN, COLOR, rect1, SOLID)

    
    CIRCLEPOS = (random.randint(MINPOS,MAXPOS), random.randint(MINPOS,MAXPOS)) 
    pygame.draw.circle(SCREEN, COLOR, CIRCLEPOS, RADIUS, SOLID)
    
pygame.display.update()

#The while loop, which keeps running for ever (becaue we have "while True")
#In computer systems, there is always an event loop always checking for user inputs
#(It keeps checking for key presses on the key board and whenever for example, "caps lock"
#is preseed all the letters you trype are printed in upper case.

#Similarly, an event loop which runs the code over and over again for ever, till
#you choose to quit is required in pygame.
#In that loop, you check for all events in the bag of events, like key presses,quit etc
#and take the right action

#here we shall first handle the "quit" event, when the "X" button is pressed on the
#pygame screen
#when it is pressed we want to exit pygame and close the window (sys.exit())
while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            #till sys.exit() is not mentioned, it will not end the program
            #but pygame has quit, hence the for loop to get events from pygame
            #will fail and hence will get an error if program does not exit
            sys.exit()
        #Here for any commands inside the for loop  
    
    #beware of the positioning of this line. It should be inside the while
    #for all the commands that need to be executed inside the while
