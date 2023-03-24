# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([600, 600])
clock = pygame.time.Clock()

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.line(screen, (0,0,0), (600, 0), (600, 600), 30)
    pygame.draw.line(screen, (0,0,0), (0,600), (0,0), 30)
    pygame.draw.line(screen, (0,0,0), (600,600), (0,600), 30)
    pygame.draw.line(screen, (0,0,0), (0,0), (600,0), 30)

    # Flip the shit because pygame dumb dumb
    pygame.display.flip()

    clock.tick(60)

# Done! Time to quit.
pygame.quit()