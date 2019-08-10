#importing
import pygame, sys

#setting up basic stuff and variables
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode((width, height))
white = (255,255,255)

# Game loop.
while True:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:pygame.quit(), sys.exit()

    #mendatory display commands
    pygame.display.flip()
    pygame.time.Clock().tick(60)
