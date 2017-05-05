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

ANGLE = 90
BLACK = (0,0,0)

#The rocket - the actor/sprite that moves with arrows/WASD
class Rocket(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #Horizontal
        #self.vertical = 1
    def draw_updatescreen(self):
        SCREEN.fill(BLACK)
        blitrocketrect = SCREEN.blit(self.image, (self.rect.x, self.rect.y))
        pygame.display.update()
    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)
    def update(self, x, y):
        self.rect.x =  x
        self.rect.y =  y
        
#This group has only one sprite
X = 40
Y = 40
SPRITENAME = 'rocket.png'
rocket = Rocket(SPRITENAME, X, Y)
rocket.draw_updatescreen()

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if (events.type == pygame.MOUSEBUTTONDOWN):
            rocket.rotate(ANGLE)
            rocket.draw_updatescreen()
            
    #Inside while, a single tab space from while
    user_input = pygame.key.get_pressed()
    if(user_input[pygame.K_UP]):
        Y=Y-1
        if(Y<0):Y=SCREENHEIGHT
    elif(user_input[pygame.K_DOWN]):
        Y=Y+1
        if(Y>SCREENHEIGHT):Y=0
    elif(user_input[pygame.K_LEFT]):
        X=X-1
        if(X<0):X=SCREENWIDTH
    elif(user_input[pygame.K_RIGHT]):
        X=X+1
        if(X>SCREENWIDTH):X=0

    rocket.update(X,Y)
    rocket.draw_updatescreen()    
