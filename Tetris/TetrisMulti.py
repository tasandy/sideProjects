import random, time, pygame, sys
from pygame.locals import *
from random import randint

#Defining my FPS and everything that relies on it
FPS = float(60)
MOVESIDEWAYSRATE = 14/FPS
MOVEDOWNRATE = 14/FPS
LOCKRATE = 30/FPS
WAITRATE = 50/FPS
LINECLEARRATE = 41/FPS
G = 3/FPS

#Defining the dimensions of my screen and board
WIDTH = 720
HEIGHT = 480
BSIZE = 20
BWIDTH = 10
BHEIGHT = 20
P1XMARGIN = int((WIDTH - BWIDTH * BSIZE) / 10)
P2XMARGIN = int((WIDTH - BWIDTH * BSIZE) / 4 * 3)
TOPMARGIN = HEIGHT - (BHEIGHT * BSIZE) - 5

#Defining all of my colours used using RGB
WHITE = (255, 255, 255)
GRAY = (185, 185, 185)
BLACK = (0.0, 0.0, 0.0)
AQUA = (0.0, 240, 240)
LAQUA = (179, 251, 251)
MAQUA = (0.0, 216, 216)
DAQUA = (0.0, 120, 120)
GREEN = (0.0, 240, 0.0)
LGREEN = (179, 251, 179)
MGREEN = (0.0, 216, 0.0)
DGREEN = (0.0, 120, 0.0)
BLUE = (0.0, 0.0, 240)
LBLUE = (179, 179, 251)
MBLUE = (0.0, 0.0, 216)
DBLUE = (0.0, 0.0, 120)
PURPLE = (160, 0.0, 240)
LPURPLE = (227, 179, 251)
MPURPLE = (144, 0.0, 216)
DPURPLE = (80, 0.0, 120)
ORANGE = (240, 160, 0.0)
LORANGE = (251, 227, 179)
MORANGE = (216, 144, 0.0)
DORANGE = (120, 80, 0.0)
RED = (240, 0.0, 0.0)
LRED = (251, 179, 179)
MRED = (216, 0.0, 0.0)
DRED = (120, 0.0, 0.0)
YELLOW = (240, 240, 0.0)
LYELLOW = (251, 251, 179)
MYELLOW = (216, 216, 0.0)
DYELLOW = (120, 120, 0.0)

#Defining colour groups
COLOURS = [AQUA, GREEN, BLUE, PURPLE, ORANGE, RED, YELLOW]
LCOLOURS = [LAQUA, LGREEN, LBLUE, LPURPLE, LORANGE, LRED, LYELLOW]
MCOLOURS = [MAQUA, MGREEN, MBLUE, MPURPLE, MORANGE, MRED, MYELLOW]
DCOLOURS = [DAQUA, DGREEN, DBLUE, DPURPLE, DORANGE, DRED, DYELLOW]

#Making sure the colour groups are the same length
assert len(COLOURS) == len(LCOLOURS) and len(DCOLOURS) == \
       len(MCOLOURS) and len(COLOURS) == len(DCOLOURS)

#I make a group of groups, so I can randomize my background colour
COL = [COLOURS, LCOLOURS, MCOLOURS, DCOLOURS]

#I define my tetrinomes; the blocks being used
TWIDTH = 5
THEIGHT = 5
BLANK = "X"

T_BLOCK = [["XXXXX",
            "XXXXX",
            "XOOOX",
            "XXOXX",
            "XXXXX"],
           ["XXXXX",
            "XXOXX",
            "XOOXX",
            "XXOXX",
            "XXXXX"],
           ["XXXXX",
            "XXOXX",
            "XOOOX",
            "XXXXX",
            "XXXXX"],
           ["XXXXX",
            "XXOXX",
            "XXOOX",
            "XXOXX",
            "XXXXX"]]

Z_BLOCK = [["XXXXX",
            "XXXXX",
            "XOOXX",
            "XXOOX",
            "XXXXX"],
           ["XXXXX",
            "XXOXX",
            "XOOXX",
            "XOXXX",
            "XXXXX"]]

J_BLOCK = [["XXXXX",
            "XXXXX",
            "XOOOX",
            "XXXOX",
            "XXXXX"],
           ["XXXXX",
            "XXOXX",
            "XXOXX",
            "XOOXX",
            "XXXXX"],
           ["XXXXX",
            "XOXXX",
            "XOOOX",
            "XXXXX",
            "XXXXX"],
           ["XXXXX",
            "XXOOX",
            "XXOXX",
            "XXOXX",
            "XXXXX"]]

S_BLOCK = [["XXXXX",
            "XXXXX",
            "XXOOX",
            "XOOXX",
            "XXXXX"],
           ["XXXXX",
            "XXOXX",
            "XXOOX",
            "XXXOX",
            "XXXXX"]]

L_BLOCK = [["XXXXX",
            "XXXXX",
            "XOOOX",
            "XOXXX",
            "XXXXX"],
           ["XXXXX",
            "XOOXX",
            "XXOXX",
            "XXOXX",
            "XXXXX"],
           ["XXXXX",
            "XXXOX",
            "XOOOX",
            "XXXXX",
            "XXXXX"],
           ["XXXXX",
            "XXOXX",
            "XXOXX",
            "XXOOX",
            "XXXXX"]]

I_BLOCK = [["XXXXX",
            "XXXXX",
            "OOOOX",
            "XXXXX",
            "XXXXX"],
           ["XXOXX",
            "XXOXX",
            "XXOXX",
            "XXOXX",
            "XXXXX"]]

O_BLOCK = [["XXXXX",
            "XXXXX",
            "XOOXX",
            "XOOXX",
            "XXXXX"]]

