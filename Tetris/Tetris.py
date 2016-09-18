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
XMARGIN = int((WIDTH - BWIDTH * BSIZE) / 2)
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
    pList = [7, 7, 7, 7]
    initialPiece = getNewPiece(pList)
    grandMaster = False
    #I add all of the graphical pieces shown at boot-up
    addNewPiece(initialPiece)
    addBoard(getNewBoard())
    addStatus(0, 0, 0)
    addRank(0)
    addTextScreen("Tetris")
    #I start the game loop; I have three different endings for a game depending on your skill
    while True:
        level, initialPiece, grandMaster = runGame(initialPiece, pList, grandMaster)
        if level > 999 and not grandMaster:
            addTextScreen("You Win!")
        elif level > 999 and grandMaster:
            addTextScreen("GRAND MASTER!")
        else:
            addTextScreen("Game Over")

#runGame() starts the game and runs the game
#Takes an initial piece, the used block list, and the grand master check
def runGame(initialPiece, pList, grandMaster):
    #Set-up variables; the background image, a bunch of check times \
    #boolean check variables, scoring integers, etc.
    bimage = randint(0,20)
    board = getNewBoard()
    lastMoveDownTime = time.time()
    lastMoveSidewaysTime = time.time()
    lastFallTime = time.time()
    lastLockTime = time.time()
    ghostFallTime = time.time()
    waitTime = time.time()
    softTime = time.time()
    startTime = time.time()
    movingDown = False
    movingLeft = False
    movingRight = False
    instantDrop = False
    ghostLeft = False
    ghostRight = False
    lock = False
    gm1 = False
    gm2 = False
    gm3 = False
    lockY = 0
    level = 1
    dropNum = 1
    combo = 1
    bravo = 1
    soft = 0
    score = 0
    removedLines = 0
    baseLevel, fallRate, dropNum = getLevel(level)
    #I plop the first piece down
    fallingPiece = initialPiece
    newPiece = getNewPiece(pList)

    #The game loop
    while True:
        #Once a piece has landed I calculate the score, check the gm requirements, and reset some variables
        if fallingPiece == None:
            score += ((level + removedLines)/4 + soft) * removedLines * combo * bravo
            if baseLevel == 400 and score >= 12000 and (time.time() - startTime <= 255) and not gm1:
                gm1 = True
            if baseLevel == 600 and score >= 40000 and (time.time() - startTime <= 420) and not gm2:
                gm2 = True
            if baseLevel == 1100 and score >= 126000 and (time.time() - startTime <= 810) and not gm3:
                gm3 = True
            if gm1 and gm2 and gm3:
                grandMaster = True
            waitTime = time.time()
            lastMoveSidewaysTime = time.time()
            lastFallTime = time.time()
            ghostFallTime = time.time()
            waitTime = time.time()
            softTime = time.time()
            soft = 0
            #I create a new block, put it at the top
            fallingPiece = newPiece
            newPiece = getNewPiece(pList)
            #Due to the fall delay I implemented, I move the piece horizontally if it should have beforehand
            if movingRight and isTruePosition(board, fallingPiece, adjX=1):
                fallingPiece["x"] += 1
            if movingLeft and isTruePosition(board, fallingPiece, adjX=-1):
                fallingPiece["x"] -= 1
            #If the game is over, I return
            if not isTruePosition(board, fallingPiece) or level > 999:
                return level, fallingPiece, grandMaster
            #This makes sure a player can get to a new hundreds of levels by only plopping a block down
            if level % 100 != 99:
                level += 1

        #Drawing all of the screen's elements
        BACKGROUND = background("images/" + str(bimage) + ".jpg", [0,0])
        SCREEN.fill([255, 255, 255])
        SCREEN.blit(BACKGROUND.image, BACKGROUND.rect)
        addBoard(board)
        addStatus(score, level, baseLevel)
        addNewPiece(newPiece)
        addRank(score)
        if fallingPiece != None:
            addPiece(fallingPiece)
        pygame.display.update()
            
        checkQuit()
        #Loop for handling events
        for event in pygame.event.get():
            if event.type == KEYUP:
                #Pauses game until a button is pressed
                if (event.key == K_p):
                    addTextScreen("Paused")
                    lastFallTime = time.time()
                    lastMoveDownTime = time.time()
                    lastMoveSidewaysTime = time.time()
                #Stops moving the block left and realligns some variables
                elif (event.key == K_LEFT or event.key == K_a):
                    movingLeft = False
                    ghostLeft = False
                    lastFallTime = ghostFallTime
                    if ghostRight:
                        movingRight = True
                        lastMoveSidewaysTime = time.time()
                        if movingRight and isTruePosition(board, fallingPiece, adjX=1):
                            fallingPiece["x"] += 1
                #Stops moving the block left and realligns some variables
                elif (event.key == K_RIGHT or event.key == K_d):
                    lastFallTime = ghostFallTime
                    movingRight = False
                    ghostRight = False
                    if ghostLeft:
                        movingLeft = True
                        lastMoveSidewaysTime = time.time()
                        if movingLeft and isTruePosition(board, fallingPiece, adjX=-1):
                            fallingPiece["x"] -= 1
                    lastMoveFallTime = lastMoveSidewaysTime
                #Declares tracking variables false
                elif (event.key == K_DOWN or event.key == K_s):
                    movingDown = False
                elif (event.key == K_w or event.key == K_UP):
                    instantDrop = False
            if time.time() - waitTime <= WAITRATE:
                if event.type == KEYDOWN:
                    #For the freeze at the top; sets up the horizontal variables ahead of time
                    if (event.key == K_LEFT or event.key == K_a) and isTruePosition(board, fallingPiece, adjX=-1):
                        movingLeft = True
                        movingRight = False
                        ghostLeft = True
                    elif (event.key == K_RIGHT or event.key == K_d) and isTruePosition(board, fallingPiece, adjX=1):
                        movingRight = True
                        movingLeft = False
                        ghostRight = True
            if time.time() - waitTime > WAITRATE:
                if event.type == KEYDOWN:
                    #Moves the block left if valid
                    if (event.key == K_LEFT or event.key == K_a) and isTruePosition(board, fallingPiece, adjX=-1):
                        fallingPiece["x"] -= 1
                        movingLeft = True
                        movingRight = False
                        ghostLeft = True
                        lastMoveSidewaysTime = time.time()
                    #Moves the block right if valid
                    elif (event.key == K_RIGHT or event.key == K_d) and isTruePosition(board, fallingPiece, adjX=1):
                        fallingPiece["x"] += 1
                        movingRight = True
                        movingLeft = False
                        ghostRight = True
                        lastMoveSidewaysTime = time.time()
                    #Rotating the block CW if valid; checks to see if it can be pushed one space to the left or right if necessary
                    elif (event.key == K_b or event.key == K_m):
                        fallingPiece["rotation"] = (fallingPiece["rotation"] + 1) % len(PIECES[fallingPiece["shape"]])
                        if not isTruePosition(board, fallingPiece):
                            if isTruePosition(board, fallingPiece, adjX=1):
                                fallingPiece["x"] += 1
                            if isTruePosition(board, fallingPiece, adjX=-1):
                                fallingPiece["x"] -= 1
                        if not isTruePosition(board, fallingPiece):
                            fallingPiece["rotation"] = (fallingPiece["rotation"] - 1) % len(PIECES[fallingPiece["shape"]])
                    #Same thing but CCW
                    elif (event.key == K_n):
                        fallingPiece["rotation"] = (fallingPiece["rotation"] - 1) % len(PIECES[fallingPiece["shape"]])
                        if not isTruePosition(board, fallingPiece):
                            if isTruePosition(board, fallingPiece, adjX=1):
                                fallingPiece["x"] += 1
                            if isTruePosition(board, fallingPiece, adjX=-1):
                                fallingPiece["x"] -= 1
                        if not isTruePosition(board, fallingPiece):
                            fallingPiece["rotation"] = (fallingPiece["rotation"] + 1) % len(PIECES[fallingPiece["shape"]])
                    #Makes the block go down faster; tallies up soft time and locks it at the bottom
                    elif (event.key == K_DOWN or event.key == K_s):
                        movingDown = True
                        softTime = time.time()
                        if isTruePosition(board, fallingPiece, adjY=1):
                            fallingPiece["y"] += 1
                        lastMoveDownTime = time.time()
                        if not isTruePosition(board, fallingPiece, adjY=1):
                            lock = True
                            lastLockTime = time.time() - LOCKRATE
                            lastFallTime = time.time() - fallRate
                    #Drops the block to the bottom
                    elif (event.key == K_w or event.key == K_UP):
                        movingDown = False
                        instantDrop = True
                        
        if time.time() - waitTime > WAITRATE:                   
            #Same comment as above; checks to see how low the block can go
            if instantDrop:
                for i in range(1, BHEIGHT):
                    if not isTruePosition(board, fallingPiece, adjY=i):
                        break
                fallingPiece["y"] += i - 1
            #I set up a block lock or unlock the piece depending on if it can move down
            if not isTruePosition(board, fallingPiece, adjY=1) and not lock and not (lockY == fallingPiece["y"]):
                lock = True
                lastLockTime = time.time()
            if isTruePosition(board, fallingPiece, adjY=1):
                lock = False
                lockY = fallingPiece["y"]
            #I tally up the soft count
            if movingDown and time.time() - softTime > 1/FPS:
                soft += 1
                softTime = time.time()
    
            #Handles moving the block horizontally
            if (movingLeft or movingRight) and (time.time() - lastMoveSidewaysTime > MOVESIDEWAYSRATE or time.time() - lastMoveSidewaysTime == 0):
                if movingLeft and isTruePosition(board, fallingPiece, adjX=-1):
                    fallingPiece["x"] -= 1
                elif movingRight and isTruePosition(board, fallingPiece, adjX=1):
                    fallingPiece["x"] += 1
                else:
                    lastFallTime = ghostFallTime
    
            #Handles the fall delay when moving horizontally
            if (movingLeft and isTruePosition(board, fallingPiece, adjX=-1)) or (movingRight and isTruePosition(board, fallingPiece, adjX=1)):
                lastFallTime = time.time()
            if movingDown and (time.time() - lastMoveDownTime > MOVEDOWNRATE or time.time() - lastMoveDownTime == 0) and isTruePosition(board, fallingPiece, adjY=1):
                fallingPiece["y"] += 1
    
            #Check if it's time for the block to fall
            if time.time() - lastFallTime > fallRate:
                #See if it can go any lower
                if not isTruePosition(board, fallingPiece, adjY=1):
                    if time.time() - lastLockTime > LOCKRATE:
                        #Stick the block on the board if it can't descend
                        addToBoard(board, fallingPiece)
                        removedLines, level, combo, bravo = removeWholeLines(board, level, combo, bravo)
                        baseLevel, fallRate, dropNum = getLevel(level)
                        fallingPiece = None
                #Block can go lower
                else:
                    #I account for different difficulties
                    if dropNum > 1:
                        for i in range(0, dropNum):
                            if isTruePosition(board, fallingPiece, adjY=dropNum-i):
                                fallingPiece["y"] += dropNum - i
                                break
                    else:
                        fallingPiece["y"] += 1
                    #I reset a few fall times
                    lastFallTime = time.time()
                    ghostFallTime = time.time()
    
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
def addRank(score):
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
    rankBlock.topleft = (WIDTH - 140, 80)
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
        pressKeyDisplay, pressKeyBlock = makeTextObjs("Arrow keys or ASD to move.", SFONT, WHITE)
        pressKeyBlock.center = (int(WIDTH / 2), int(HEIGHT / 4) + 80)
        SCREEN.blit(pressKeyDisplay, pressKeyBlock)
        pressKeyDisplay, pressKeyBlock = makeTextObjs("UP or W to instant drop.", SFONT, WHITE)
        pressKeyBlock.center = (int(WIDTH / 2), int(HEIGHT / 4) + 105)
        SCREEN.blit(pressKeyDisplay, pressKeyBlock)
        pressKeyDisplay, pressKeyBlock = makeTextObjs("BNM to rotate.", SFONT, WHITE)
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
def addStatus(score, level, baseLevel):
    scoreDisplay = SFONT.render("Score: %s" % score, True, WHITE)
    scoreBlock = scoreDisplay.get_rect()
    scoreBlock.topleft = (WIDTH - 168, 20)
    SCREEN.blit(scoreDisplay, scoreBlock)
    #For this and base level, I account for the end of a player's game
    if level > 999:
        levelDisplay = SFONT.render("Level: 999", True, WHITE)
    else:
        levelDisplay = SFONT.render("Level: %s" % level, True, WHITE)
    levelBlock = levelDisplay.get_rect()
    levelBlock.topleft = (WIDTH - 147, 50)
    SCREEN.blit(levelDisplay, levelBlock)

    #Got to have the dividing line for aestetics!
    levelDisplay = SFONT.render("----", True, WHITE)
    levelBlock = levelDisplay.get_rect()
    levelBlock.topleft = (WIDTH - 85, 60)
    SCREEN.blit(levelDisplay, levelBlock)

    if baseLevel > 999:
        baseLevelDisplay = SFONT.render("999", True, WHITE)
    else:
        baseLevelDisplay = SFONT.render("%s" % baseLevel, True, WHITE)
    baseLevelBlock = baseLevelDisplay.get_rect()
    baseLevelBlock.topleft = (WIDTH - 85, 70)
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
def addBoard(board):
    pygame.draw.rect(SCREEN, BCOLOUR, (XMARGIN - 3, TOPMARGIN - 3, (BWIDTH * BSIZE) + 6, (BHEIGHT * BSIZE) + 6), 5)
    bg = pygame.Surface((BSIZE * BWIDTH, BSIZE * BHEIGHT), pygame.SRCALPHA)
    bg.fill((0, 0, 0, 128)) 
    SCREEN.blit(bg, (XMARGIN, TOPMARGIN))
    for x in range(BWIDTH):
        for y in range(BHEIGHT):
            addBox(x, y, board[x][y])

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
def addPiece(block, pixelx=None, pixely=None):
    shapeToDraw = PIECES[block["shape"]][block["rotation"]]
    if pixelx == None and pixely == None:
        pixelx, pixely = convertCoords(block["x"], block["y"])
    for x in range(TWIDTH):
        for y in range(THEIGHT):
            if shapeToDraw[y][x] != BLANK:
                addBox(None, None, block["COLOUR"], pixelx + (x * BSIZE), pixely + (y * BSIZE))

#Draws the next piece on the sidebar
def addNewPiece(block):
    nextDisplay = SFONT.render("Next:", True, WHITE)
    nextBlock = nextDisplay.get_rect()
    nextBlock.topleft = (WIDTH - 120, 125)
    SCREEN.blit(nextDisplay, nextBlock)
    addPiece(block, pixelx=WIDTH-120, pixely=130)

#Converts the xy coords of the board the xy coords on the location of the screen
def convertCoords(boxx, boxy):
    return (XMARGIN + (boxx * BSIZE)), (TOPMARGIN + (boxy * BSIZE))

#Draws a single block out of 4, including all of the shading
def addBox(boxx, boxy, COLOUR, pixelx=None, pixely=None):
    if COLOUR == BLANK:
        return
    if pixelx == None and pixely == None:
        pixelx, pixely = convertCoords(boxx, boxy)
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
