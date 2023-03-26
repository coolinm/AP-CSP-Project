# import and initialize the pygame library
import pygame
import time
pygame.init()

# set up the screen and clock
screen = pygame.display.set_mode([600, 650])
clock = pygame.time.Clock()
startTime = time.time()

# create text fonts
font = pygame.font.Font('freesansbold.ttf', 32)
font_sm = pygame.font.Font('freesansbold.ttf', 16)
 
# create a text surface object
text1 = font.render('Tic Tac Toe', True, (0,0,0), (255,255,255))
text2 = font_sm.render("Press anywhere to begin", True, (0,0,0), (255,255,255))

# create a rectangular object for the text
textRect1 = text1.get_rect()
textRect2 = text2.get_rect()
 
# set the center of the rectangular object.
textRect1.center = (600 // 2, 650 // 2)
textRect2.center = (600 // 2, 650 // 1.3)

# run until the user asks to quit
running = True
started = False
while running:

    # check if window has been asked to close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
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

    # draw game borders and lines
    pygame.draw.line(screen, (0,0,0), (600, 0), (600, 600), 10 )
    pygame.draw.line(screen, (0,0,0), (0,600), (0,0), 10)
    pygame.draw.line(screen, (0,0,0), (600,600), (0,600), 10)
    pygame.draw.line(screen, (0,0,0), (0,0), (600,0), 10)
    pygame.draw.line(screen, (0,0,0), (200,0), (200,600), 10)
    pygame.draw.line(screen, (0,0,0), (400, 0), (400,600), 10)
    pygame.draw.line(screen, (0,0,0), (0, 200), (600,200), 10)
    pygame.draw.line(screen, (0,0,0), (0,400), (600,400), 10)

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

# def playerMove(x, y):

# def compMove(x, y):
