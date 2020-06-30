import pygame

# initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Tile and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370  # define the initial X value
playerY = 480  # define the initial Y value
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Game loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Update the playerX position
    playerX += playerX_change

    # Add the player to the screen
    player(playerX, playerY)

    # Update the display
    pygame.display.update()
