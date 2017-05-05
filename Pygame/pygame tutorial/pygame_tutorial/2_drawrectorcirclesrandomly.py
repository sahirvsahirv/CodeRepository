import pygame
import sys
import os

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
LEFT = 100
TOP = 100
LENGTH = 20
WIDTH = 20
RECTCOORD = [LEFT, TOP, LENGTH, WIDTH]
rect1 = pygame.Rect(RECTCOORD)

RED = 255
YELLOW = 230
BLUE = 200
COLOR = (RED, YELLOW, BLUE)

#0 is fully thick
#2 is little, try 10, which is equivalent to 0
pygame.draw.rect(SCREEN, COLOR, rect1, 2)

LEFT = 20
TOP = 20
RECTCOORD = [LEFT, TOP, LENGTH, WIDTH]
rect2 = pygame.Rect(RECTCOORD)
#hollow
pygame.draw.rect(SCREEN, COLOR, rect2, 0)

LEFT = 200
TOP = 200
RADIUS = 20
pygame.draw.circle(SCREEN, COLOR, (LEFT,TOP), RADIUS,0)

#pygame.display.flip()
#update is more powerful, has the capacity to update only the rect
#instead of the whole screen

#pygame.display.update(rect1)
#pygame.display.update(rect2)
            
#Update without a parameter is same as flip
#pygame.display.update()
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