PIECES = {0: T_BLOCK,
          1: Z_BLOCK,
          2: J_BLOCK,
          3: S_BLOCK,
          4: L_BLOCK,
          5: I_BLOCK,
          6: O_BLOCK,
          }

#Main method
def main():
    #Some global variables; font sizes and the screen
    global SCREEN, SFONT, MFONT, LFONT, BCOLOUR
    pygame.init()
    #I define those global variables
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    SFONT = pygame.font.SysFont("verdana", 18)
    MFONT = pygame.font.SysFont("times", 35)
    LFONT = pygame.font.SysFont("verdana", 100)
    GHOST = COL[randint(0,3)]
    BCOLOUR = GHOST[randint(0,6)]
    pygame.display.set_caption("Tetris")
    #I create a list of the last 4 used blocks
    p1List = [7, 7, 7, 7]
    p2List = [7, 7, 7, 7]
    p1InitialPiece = getNewPiece(p1List)
    p2InitialPiece = getNewPiece(p2List)
    p1GrandMaster = False
    p2GrandMaster = False
    #I add all of the graphical pieces shown at boot-up
    addNewPiece(p1InitialPiece, 1)
    addNewPiece(p2InitialPiece, 2)
    addBoard(getNewBoard(), 1)
    addBoard(getNewBoard(), 2)
    addStatus(0, 0, 0, 1)
    addStatus(0, 0, 0, 2)
    addRank(0, 1)
    addRank(0, 2)
    addTextScreen("Tetris")
    #I start the game loop; I have three different endings for a game depending on your skill
    while True:
        p1Level, p2Level, p1InitialPiece, p2InitialPiece, p1GrandMaster, p2GrandMaster \
                 = runGame(p1InitialPiece, p2InitialPiece, p1List, p2List, p1GrandMaster, p2GrandMaster)
        if p1GrandMaster and p2GrandMaster:
            addTextScreen("DOUBLE GRAND MASTER!!!")
        elif p1Level > 999 and not p1GrandMaster and p2GrandMaster:
            addTextScreen("P2 GRAND MASTER!!! P1 WIN!")
        elif p2Level > 999 and p1GrandMaster and not p2GrandMaster:
            addTextScreen("P1 GRAND MASTER!!! P2 WIN!")
        elif p1Level > 999 and p2Level > 999:
            addTextScreen("DOUBLE WIN!!!")
        elif p1Level > p2Level:
            addTextScreen("P1 WINS!")
        elif p1Level < p2Level:
            addTextScreen("P2 WINS!")
        else:
            addTextScreen("YOU TIED!!!")

