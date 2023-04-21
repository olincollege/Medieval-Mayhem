"""
File containing Sprite class
"""
import os
import pygame


class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(
                os.path.join("images", "DragonFly" + str(i) + ".png")
            ).convert()
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
