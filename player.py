import pygame
import sys
import os


class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    player_list = pygame.sprite.Group()

    def __init__(self):
        """
        Initialize an instance of the dragon sprite
        """
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
            # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
        self.current_image = 0

    def control(self, x, y, z):
        """
        control player movement
        """
        self.movex += x
        self.movey += y
        self.movez += z

    def update(self):
        """
        Update sprite position and image
        """
        # Update sprite position
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

    def update_image(self):
        # Update sprite image
        self.current_image += 1
        if self.current_image >= len(self.images):
            self.current_image = 0
        self.image = self.images[self.current_image]

    def check_bounds(self, player, worldx, worldy):
        if player.rect.left < 0:
            player.rect.left = 0
        elif player.rect.right > worldx:
            player.rect.right = worldx
        if player.rect.top < 0:
            player.rect.top = 0
        elif player.rect.bottom > worldy:
            player.rect.bottom = worldy