#runGame() starts the game and runs the game
#Takes an initial piece, the used block list, and the grand master check
def runGame(p1InitialPiece, p2InitialPiece, p1List, p2List, p1GrandMaster, p2GrandMaster):
    #Set-up variables; the background image, a bunch of check times \
    #boolean check variables, scoring integers, etc.
    bimage = randint(0,20)
    p1Board = getNewBoard()
    p2Board = getNewBoard()
    startTime = time.time()
    p1LastMoveDownTime = time.time()
    p2LastMoveDownTime = time.time()
    p1LastMoveSidewaysTime = time.time()
    p2LastMoveSidewaysTime = time.time()
    p1LastFallTime = time.time()
    p2LastFallTime = time.time()
    p1LastLockTime = time.time()
    p2LastLockTime = time.time()
    p1GhostFallTime = time.time()
    p2GhostFallTime = time.time()
    p1WaitTime = time.time()
    p2WaitTime = time.time()
    p1SoftTime = time.time()
    p2SoftTime = time.time()
    p1MovingDown = False
    p2MovingDown = False
    p1MovingLeft = False
    p2MovingLeft = False
    p1MovingRight = False
    p2MovingRight = False
    p1InstantDrop = False
    p2InstantDrop = False
    p1GhostLeft = False
    p2GhostLeft = False
    p1GhostRight = False
    p2GhostRight = False
    p1Lock = False
    p2Lock = False
    p1gm1 = False
    p2gm1 = False
    p1gm2 = False
    p2gm2 = False
    p1gm3 = False
    p2gm3 = False
    p1Play = True
    p2Play = True
    p1LockY = 0
    p2LockY = 0
    p1Level = 1
    p2Level = 1
    p1DropNum = 1
    p2DropNum = 1
    p1Combo = 1
    p2Combo = 1
    p1Bravo = 1
    p2Bravo = 1
    p1Soft = 0
    p2Soft = 0
    p1Score = 0
    p2Score = 0
    p1RemovedLines = 0
    p2RemovedLines = 0
    p1BaseLevel, p1FallRate, p1DropNum = getLevel(p1Level)
    p2BaseLevel, p2FallRate, p2DropNum = getLevel(p2Level)
    #I plop the first piece down
    p1FallingPiece = p1InitialPiece
    p2FallingPiece = p2InitialPiece
    p1NewPiece = getNewPiece(p1List)
    p2NewPiece = getNewPiece(p2List)

    #The game loop
    while True:
        #Once a piece has landed I calculate the score, check the gm requirements, and reset some variables
        if p1FallingPiece == None and p1Play:
            p1Score += ((p1Level + p1RemovedLines)/4 + p1Soft) * p1RemovedLines * p1Combo * p1Bravo
            if p1BaseLevel == 400 and p1Score >= 12000 and (time.time() - startTime <= 255) and not p1gm1:
                p1gm1 = True
            if p1BaseLevel == 600 and p1Score >= 40000 and (time.time() - startTime <= 420) and not p1gm2:
                p1gm2 = True
            if p1BaseLevel == 1100 and p1Score >= 126000 and (time.time() - startTime <= 810) and not p1gm3:
                p1gm3 = True
            if p1gm1 and p1gm2 and p1gm3:
                p1GrandMaster = True
            p1WaitTime = time.time()
            p1LastMoveSidewaysTime = time.time()
            p1LastFallTime = time.time()
            p1GhostFallTime = time.time()
            p1WaitTime = time.time()
            p1SoftTime = time.time()
            p1Soft = 0
            #I create a new block, put it at the top
            p1FallingPiece = p1NewPiece
            p1NewPiece = getNewPiece(p1List)
            #Due to the fall delay I implemented, I move the piece horizontally if it should have beforehand
            if p1MovingRight and isTruePosition(p1Board, p1FallingPiece, adjX=1):
                p1FallingPiece["x"] += 1
            if p1MovingLeft and isTruePosition(p1Board, p1FallingPiece, adjX=-1):
                p1FallingPiece["x"] -= 1
            #If the game is over, I switch a variable to show they aren't playing
            if not isTruePosition(p1Board, p1FallingPiece) or p1Level > 999:
                p1Play = False
            #This makes sure a player can get to a new hundreds of levels by only plopping a block down
            if p1Level % 100 != 99:
                p1Level += 1

        #Once a piece has landed I calculate the score, check the gm requirements, and reset some variables
        if p2FallingPiece == None and p2Play:
            p2Score += ((p2Level + p2RemovedLines)/4 + p2Soft) * p2RemovedLines * p2Combo * p2Bravo
            if p2BaseLevel == 400 and p2Score >= 12000 and (time.time() - startTime <= 255) and not p2gm1:
                p2gm1 = True
            if p2BaseLevel == 600 and p2Score >= 40000 and (time.time() - startTime <= 420) and not p2gm2:
                p2gm2 = True
            if p2BaseLevel == 1100 and p2Score >= 126000 and (time.time() - startTime <= 810) and not p2gm3:
                p2gm3 = True
            if p2gm1 and p2gm2 and p2gm3:
                p2GrandMaster = True
            p2WaitTime = time.time()
            p2LastMoveSidewaysTime = time.time()
            p2LastFallTime = time.time()
            p2GhostFallTime = time.time()
            p2WaitTime = time.time()
            p2SoftTime = time.time()
            p2Soft = 0
            #I create a new block, put it at the top
            p2FallingPiece = p2NewPiece
            p2NewPiece = getNewPiece(p2List)
            #Due to the fall delay I implemented, I move the piece horizontally if it should have beforehand
            if p2MovingRight and isTruePosition(p2Board, p2FallingPiece, adjX=1):
                p2FallingPiece["x"] += 1
            if p2MovingLeft and isTruePosition(p2Board, p2FallingPiece, adjX=-1):
                p2FallingPiece["x"] -= 1
            #If the game is over, I switch a variable to show they aren't playing
            if not isTruePosition(p2Board, p2FallingPiece) or p2Level > 999:
                p2Play = False
            #This makes sure a player can get to a new hundreds of levels by only plopping a block down
            if p2Level % 100 != 99:
                p2Level += 1        

        #Checks to see both people are finished playing and returns if they are
        if not p1Play and not p2Play:
            return p1Level, p2Level, p1InitialPiece, p2InitialPiece, p1GrandMaster, p2GrandMaster

        #Drawing all of the screen's elements
        BACKGROUND = background("images/" + str(bimage) + ".jpg", [0,0])
        SCREEN.fill([255, 255, 255])
        SCREEN.blit(BACKGROUND.image, BACKGROUND.rect)
        addBoard(p1Board, 1)
        addBoard(p2Board, 2)
        addStatus(p1Score, p1Level, p1BaseLevel, 1)
        addStatus(p2Score, p2Level, p2BaseLevel, 2)
        addNewPiece(p1NewPiece, 1)
        addNewPiece(p2NewPiece, 2)
        addRank(p1Score, 1)
        addRank(p2Score, 2)
        if p1FallingPiece != None:
            addPiece(p1FallingPiece, 1)
        if p2FallingPiece != None:
            addPiece(p2FallingPiece, 2)
        pygame.display.update()
            
        checkQuit()
        #Loop for handling events
        for event in pygame.event.get():
            if event.type == KEYUP:
                #Pauses game until a button is pressed
                if (event.key == K_p):
                    addTextScreen("Paused")
                    p1LastFallTime = time.time()
                    p2LastFallTime = time.time()
                    p1LastMoveDownTime = time.time()
                    p2LastMoveDownTime = time.time()
                    p1LastMoveSidewaysTime = time.time()
                    p2LastMoveSidewaysTime = time.time()
                #Stops moving the block left and realligns some variables
                elif (event.key == K_a):
                    p1MovingLeft = False
                    p1GhostLeft = False
                    p1LastFallTime = p1GhostFallTime
                    if p1GhostRight:
                        p1MovingRight = True
                        p1LastMoveSidewaysTime = time.time()
                        if p1MovingRight and isTruePosition(p1Board, p1FallingPiece, adjX=1):
                            p1FallingPiece["x"] += 1
                elif (event.key == K_LEFT):
                    p2MovingLeft = False
                    p2GhostLeft = False
                    p2LastFallTime = p2GhostFallTime
                    if p2GhostRight:
                        p2MovingRight = True
                        p2LastMoveSidewaysTime = time.time()
                        if p2MovingRight and isTruePosition(p2Board, p2FallingPiece, adjX=1):
                            p2FallingPiece["x"] += 1
                #Stops moving the block right and realligns some variables
                elif (event.key == K_d):
                    p1MovingRight = False
                    p1GhostRight = False
                    p1LastFallTime = p1GhostFallTime
                    if p1GhostLeft:
                        p1MovingLeft = True
                        p1LastMoveSidewaysTime = time.time()
                        if p1MovingLeft and isTruePosition(p1Board, p1FallingPiece, adjX=-1):
                            p1FallingPiece["x"] -= 1
                elif (event.key == K_RIGHT):
                    p2MovingRight = False
                    p2GhostRight = False
                    p2LastFallTime = p2GhostFallTime
                    if p2GhostLeft:
                        p2MovingLeft = True
                        p2LastMoveSidewaysTime = time.time()
                        if p2MovingLeft and isTruePosition(p2Board, p2FallingPiece, adjX=-1):
                            p2FallingPiece["x"] -= 1
                
                #Declares tracking variables false
                elif (event.key == K_s):
                    p1MovingDown = False
                elif (event.key == K_DOWN):
                    p2MovingDown = False
                elif (event.key == K_w):
                    p1InstantDrop = False
                elif (event.key == K_UP):
                    p2InstantDrop = False
                    
            if time.time() - p1WaitTime <= WAITRATE:
                if event.type == KEYDOWN:
                    #For the freeze at the top; sets up the horizontal variables ahead of time
                    if (event.key == K_a) and isTruePosition(p1Board, p1FallingPiece, adjX=-1):
                        p1MovingLeft = True
                        p1MovingRight = False
                        p1GhostLeft = True
                    elif (event.key == K_LEFT) and isTruePosition(p2Board, p2FallingPiece, adjX=-1):
                        p2MovingLeft = True
                        p2MovingRight = False
                        p2GhostLeft = True
                        
            if time.time() - p2WaitTime <= WAITRATE:
                if event.type == KEYDOWN:
                    if (event.key == K_d) and isTruePosition(p1Board, p1FallingPiece, adjX=1):
                        p1MovingRight = True
                        p1MovingLeft = False
                        p1GhostRight = True
                    elif (event.key == K_RIGHT) and isTruePosition(p2Board, p2FallingPiece, adjX=1):
                        p2MovingRight = True
                        p2MovingLeft = False
                        p2GhostRight = True
                        
            if time.time() - p1WaitTime > WAITRATE and p1Play:
                if event.type == KEYDOWN:
                    #Moves the block left if valid
                    if (event.key == K_a) and isTruePosition(p1Board, p1FallingPiece, adjX=-1):
                        p1FallingPiece["x"] -= 1
                        p1MovingLeft = True
                        p1MovingRight = False
                        p1GhostLeft = True
                        p1LastMoveSidewaysTime = time.time()
                    #Moves the block right if valid
                    elif (event.key == K_d) and isTruePosition(p1Board, p1FallingPiece, adjX=1):
                        p1FallingPiece["x"] += 1
                        p1MovingRight = True
                        p1MovingLeft = False
                        p1GhostRight = True
                        p1LastMoveSidewaysTime = time.time()
                    #Rotating the block CW if valid; checks to see if it can be pushed one space to the left or right if necessary
                    elif (event.key == K_c or event.key == K_b):
                        p1FallingPiece["rotation"] = (p1FallingPiece["rotation"] + 1) % len(PIECES[p1FallingPiece["shape"]])
                        if not isTruePosition(p1Board, p1FallingPiece):
                            if isTruePosition(p1Board, p1FallingPiece, adjX=1):
                                p1FallingPiece["x"] += 1
                            if isTruePosition(p1Board, p1FallingPiece, adjX=-1):
                                p1FallingPiece["x"] -= 1
                        if not isTruePosition(p1Board, p1FallingPiece):
                            p1FallingPiece["rotation"] = (p1FallingPiece["rotation"] - 1) % len(PIECES[p1FallingPiece["shape"]])
                    #Same thing but CCW
                    elif (event.key == K_v):
                        p1FallingPiece["rotation"] = (p1FallingPiece["rotation"] - 1) % len(PIECES[p1FallingPiece["shape"]])
                        if not isTruePosition(p1Board, p1FallingPiece):
                            if isTruePosition(p1Board, p1FallingPiece, adjX=1):
                                p1FallingPiece["x"] += 1
                            if isTruePosition(p1Board, p1FallingPiece, adjX=-1):
                                p1FallingPiece["x"] -= 1
                        if not isTruePosition(p1Board, p1FallingPiece):
                            p1FallingPiece["rotation"] = (p1FallingPiece["rotation"] + 1) % len(PIECES[p1FallingPiece["shape"]])
                    #Makes the block go down faster; tallies up soft time and locks it at the bottom
                    elif (event.key == K_s):
                        p1MovingDown = True
                        p1SoftTime = time.time()
                        if isTruePosition(p1Board, p1FallingPiece, adjY=1):
                            p1FallingPiece["y"] += 1
                        p1LastMoveDownTime = time.time()
                        if not isTruePosition(p1Board, p1FallingPiece, adjY=1):
                            p1Lock = True
                            p1LastLockTime = time.time() - LOCKRATE
                            p1LastFallTime = time.time() - p1FallRate
                    #Drops the block to the bottom
                    elif (event.key == K_w):
                        p1MovingDown = False
                        p1InstantDrop = True
                        
            if time.time() - p2WaitTime > WAITRATE and p2Play:
                if event.type == KEYDOWN:
                    #Moves the block left if valid
                    if (event.key == K_LEFT) and isTruePosition(p2Board, p2FallingPiece, adjX=-1):
                        p2FallingPiece["x"] -= 1
                        p2MovingLeft = True
                        p2MovingRight = False
                        p2GhostLeft = True
                        p2LastMoveSidewaysTime = time.time()
                    #Moves the block right if valid
                    elif (event.key == K_RIGHT) and isTruePosition(p2Board, p2FallingPiece, adjX=1):
                        p2FallingPiece["x"] += 1
                        p2MovingRight = True
                        p2MovingLeft = False
                        p2GhostRight = True
                        p2LastMoveSidewaysTime = time.time()
                    #Rotating the block CW if valid; checks to see if it can be pushed one space to the left or right if necessary
                    elif (event.key == K_COMMA or event.key == K_SLASH):
                        p2FallingPiece["rotation"] = (p2FallingPiece["rotation"] + 1) % len(PIECES[p2FallingPiece["shape"]])
                        if not isTruePosition(p2Board, p2FallingPiece):
                            if isTruePosition(p2Board, p2FallingPiece, adjX=1):
                                p2FallingPiece["x"] += 1
                            if isTruePosition(p2Board, p2FallingPiece, adjX=-1):
                                p2FallingPiece["x"] -= 1
                        if not isTruePosition(p2Board, p2FallingPiece):
                            p2FallingPiece["rotation"] = (p2FallingPiece["rotation"] - 1) % len(PIECES[p2FallingPiece["shape"]])
                    #Same thing but CCW
                    elif (event.key == K_PERIOD):
                        p2FallingPiece["rotation"] = (p2FallingPiece["rotation"] - 1) % len(PIECES[p2FallingPiece["shape"]])
                        if not isTruePosition(p2Board, p2FallingPiece):
                            if isTruePosition(p2Board, p2FallingPiece, adjX=1):
                                p2FallingPiece["x"] += 1
                            if isTruePosition(p2Board, p2FallingPiece, adjX=-1):
                                p2FallingPiece["x"] -= 1
                        if not isTruePosition(p2Board, p2FallingPiece):
                            p2FallingPiece["rotation"] = (p2FallingPiece["rotation"] + 1) % len(PIECES[p2FallingPiece["shape"]])
                    #Makes the block go down faster; tallies up soft time and locks it at the bottom
                    elif (event.key == K_DOWN):
                        p2MovingDown = True
                        p2SoftTime = time.time()
                        if isTruePosition(p2Board, p2FallingPiece, adjY=1):
                            p2FallingPiece["y"] += 1
                        p2LastMoveDownTime = time.time()
                        if not isTruePosition(p2Board, p2FallingPiece, adjY=1):
                            p2Lock = True
                            p2LastLockTime = time.time() - LOCKRATE
                            p2LastFallTime = time.time() - p2FallRate
                    #Drops the block to the bottom
                    elif (event.key == K_UP):
                        p2MovingDown = False
                        p2InstantDrop = True
                        
        if time.time() - p1WaitTime > WAITRATE and p1Play:                   
            #Same comment as above; checks to see how low the block can go
            if p1InstantDrop:
                for i in range(1, BHEIGHT):
                    if not isTruePosition(p1Board, p1FallingPiece, adjY=i):
                        break
                p1FallingPiece["y"] += i - 1
            #I set up a block lock or unlock the piece depending on if it can move down
            if not isTruePosition(p1Board, p1FallingPiece, adjY=1) and not p1Lock and not (p1LockY == p1FallingPiece["y"]):
                p1Lock = True
                p1LastLockTime = time.time()
            if isTruePosition(p1Board, p1FallingPiece, adjY=1):
                p1Lock = False
                p1LockY = p1FallingPiece["y"]
            #I tally up the soft count
            if p1MovingDown and time.time() - p1SoftTime > 1/FPS:
                p1Soft += 1
                p1SoftTime = time.time()
    
            #Handles moving the block horizontally
            if (p1MovingLeft or p1MovingRight) and (time.time() - p1LastMoveSidewaysTime > MOVESIDEWAYSRATE or time.time() - p1LastMoveSidewaysTime == 0):
                if p1MovingLeft and isTruePosition(p1Board, p1FallingPiece, adjX=-1):
                    p1FallingPiece["x"] -= 1
                elif p1MovingRight and isTruePosition(p1Board, p1FallingPiece, adjX=1):
                    p1FallingPiece["x"] += 1
                else:
                    p1LastFallTime = p1GhostFallTime
    
            #Handles the fall delay when moving horizontally
            if (p1MovingLeft and isTruePosition(p1Board, p1FallingPiece, adjX=-1)) or (p1MovingRight and isTruePosition(p1Board, p1FallingPiece, adjX=1)):
                p1LastFallTime = time.time()
            if p1MovingDown and (time.time() - p1LastMoveDownTime > MOVEDOWNRATE or time.time() - p1LastMoveDownTime == 0) and isTruePosition(p1Board, p1FallingPiece, adjY=1):
                p1FallingPiece["y"] += 1
    
            #Check if it's time for the block to fall
            if time.time() - p1LastFallTime > p1FallRate:
                #See if it can go any lower
                if not isTruePosition(p1Board, p1FallingPiece, adjY=1):
                    if time.time() - p1LastLockTime > LOCKRATE:
                        #Stick the block on the board if it can't descend
                        addToBoard(p1Board, p1FallingPiece)
                        p1RemovedLines, p1Level, p1Combo, p1Bravo = removeWholeLines(p1Board, p1Level, p1Combo, p1Bravo)
                        p1BaseLevel, p1FallRate, p1DropNum = getLevel(p1Level)
                        p1FallingPiece = None
                #Block can go lower
                else:
                    #I account for different difficulties
                    if p1DropNum > 1:
                        for i in range(0, p1DropNum):
                            if isTruePosition(p1Board, p1FallingPiece, adjY=p1DropNum-i):
                                p1FallingPiece["y"] += p1DropNum - i
                                break
                    else:
                        p1FallingPiece["y"] += 1
                    #I reset a few fall times
                    p1LastFallTime = time.time()
                    p1GhostFallTime = time.time()
                        
        if time.time() - p2WaitTime > WAITRATE and p2Play:                   
            #Same comment as above; checks to see how low the block can go
            if p2InstantDrop:
                for i in range(1, BHEIGHT):
                    if not isTruePosition(p2Board, p2FallingPiece, adjY=i):
                        break
                p2FallingPiece["y"] += i - 1
            #I set up a block lock or unlock the piece depending on if it can move down
            if not isTruePosition(p2Board, p2FallingPiece, adjY=1) and not p2Lock and not (p2LockY == p2FallingPiece["y"]):
                p2Lock = True
                p2LastLockTime = time.time()
            if isTruePosition(p2Board, p2FallingPiece, adjY=1):
                p2Lock = False
                p2LockY = p2FallingPiece["y"]
            #I tally up the soft count
            if p2MovingDown and time.time() - p2SoftTime > 1/FPS:
                p2Soft += 1
                p2SoftTime = time.time()
    
            #Handles moving the block horizontally
            if (p2MovingLeft or p2MovingRight) and (time.time() - p2LastMoveSidewaysTime > MOVESIDEWAYSRATE or time.time() - p2LastMoveSidewaysTime == 0):
                if p2MovingLeft and isTruePosition(p2Board, p2FallingPiece, adjX=-1):
                    p2FallingPiece["x"] -= 1
                elif p2MovingRight and isTruePosition(p2Board, p2FallingPiece, adjX=1):
                    p2FallingPiece["x"] += 1
                else:
                    p2LastFallTime = p2GhostFallTime
    
            #Handles the fall delay when moving horizontally
            if (p2MovingLeft and isTruePosition(p2Board, p2FallingPiece, adjX=-1)) or (p2MovingRight and isTruePosition(p2Board, p2FallingPiece, adjX=1)):
                p2LastFallTime = time.time()
            if p2MovingDown and (time.time() - p2LastMoveDownTime > MOVEDOWNRATE or time.time() - p2LastMoveDownTime == 0) and isTruePosition(p2Board, p2FallingPiece, adjY=1):
                p2FallingPiece["y"] += 1
    
            #Check if it's time for the block to fall
            if time.time() - p2LastFallTime > p2FallRate:
                #See if it can go any lower
                if not isTruePosition(p2Board, p2FallingPiece, adjY=1):
                    if time.time() - p2LastLockTime > LOCKRATE:
                        #Stick the block on the board if it can't descend
                        addToBoard(p2Board, p2FallingPiece)
                        p2RemovedLines, p2Level, p2Combo, p2Bravo = removeWholeLines(p2Board, p2Level, p2Combo, p2Bravo)
                        p2BaseLevel, p2FallRate, p2DropNum = getLevel(p2Level)
                        p2FallingPiece = None
                #Block can go lower
                else:
                    #I account for different difficulties
                    if p2DropNum > 1:
                        for i in range(0, p2DropNum):
                            if isTruePosition(p2Board, p2FallingPiece, adjY=p2DropNum-i):
                                p2FallingPiece["y"] += p2DropNum - i
                                break
                    else:
                        p2FallingPiece["y"] += 1
                    #I reset a few fall times
                    p2LastFallTime = time.time()
                    p2GhostFallTime = time.time()

