"""
File containing Player class
"""

import os
import pygame

class Player(pygame.sprite.Sprite):
    """
    A class to represent the player object.

    Attributes:
        player_list: A pygame Sprite group containing all the Player objects in the game
    """

    player_list = pygame.sprite.Group()

    def __init__(self):
        """
        Initialize a new instance of the Player object.
        """
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.movez = 0
        self.frame = 0
        self.images = []

        # Set dimensions for rectangle that detects collisions
        rect_dimensions = 40

        # Load and optimize player images
        for i in range(1, 3):
            img = pygame.image.load(
                os.path.join("images", "DragonFly" + str(i) + ".png")
            ).convert()
            img.convert_alpha()  # Optimize alpha
            # Make the image background transparent
            img.set_colorkey(img.get_at((0, 0)))
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

            # Change dimensions and position of collision detection rectangle
            self.rect.w -= rect_dimensions
            self.rect.h -= rect_dimensions
            self.rect.x += rect_dimensions // 2
            self.rect.y += rect_dimensions // 2
        self.current_image = 0

        # NEW STUFF
        self.rect.x = 50
        self.rect.y = 0
        self.player_list.add(self)

    def control(self, x, y, z):
        """
        Control the movement of the Player object.

        Args:
            x: An int representing the x-coordinate of the Player object
            y: An int representing the y-coordinate of the Player object
            z: An int representing the z-coordinate of the Player object
        """
        self.movex += x
        self.movey += y
        self.movez += z

    def update(self):
        """
        Update the position of the Player object based on its velocity
        """
        # Update sprite position
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        # Moving up
        if self.movez < 0:
            self.rect.y -= abs(self.movez)
            self.movez = 0

        # Moving down
        if self.movez > 0:
            self.rect.y += abs(self.movez)
            self.movez = 0

    def update_image(self):
        """
        Update the image of the Player object
        """
        # Update sprite image
        self.current_image += 1
        if self.current_image >= len(self.images):
            self.current_image = 0
        self.image = self.images[self.current_image]

    def check_bounds(self, player, worldx, worldy):
        """
        Check if the Player object is within the game bounds

        Args:
            player: A Player object representing the player sprite
            worldx: An int representing the width of the game world
            worldy: An int representing the height of the game world
        """
        # Check if the left edge of the player sprite is out of bounds, and adjust it if necessary
        if player.rect.left < 0:
            player.rect.left = 0

        # Check if the right edge of the player sprite is out of bounds, and adjust it if necessary
        elif player.rect.right > worldx:
            player.rect.right = worldx

        # Check if the top edge of the player sprite is out of bounds, and adjust it if necessary
        if player.rect.top < 0:
            player.rect.top = 0

        # Check if the bottom edge of the player sprite is out of bounds, and adjust it if necessary
        elif player.rect.bottom > worldy:
            player.rect.bottom = worldy
