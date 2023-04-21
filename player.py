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
        """
        Method to create the object (penguin) desired on screen

        Args:
            self: an instance of the class
        """
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        # Loop to cycle through each image
        for i in range(1, 5):
            # Lines 26-28 only works if person running the code has the
            # files stored on their computer
            picture = pygame.image.load(
                os.path.join("images", "hero" + str(i) + "png")
            ).convert()
            self.images.append(picture)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

        