#This creates the background; if you noticed up top it randomizes the background
class background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

#This draws the text on the screen
def makeTextObjs(text, font, COLOUR):
    surf = font.render(text, True, COLOUR)
    return surf, surf.get_rect()

#Checks if the position the block wants to move into is actually available
def isTruePosition(board, block, adjX=0, adjY=0):
    #Checks if the block is not colliding and in the board
    for x in range(TWIDTH):
        for y in range(THEIGHT):
            isAboveBoard = y + block["y"] + adjY < 0
            if isAboveBoard or PIECES[block["shape"]][block["rotation"]][y][x] == BLANK:
                continue
            if not ((x + block["x"] + adjX >= 0) and (x + block["x"] + adjX < BWIDTH) and (y + block["y"] + adjY < BHEIGHT)):
                return False
            if board[x + block["x"] + adjX][y + block["y"] + adjY] != BLANK:
                return False
    return True

#Checks to see if the board is cleared
def isClear(board):
    y = BHEIGHT - 1
    for x in range(BWIDTH):
        if board[x][y] != BLANK:
            return False
    return True

#Checks the rank of the player and displays it
def addRank(score, p):
    rank = "S9"
    if score < 120000:
        rank = "S8"
    if score < 100000:
        rank = "S7"
    if score < 82000:
        rank = "S6"
    if score < 66000:
        rank = "S5"
    if score < 52000:
        rank = "S4"
    if score < 40000:
        rank = "S3"
    if score < 30000:
        rank = "S2"
    if score < 22000:
        rank = "S1"
    if score < 16000:
        rank = "1"
    if score < 12000:
        rank = "2"
    if score < 8000:
        rank = "3"
    if score < 5500:
        rank = "4"
    if score < 3500:
        rank = "5"
    if score < 2000:
        rank = "6"
    if score < 1400:
        rank = "7"
    if score < 800:
        rank = "8"
    if score < 400:
        rank = "9"
    rankDisplay = MFONT.render("%s" % rank, True, WHITE)
    rankBlock = rankDisplay.get_rect()
    if p == 1:
        rankBlock.topleft = (WIDTH / 2 - 91, 80)
    if p == 2:
        rankBlock.topleft = (WIDTH - 113, 80)
    SCREEN.blit(rankDisplay, rankBlock)

