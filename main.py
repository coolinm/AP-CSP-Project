# import and initialize pygame and time
import pygame
import time
pygame.init()

# set up the screen and clock
screen = pygame.display.set_mode([600, 650])
clock = pygame.time.Clock()
startTime = time.time()

# create empty list to represent grid and list containing rectangles to detect mouse collision
grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
winListH = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
winListV = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
gridRect = [pygame.Rect(5, 5, 195, 195), pygame.Rect(5, 205, 195, 195), pygame.Rect(5, 405, 195, 195), pygame.Rect(205, 5, 195, 195), pygame.Rect(205, 205, 195, 195), pygame.Rect(205, 405, 195, 195), pygame.Rect(405, 5, 195, 195), pygame.Rect(405, 205, 195, 195), pygame.Rect(405, 405, 195, 195)]

# create text fonts
font = pygame.font.Font('freesansbold.ttf', 32)
fontSm = pygame.font.Font('freesansbold.ttf', 16)
 
# create a text surface object
text1 = font.render('Tic Tac Toe', True, (0,0,0), (255,255,255))
text2 = fontSm.render("Press anywhere to begin", True, (0,0,0), (255,255,255))

# create a rectangular object for the text
textRect1 = text1.get_rect()
textRect2 = text2.get_rect()
 
# set the center of the rectangular object.
textRect1.center = (600 // 2, 650 // 2)
textRect2.center = (600 // 2, 650 // 1.3)

# place an X or O in gridNum list
def placeGrid(index, player):
    row = 0
    col = 0
    
    match index:
        case 0:
           row = 0
           col = 0
        case 1:
           row = 1
           col = 0
        case 2:
           row = 2
           col = 0
        case 3:
           row = 0
           col = 1
        case 4:
           row = 1
           col = 1
        case 5:
           row = 2
           col = 1
        case 6:
           row = 0
           col = 2
        case 7:
           row = 1
           col = 2
        case 8:
           row = 2
           col = 2

    if grid[row][col] == " ":       
        if player == "X":
            grid[row][col] = "X" + str(col) + str(row)
            winListH[row][col] = "X"
            winListV[col][row] = "X"
            print("X placed at " + str(row) + ", " + str(col))
            return(True)
        elif player == "O":
            grid[row][col] = "O" + str(col) + str(row)
            winListH[row][col] = "O"
            winListV[col][row] = "O"
            print("O placed at " + str(row) + ", " + str(col))
            return(True)
    else:
        return(False)
    
# place Xs and Os in the game
def placeScreen():

    for item in grid:
        for piece in item:
            if piece.startswith("X"):
                uCol = (piece.removeprefix("X"))
                col = int(uCol[0])
                uRow = (piece.removeprefix("X"))
                row = int(uRow[1])

                y=0
                x=0

                match row:
                    case 0:
                        y=100
                    case 1:
                        y=300
                    case 2:
                        y=500
                
                match col:
                    case 0:
                        x=100
                    case 1:
                        x=300
                    case 2:
                        x=500
            
                pygame.draw.line(screen, (255,0,0), (x-100, y-100), (x+100, y+100), 5)
                pygame.draw.line(screen, (255,0,0), (x-100, y+100), (x+100, y-100), 5)

            elif piece.startswith("O"):
                uCol = (piece.removeprefix("O"))
                col = int(uCol[0])
                uRow = (piece.removeprefix("O"))
                row = int(uRow[1])
                
                y=0
                x=0

                match row:
                    case 0:
                        y=100
                    case 1:
                        y=300
                    case 2:
                        y=500
                
                match col:
                    case 0:
                        x=100
                    case 1:
                        x=300
                    case 2:
                        x=500
            
                pygame.draw.circle(screen, (0,0,0), (x, y), 100, 5)

def winCheck():
    # check for horizontal wins
    for list in winListH:
        if list.count("X") == 3:
            return("X")
        elif list.count("O") == 3:
            return("O")

    # check for vertical wins
    for list in winListV:
        if list.count("X") == 3:
            return("X")
        elif list.count("O") == 3:
            return("O")
        
    #check for diagonals
    if winListH[0][0] == "X" and winListH[1][1] == "X" and winListH[2][2] == "X":
        return("X")
    elif winListH[0][2] == "X" and winListH[1][1] == "X" and winListH[2][0] == "X":
        return("X")
    
    if winListH[0][0] == "O" and winListH[1][1] == "O" and winListH[2][2] == "O":
        return("O")
    elif winListH[0][2] == "O" and winListH[1][1] == "O" and winListH[2][0] == "O":
        return("O")

# run until the user asks to quit
running = True
started = False
pTurn = True
winner = False
while running:
    # check if window has been asked to close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            mousePosRx = round(mousePos[0], -1)
            mousePosRy = round(mousePos[1], -1)
            print(str(mousePosRx) + ", " + str(mousePosRy))
            for rectangle in gridRect:
                if rectangle.collidepoint(pygame.mouse.get_pos()):
                    if pTurn == True:
                        if placeGrid(gridRect.index(rectangle), "X") == True:
                            pTurn = False
                        else:
                            print("Item already placed there")
                    else:
                        if placeGrid(gridRect.index(rectangle), "O") == True:
                            pTurn = True
                        else:
                            print("Item already placed there")
                    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # fill the background with white
    screen.fill((255, 255, 255))

    # check if the start screen has been passed
    while started == False:
        # render text
        screen.fill((255, 255, 255))
        screen.blit(text1, textRect1)
        screen.blit(text2, textRect2)
        pygame.display.update()

        # check if mouse has been clicked and start game if it has
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                started = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                started = True
                # record time at start of game
                startTime = time.time()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    started = True
                    running = False

        clock.tick(60)

    while winner:
        screen.fill((255, 255, 255))
        winText = font.render(winCheck() + " won the game! Press R to restart.", True, (0,0,0), (255,255,255))
        winRect = winText.get_rect()
        winRect.center = (600 // 2, 650 // 2)
        screen.blit(winText, winRect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                started = True
                winner = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    started = True
                    running = False
                    winner = False
                elif event.key == pygame.K_r:
                    started = False
                    winner = False
                    grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
                    winListH = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
                    winListV = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

        clock.tick(60)
            

    # draw game borders and lines
    pygame.draw.line(screen, (0,0,0), (600, 0), (600, 600), 10)
    pygame.draw.line(screen, (0,0,0), (0, 600), (0, 0), 10)
    pygame.draw.line(screen, (0,0,0), (600,600), (0,600), 10)
    pygame.draw.line(screen, (0,0,0), (0,0), (600,0), 10)
    pygame.draw.line(screen, (0,0,0), (200,0), (200,600), 10)
    pygame.draw.line(screen, (0,0,0), (400, 0), (400,600), 10)
    pygame.draw.line(screen, (0,0,0), (0, 200), (600,200), 10)
    pygame.draw.line(screen, (0,0,0), (0,400), (600,400), 10)

    placeScreen()
    
    if winCheck() == "X" or winCheck() == "O":
        winner = True
        pygame.time.wait(500)

    # calculate seconds passed since game start
    # and create text object
    seconds = round(time.time() - startTime, 1)
    timerText = font.render(str(seconds), True, (0,0,0), (255,255,255))
    timerRect = timerText.get_rect()
    timerRect.center = (600 // 11, 650 // 1.035)
    screen.blit(timerText, timerRect)
        
    # update the display
    pygame.display.update()

    clock.tick(60)

# close game
pygame.quit()