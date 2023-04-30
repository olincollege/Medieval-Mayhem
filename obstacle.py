"""
This file contains classes for the obstacles in the game.
The Castle and arrows obstacle classes are both in this
file.
"""

import pygame
import random
import os
import background as Background


class Castle(pygame.sprite.Sprite):
    """
    Represents a castle obstacle in the game.

    Attributes:
        obstacle_list (pygame.sprite.Group): A group of all the castle obstacles in the game.

    Methods:
        __init__(self, x, y, width, height): Initializes a new Castle instance with the given x and y coordinates,
            width, and height.
        update(self): Updates the position of the castle by moving it to the left by the specified velocity.
        add_obstacle(self, worldx, worldy, obstacle_list): Adds a new castle obstacle to the game with the given x and y
            coordinates, width, and height, and adds it to the given obstacle list.
    """

    obstacle_list = pygame.sprite.Group()

    def __init__(self, x, y, width, height):
        """
        Initialize a new castle obstacle.

        Parameters:
        - x: An int representing the x-coordinate of the castle's position
        - y: An int representing the y-coordinate of the castle's position
        - width: An int representing the width of the castle image
        - height: An int represnting the height of the castle image
        """
        super().__init__()

        # Load the two different tower images and add them to the images list
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(
                os.path.join("images", "tower" + str(i) + ".png")
            ).convert()
            img.set_colorkey(img.get_at((0, 0)))
            img = pygame.transform.scale(img, (width, height))
            self.images.append(img)

        # Choose one of the two images at random for the current image of the castle
        self.image = self.images[random.randint(0, 1)]

        # Set the position of the castle
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Set the speed of the castle
        self.velocity = 10  # change this value to control the speed of the obstacle

    def update(self):
        """
        Update the position of the castle by moving it to the left at its current velocity.
        """
        self.rect.x -= self.velocity

    def add_obstacle(self, worldx, worldy, obstacle_list):
        """
        Add a new castle obstacle to the given obstacle_list.

        Args:
            - worldx: An int representing the x-coordinate of the world
            in which the obstacle will be placed
            - worldy: An int representing the y-coordinate of the world
            in which the obstacle will be placed
            - obstacle_list: A pygame sprite group representing the list
            of obstacles to which the new obstacle will be added
        """
        width = 200
        height = random.randint(200, 500)
        x = worldx + width
        y = worldy - height
        obstacle = Castle(x, y, width, height)
        obstacle_list.add(obstacle)


class Arrows(pygame.sprite.Sprite):
    """
    A class to represent an arrows obstacle in the game.

    Attributes:
    arrows_list: A pygame Sprite group containing all the Arrows objects in the game.

    Methods:
    __init__(self, x, y):
        Initialize a new Arrows object.
    update(self):
        Update the position of the Arrows object based on its velocity.
    add_arrows(self, frame_width, arrows_list):
        Create a new Arrows object and add it to the arrows_list.
    """

    # A Sprite group containing all the Arrows objects in the game.
    arrows_list = pygame.sprite.Group()

    def __init__(self, x, y):
        """
        Initialize a new Arrows object.

        Args:
            x: An int representing the x-coordinate of the Arrows object.
            y: An int representing the y-coordinate of the Arrows object.
        """
        super().__init__()

        # Load and scale the image for the Arrows object.
        image_width = 200
        image_height = 150
        self.image = pygame.image.load(os.path.join("images", "arrows.png")).convert()
        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.image = pygame.transform.scale(self.image, (image_width, image_height))
        # Set dimensions for rectangle that detects collisions
        rect_dimensions = 60

        # Set the initial position of the Arrows object and generate a random velocity.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = random.randint(20, 40)

        # Change dimensions and position of collision detection rectangle
        self.rect.w -= rect_dimensions
        self.rect.h -= rect_dimensions
        self.rect.x += rect_dimensions // 2
        self.rect.y += rect_dimensions // 2

    def update(self):
        """
        Update the position of the Arrows object based on its velocity.
        """
        # Move the Arrows object to the left based on its velocity.
        self.rect.x -= self.velocity

    def add_arrows(self, frame_width, arrows_list):
        """
        Create a new Arrows object and add it to the arrows_list.

        Args:
            frame_width: An int representing the width of the game frame.
            arrows_list: A sprite group containing all the Arrows objects in the game.
        """
        # Generate a random width and height for the Arrows object and set its initial position.
        width = random.randint(200, 400)
        height = random.randint(50, 250)
        x = frame_width + width
        y = height

        # Create a new Arrows object and add it to the arrows_list.
        obstacle = Arrows(x, y)
        arrows_list.add(obstacle)