#Displays text on the screen
def addTextScreen(text):
    #If it's the word Tetris I adjust the height a little
    titleDisplay, titleBlock = makeTextObjs(text, LFONT, WHITE)
    if text != "Tetris":
        titleBlock.center = (int(WIDTH / 2), int(HEIGHT / 2))
    else:
        titleBlock.center = (int(WIDTH / 2) , int(HEIGHT / 4))
    SCREEN.blit(titleDisplay, titleBlock)

    #I draw appropriate additional text
    if text == "Tetris":
        pressKeyDisplay, pressKeyBlock = makeTextObjs("P1: ASD to move, W to instant drop,", SFONT, WHITE)
        pressKeyBlock.center = (int(WIDTH / 2), int(HEIGHT / 4) + 80)
        SCREEN.blit(pressKeyDisplay, pressKeyBlock)
        pressKeyDisplay, pressKeyBlock = makeTextObjs("CVB to rotate. P2: Arrow keys to move,", SFONT, WHITE)
        pressKeyBlock.center = (int(WIDTH / 2), int(HEIGHT / 4) + 105)
        SCREEN.blit(pressKeyDisplay, pressKeyBlock)
        pressKeyDisplay, pressKeyBlock = makeTextObjs("UP to instant drop, ,./ to rotate.", SFONT, WHITE)
        pressKeyBlock.center = (int(WIDTH / 2), int(HEIGHT / 4) + 130)
    else:
        pressKeyDisplay, pressKeyBlock = makeTextObjs("Press any key to continue.", SFONT, WHITE)
        pressKeyBlock.center = (int(WIDTH / 2), int(HEIGHT / 2) + 100)
    SCREEN.blit(pressKeyDisplay, pressKeyBlock)

    while checkForKeyPress() == None:
        pygame.display.update()

