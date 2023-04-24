import pygame
import sys
import os
import math

"""
Variables
"""

worldx = 960
worldy = 720
fps = 40
ani = 10000
world = pygame.display.set_mode([worldx, worldy])
pi = 3.14

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)

"""
Objects
"""


class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.movez = 0
        self.frame = 0
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(
                os.path.join("images", "DragonFly" + str(i) + ".png")
            ).convert()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(ALPHA)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def control(self, x, y, z):
        """
        control player movement
        """
        self.movex += x
        self.movey += y
        self.movez += z

    def update(self):
        """
        Update sprite position
        """
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        # moving up
        if self.movez < 0:
            self.rect.y -= abs(self.movez)
            self.movez = 0

        # moving down
        if self.movez > 0:
            self.rect.y += abs(self.movez)
            self.movez = 0


"""
Setup
"""

backdrop = pygame.image.load(os.path.join("images", "background.PNG"))
clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True

player = Player()  # spawn player
player.rect.x = 0  # go to x
player.rect.y = 0  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10

"""
Main Loop
"""

"""
Main Loop
"""

# Load the background image and get its dimensions
background = pygame.image.load(os.path.join("images", "background.PNG")).convert()
bg_width, bg_height = background.get_size()

# Initialize the x position of the background to 0
bg_x = 0
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord("q"):
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False
            if event.key == pygame.K_UP or event.key == ord("w"):
                player.control(0, -steps, 5)
            if event.key == pygame.K_DOWN or event.key == ord("s"):
                player.control(0, steps, 5)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == ord("w"):
                player.control(0, steps, 0)
            if event.key == pygame.K_DOWN or event.key == ord("s"):
                player.control(0, -steps, 0)

    # Move the background image
    bg_x -= steps
    if bg_x < -bg_width:
        bg_x = 0

    # Draw the background image twice to simulate scrolling
    world.blit(background, (bg_x, 0))
    world.blit(background, (bg_x + bg_width, 0))

    # Check if player is out of bounds and adjust position if necessary
    if player.rect.left < 0:
        player.rect.left = 0
    elif player.rect.right > worldx:
        player.rect.right = worldx
    if player.rect.top < 0:
        player.rect.top = 0
    elif player.rect.bottom > worldy:
        player.rect.bottom = worldy

    player.update()
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)
