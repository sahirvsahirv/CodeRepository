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
        #Do it once
        #SCREEN.fill(BLACK)
        blitrocketrect = SCREEN.blit(self.image, (self.rect.x, self.rect.y))
        #pygame.display.update()
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

#uncomment - for drawing with sprite group
rocket_group = pygame.sprite.Group()
rocket_group.add(rocket)

#Do it once
#rocket.draw_updatescreen()
#rocket_group.draw(SCREEN)


ZEROINTENSITY = 0
MAXINTENSITY = 255
RADIUS = 20

#Getting the surface of the drawn circle and finding collisions is difficult
#hence will have to change it to an image
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #Not required - tried for collision
        #screensurf = pygame.Surface([SCREENWIDTH, SCREENHEIGHT])
        
        # Draw the circle
        COLOR = (random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY))
        circlerect = pygame.draw.circle(SCREEN, COLOR, (x,y), RADIUS)
        self.color = COLOR
        #Ignore as of now - for collision - not happening
        #self.image = pygame.Surface((x+20,y+20)).convert_alpha()

        #convert_alpha is required
        self.image = SCREEN.convert_alpha()
        self.rect = self.image.get_rect()
        self.circlerect = circlerect
        #blit - we don't need blitting here since we are using a group to draw
        #SCREEN.blit(self.image, circlerect)
        

NOOFWALLS = 4
XMIN = 50
XMAX = SCREENWIDTH-100
YMIN = 50
YMAX = SCREENHEIGHT-100

wall_group=pygame.sprite.Group()
for i in range(0, NOOFWALLS):
    wall = Wall(random.randrange(XMIN, XMAX, 40), random.randrange(YMIN,YMAX, 20))
    wall_group.add(wall)

#Do it once
#pygame.display.update()
#wall_group.draw(SCREEN)

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if (events.type == pygame.MOUSEBUTTONDOWN):
            rocket.rotate(ANGLE)
            #Method 1
            #rocket.draw_updatescreen()
            #Method 2 - commented out
            rocket_group.draw(SCREEN)
            
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

    SCREEN.fill(BLACK)
    wall_group.draw(SCREEN)
    
    rocket.update(X,Y)
    rocket.draw_updatescreen()
    #Method 2
    #rocket_group.draw(SCREEN)
    
    pygame.display.update()    


    