#I check the base level, fall rate, and the drop mulitplier of the player
def getLevel(level):
    baseLevel = (int(level / 100) + 1) * 100
    fallRate = G
    dropNum = 20
    if level < 500:
        dropNum = 3
    if level < 450:
        dropNum = 4
    if level < 420:
        dropNum = 5
    if level < 400:
        dropNum = 4
    if level < 360:
        dropNum = 3
    if level < 330:
        dropNum = 2
    if level < 300:
        dropNum = 1
    if level < 251:
        fallRate = G*16/15
    if level < 247:
        fallRate = G*8/7
    if level < 243:
        fallRate = G*16/9
    if level < 239:
        fallRate = G*8/5
    if level < 236:
        fallRate = G*2
    if level < 233:
        fallRate = G*32/13
    if level < 230:
        fallRate = G*32/9
    if level < 220:
        fallRate = G*64/3
    if level < 200:
        fallRate = G*4/3
    if level < 170:
        fallRate = G*8/5
    if level < 160:
        fallRate = G*32/17
    if level < 140:
        fallRate = G*2
    if level < 120:
        fallRate = G*32/15
    if level < 100:
        fallRate = G*32/13
    if level < 90:
        fallRate = G*8/3
    if level < 80:
        fallRate = G*32/9
    if level < 70:
        fallRate = G*16/3
    if level < 60:
        fallRate = G*32/5
    if level < 50:
        fallRate = G*8
    if level < 40:
        fallRate = G*32/3
    if level < 35:
        fallRate = G*16
    if level < 30:
        fallRate = G*64/3
    return baseLevel, fallRate, dropNum

