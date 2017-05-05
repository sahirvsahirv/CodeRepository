#DAY 1
"""
1. 2-dim array to maintain the colors in each tile
2. Randomize the colors so that you get 2 unique pairs
3. Print the board on command line
4. HOMEWORK: expand it to BOARDWIDTH*BOARDHEIGHT being even
"""
#TODO: Read up on the different algorithms to do this

import random

RED = (255, 0 , 0)
YELLOW = (255, 255,   0)

#The program should work by changing it to 3
BOARDWIDTH = 2
BOARDHEIGHT = 2

COLORRANGEMIN = 0
COLORRANGEMAX = 255

#Need only colors in pairs of 2
PAIR = 2
RANGEOFPAIRS = int((BOARDWIDTH*BOARDHEIGHT)/PAIR)


#color tuple
ALLCOLORS = (RED, YELLOW)

###################################BOARD DATA STRUCTURE#################################
def createRandomBoardDS():
    """
    Create board data structure
    """

    ###################################Works only for 2*2#################################
    colorarr = []
    #need 2 distinct random colors - sample will give me two
    #range does not use the upper limit 0 to < RANGEOFPAIRS
    ##color1, color2 = random.sample(range(0, RANGEOFPAIRS), 2)
    ##colorarr.append(ALLCOLORS[color1])
    ##colorarr.append(ALLCOLORS[color2])
    ###################################Works only for 2*2#################################

    ###################################Works for all#################################
    #How do you make color1, color2 and colorn dynamic? 
    #Returns a list of 3 unique colors
    colormap = random.sample(range(0, RANGEOFPAIRS), RANGEOFPAIRS)
    print(colormap)
    ###################################Works only for all#################################
    
    #highly unlikely that all three colors are the same
    colorlist = []
    for colors in colormap:
        colorlist.append((random.randint(COLORRANGEMIN,COLORRANGEMAX), random.randint(COLORRANGEMIN,COLORRANGEMAX), random.randint(COLORRANGEMIN,COLORRANGEMAX)))
    print(colorlist)
    

    #Pair it up to make BOARDWIDTH*BOARDHEIGHT
    #colorlist has RANGEOFPAIRS
    copylist = list(colorlist)
    #merge both into colorarr
    colorlist = colorlist + copylist
    print("Non - Random array of {} colors = {}".format(BOARDWIDTH*BOARDHEIGHT, colorlist))
    random.shuffle(colorlist)
    print("Random array of {} colors = {}".format(BOARDWIDTH*BOARDHEIGHT, colorlist))

    #data structure 2 dim - list of lists
    #2 image for 4 tiles - randomly distribute
    #new DS to store 2 copies of 2 randomly generated images/colors
    #nested loop will just pick from this new array
    board = []
    colorcount = 0
    for col in range(BOARDWIDTH):
        columnarr = []
        for row in range(BOARDHEIGHT):
            columnarr.append(colorlist[colorcount])
            colorcount+=1
        board.append(columnarr)
    return board
###################################BOARD DATA STRUCTURE#################################

if __name__ == '__main__':
    board = createRandomBoardDS()
    print("Board = {}".format(board))
