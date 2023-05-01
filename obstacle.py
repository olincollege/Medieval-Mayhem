"""
This file contains classes for the obstacles in the game.
The Castle and arrows obstacle classes are both in this
file.
"""

import random
import os
import pygame


class Castle(pygame.sprite.Sprite):
    """
    Represents a castle obstacle in the game.

    Attributes:
        obstacle_list: A pygame Sprite group of all
        the castle obstacles in the game
    """

    obstacle_list = pygame.sprite.Group()

    def __init__(self, x_position, y_position, width, height):
        """
        Create a new instance of the Castle object

        Args:
            x: An int representing the x-coordinate of the castle's position
            y: An int representing the y-coordinate of the castle's position
            width: An int representing the width of the castle image
            height: An int represnting the height of the castle image
        """
        super().__init__()

        # Create an images list to store all tower images
        self.images = []

        # Load the tower images
        for i in range(1, 3):
            img = pygame.image.load(
                os.path.join("images", "tower" + str(i) + ".png")
            ).convert()

            # Set the tower background to be transparent
            img.set_colorkey(img.get_at((0, 0)))
            img = pygame.transform.scale(img, (width, height))

            # Append the image into the image list
            self.images.append(img)

        # Choose one of the two images at random for
        # the current image of the castle
        self.image = self.images[random.randint(0, 1)]

        # Set the position of the castle
        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position

        # Set the speed of the castle
        self.velocity = 10


    def update(self):
        """
        Update the position of the castle by moving it to the
        left at its current velocity.
        """
        self.rect.x -= self.velocity

    def add_obstacle(self, worldx, worldy, obstacle_list):
        """
        Add a new castle obstacle to the given obstacle_list.

        Args:
            worldx: An int representing the x-coordinate of the world
            in which the obstacle will be placed
            worldy: An int representing the y-coordinate of the world
            in which the obstacle will be placed
            obstacle_list: A pygame sprite group representing the list
            of obstacles to which the new obstacle will be added
        """
        width = 200
        height = random.randint(200, 500)
        x_position = worldx + width
        y_position = worldy - height
        obstacle = Castle(x_position, y_position, width, height)
        obstacle_list.add(obstacle)


class Arrows(pygame.sprite.Sprite):
    """
    A class to create and position the arrow obstacles

    Attributes:
        arrows_list: A pygame Sprite group containing all the
        Arrows objects in the game

    """

    # A Sprite group containing all the Arrows objects in the game.
    arrows_list = pygame.sprite.Group()

    def __init__(self, x_position, y_position):
        """
        Initialize a new Arrows object.

        Args:
            x: An int representing the x-coordinate of the Arrows object
            y: An int representing the y-coordinate of the Arrows object
        """
        super().__init__()

        # Scale the image
        image_width = 200
        image_height = 150

        # Load the image
        self.image = pygame.image.load(
            os.path.join("images", "arrows.png")
            ).convert()
        # Make the image background transparent
        self.image.set_colorkey(self.image.get_at((0, 0)))

        self.image = pygame.transform.scale(
            self.image, (image_width, image_height)
            )
        # Set dimensions for rectangle that detects collisions
        rect_dimensions = 60

        # Set the initial position of the Arrows object
        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position

        # Generate a random speed for the arrows
        self.velocity = random.randint(20, 40)

        # Change dimensions and position of collision detection rectangle
        self.rect.w -= rect_dimensions
        self.rect.h -= rect_dimensions
        self.rect.x += rect_dimensions // 2
        self.rect.y += rect_dimensions // 2

    def update(self):
        """
        Update the position of the Arrows object based on its velocity
        """

        # Move the Arrows object to the left based on its velocity
        self.rect.x -= self.velocity

    def add_arrows(self, frame_width, arrows_list):
        """
        Create a new Arrows object and add it to the arrows_list.

        Args:
            frame_width: An int representing the width of the game frame
            arrows_list: A sprite group containing all the Arrows
            objects in the game
        """
        # Generate a random width and height for the Arrows object
        width = random.randint(200, 400)
        height = random.randint(15, 250)

        x_position = frame_width + width
        y_position = height

        # Create a new Arrows object and add it to the arrows_list
        obstacle = Arrows(x_position, y_position)
        arrows_list.add(obstacle)