#I draw text conveying information; the score, level, base level
def addStatus(score, level, baseLevel, p):
    scoreDisplay = SFONT.render("Score: %s" % score, True, WHITE)
    scoreBlock = scoreDisplay.get_rect()
    if p == 1:
        scoreBlock.topleft = (WIDTH / 2 - 119, 20)
    if p == 2:
        scoreBlock.topleft = (WIDTH - 111, 20)
    SCREEN.blit(scoreDisplay, scoreBlock)
    #For this and base level, I account for the end of a player's game
    if level > 999:
        levelDisplay = SFONT.render("Level: 999", True, WHITE)
    else:
        levelDisplay = SFONT.render("Level: %s" % level, True, WHITE)
    levelBlock = levelDisplay.get_rect()
    if p == 1:
        levelBlock.topleft = (WIDTH / 2 - 98, 50)
    if p == 2:
        levelBlock.topleft = (WIDTH - 120, 50)
    SCREEN.blit(levelDisplay, levelBlock)

    #Got to have the dividing line for aestetics!
    levelDisplay = SFONT.render("----", True, WHITE)
    levelBlock = levelDisplay.get_rect()
    if p == 1:
        levelBlock.topleft = (WIDTH / 2 - 36, 60)
    if p == 2:
        levelBlock.topleft = (WIDTH - 58, 60)
    SCREEN.blit(levelDisplay, levelBlock)

    if baseLevel > 999:
        baseLevelDisplay = SFONT.render("999", True, WHITE)
    else:
        baseLevelDisplay = SFONT.render("%s" % baseLevel, True, WHITE)
    baseLevelBlock = baseLevelDisplay.get_rect()
    if p == 1:
        baseLevelBlock.topleft = (WIDTH / 2 - 36, 70)
    if p == 2:
        baseLevelBlock.topleft = (WIDTH - 58, 70)
    SCREEN.blit(baseLevelDisplay, baseLevelBlock)

#Returns a random block, making sure it's not a near repeat
def getNewPiece(pList):
    shape = random.choice(list(PIECES.keys()))
    for num in range(0, len(pList)):
        for part in range(0, len(pList)):
            if shape == pList[part]:
                shape = random.choice(list(PIECES.keys()))
    pList.append(shape)
    pList.remove(pList[0])
    newPiece = {"shape": shape,
                "rotation": 0,
                "x": int(BWIDTH / 2) - int(TWIDTH / 2),
                "y": -2,
                "COLOUR": shape}
    return newPiece

#Fills in the board based on the last block that fell
def addToBoard(board, block):
    for x in range(TWIDTH):
        for y in range(THEIGHT):
            if PIECES[block["shape"]][block["rotation"]][y][x] != BLANK:
                board[x + block["x"]][y + block["y"]] = block["COLOUR"]

