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
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        #Not required - tried for collision
        #screensurf = pygame.Surface([SCREENWIDTH, SCREENHEIGHT])

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
                

NOOFWALLS = 4
XMIN = 50
XMAX = SCREENWIDTH-100
YMIN = 50
YMAX = SCREENHEIGHT-100

WALLNAME = 'football.png'

wall_group=pygame.sprite.Group()
for i in range(0, NOOFWALLS):
    wall = Wall(WALLNAME, random.randrange(XMIN, XMAX, 40), random.randrange(YMIN,YMAX, 20))
    wall_group.add(wall)

#Do it once
#pygame.display.update()
#wall_group.draw(SCREEN)

#Play music infintely till the game runs
MUSICFILE = "background_music.mp3"
INFINITE = -1
pygame.mixer.music.load(MUSICFILE)
pygame.mixer.music.play(INFINITE)

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
    
    #sprite collide is for sprites in a group
    for circle in wall_group:
       if(rocket.rect.colliderect(circle.rect)):
            print("collision  :  " + str(id(circle)))
            wall_group.remove(circle)
            wall_group.draw(SCREEN)
            
    pygame.display.update()

    GAMEOVER = "Game Over"
    FONTNAME = 'freesansbold.ttf'
    GAMEOVERTXTCOLOR = (150, 150, 150)
    CENTERSCREENPOS = (250, 250)
    SCOREFILENAME = "gamescores.txt"
    FILEMODE = "w"
    FILETEXT = "Cannons burst = {}"
    ERRORMSG = "could not handle file"
    GAMEOVERMUSIC = "gameover.mp3"
    PLAYONCE = 0
    if(len(wall_group.sprites()) == 0):
        print("game over")
        pygame.mixer.music.stop()
        pygame.mixer.music.load(GAMEOVERMUSIC)
        pygame.mixer.music.play(PLAYONCE)
        try:
            #delete the file
            save_file = open(SCOREFILENAME, FILEMODE)
            save_file.write(FILETEXT.format(NOOFWALLS))
            save_file.close()
        except IOError:
            print(ERRORMSG)
        SCREEN.fill(BLACK)
        font = pygame.font.Font(FONTNAME, 30)
        text_surface = font.render(GAMEOVER, True, GAMEOVERTXTCOLOR)
        text_rect = text_surface.get_rect()
        text_rect.center = CENTERSCREENPOS
        SCREEN.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(5000)
        pygame.quit()
        sys.exit()
    