#Creates a new board
def getNewBoard():
    board = []
    for i in range(BWIDTH):
        board.append([BLANK] * BHEIGHT)
    return board

#Draws the board; the boarder and translucent background of the "Tetris" area
def addBoard(board, p):
    if p == 1:
        pygame.draw.rect(SCREEN, BCOLOUR, (P1XMARGIN - 3, TOPMARGIN - 3, (BWIDTH * BSIZE) + 6, (BHEIGHT * BSIZE) + 6), 5)
    if p == 2:
        pygame.draw.rect(SCREEN, BCOLOUR, (P2XMARGIN - 3, TOPMARGIN - 3, (BWIDTH * BSIZE) + 6, (BHEIGHT * BSIZE) + 6), 5)
    bg = pygame.Surface((BSIZE * BWIDTH, BSIZE * BHEIGHT), pygame.SRCALPHA)
    bg.fill((0, 0, 0, 128))
    if p == 1:
        SCREEN.blit(bg, (P1XMARGIN, TOPMARGIN))
    if p == 2:
        SCREEN.blit(bg, (P2XMARGIN, TOPMARGIN))
    for x in range(BWIDTH):
        for y in range(BHEIGHT):
            addBox(x, y, p, board[x][y])

#Checks if a line is filled with blocks
def isWholeLine(board, y):
    for x in range(BWIDTH):
        if board[x][y] == BLANK:
            return False
    return True

#Removed completed lines, moves them down, and calculates some score multipliers
def removeWholeLines(board, level, combo, bravo):
    numLinesRemoved = 0
    y = BHEIGHT - 1
    while y >= 0:
        if isWholeLine(board, y):
            for pullDownY in range(y, 0, -1):
                for x in range(BWIDTH):
                    board[x][pullDownY] = board[x][pullDownY-1]
            for x in range(BWIDTH):
                board[x][0] = BLANK
            numLinesRemoved += 1
        else:
            y -= 1
    combo += (2 * numLinesRemoved) - 2
    if not numLinesRemoved:
        combo = 1
        bravo = 1
    if isClear(board):
        bravo = 4
    level += numLinesRemoved
    return numLinesRemoved, level, combo, bravo

#Check for a key press and differentiates a KEYUP from KEYDOWN
def checkForKeyPress():
    checkQuit()
    for event in pygame.event.get([KEYDOWN, KEYUP]):
        if event.type == KEYDOWN:
            continue
        return event.key
    return None

#I add the framework of a block; the backbones
def addPiece(block, p, pixelx=None, pixely=None):
    shapeToDraw = PIECES[block["shape"]][block["rotation"]]
    if pixelx == None and pixely == None:
        pixelx, pixely = convertCoords(block["x"], block["y"], p)
    for x in range(TWIDTH):
        for y in range(THEIGHT):
            if shapeToDraw[y][x] != BLANK:
                addBox(None, None, p, block["COLOUR"], pixelx + (x * BSIZE), pixely + (y * BSIZE))

#Draws the next piece on the sidebar
def addNewPiece(block, p):
    nextDisplay = SFONT.render("Next:", True, WHITE)
    nextBlock = nextDisplay.get_rect()
    if p == 1:
        nextBlock.topleft = (WIDTH / 2 - 81, 125)
    if p == 2:
        nextBlock.topleft = (WIDTH - 103, 125)
    SCREEN.blit(nextDisplay, nextBlock)
    if p == 1:
        addPiece(block, p, pixelx=WIDTH/2-81, pixely=130)
    if p == 2:
        addPiece(block, p, pixelx=WIDTH-103, pixely=130)

#Converts the xy coords of the board the xy coords on the location of the screen
def convertCoords(boxx, boxy, p):
    if p == 1:
        return (P1XMARGIN + (boxx * BSIZE)), (TOPMARGIN + (boxy * BSIZE))
    if p == 2:
        return (P2XMARGIN + (boxx * BSIZE)), (TOPMARGIN + (boxy * BSIZE))

#Draws a single block out of 4, including all of the shading
def addBox(boxx, boxy, p, COLOUR, pixelx=None, pixely=None):
    if COLOUR == BLANK:
        return
    if pixelx == None and pixely == None:
        pixelx, pixely = convertCoords(boxx, boxy, p)
    pygame.draw.rect(SCREEN, MCOLOURS[COLOUR], (pixelx + 1, pixely + 4, BSIZE - 1, BSIZE - 7))
    pygame.draw.rect(SCREEN, COLOURS[COLOUR], (pixelx + 4, pixely + 4, BSIZE - 7, BSIZE - 7))
    pygame.draw.rect(SCREEN, LCOLOURS[COLOUR], (pixelx + 1, pixely + 1, BSIZE - 1, 3))
    pygame.draw.rect(SCREEN, DCOLOURS[COLOUR], (pixelx + 1, pixely + 17, BSIZE - 1, 3))
    pygame.draw.rect(SCREEN, MCOLOURS[COLOUR], (pixelx + 1, pixely + 2, 1, BSIZE - 3))
    pygame.draw.rect(SCREEN, MCOLOURS[COLOUR], (pixelx + 2, pixely + 3, 1, BSIZE - 5))
    pygame.draw.rect(SCREEN, MCOLOURS[COLOUR], (pixelx + 19, pixely + 2, 1, BSIZE - 3))
    pygame.draw.rect(SCREEN, MCOLOURS[COLOUR], (pixelx + 18, pixely + 3, 1, BSIZE - 5))

#Checks to see if the user wants to quit or not
def checkQuit():
    for event in pygame.event.get(QUIT):
        close()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            close()
        pygame.event.post(event)

#Closes the game
def close():
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
