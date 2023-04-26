"""
File containing both obstacle classes
"""
import os
import random
import pygame


class Castle(pygame.sprite.Sprite):
    """
    This class initializes an instance of the castle sprite and updates
    the position
    """
    obstacle_list = pygame.sprite.Group()

    def __init__(self, x, y, width, height):
        """
        Initialize an instance of the class

        Args:
            x: an integer representing the x position in the frame
            y: an integer representing the y position in the frame
            width: an integer representing the width of the obstacle
            height: an integer representing the height of the obstacle
        """
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(0)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = 10  # change this value to control the speed of the obstacle

    def update(self):
        """
        This method updates the position of the castles so that they appear to be
        moving
        """
        self.rect.x -= self.velocity

    def add_obstacle(self, worldx, worldy, obstacle_list):
        """
        This method places the obstacle on the screen
        """
        width = random.randint(100, 150)
        height = random.randint(100, 500)
        x = worldx + width
        y = worldy - height
        obstacle = Castle(x, y, width, height)
        obstacle_list.add(obstacle)


class Arrows(pygame.sprite.Sprite):
    """
    This class creates instances of the arrows obstacle
    """
    def __init__(self):
        """
        This method initializes an instance of the class
        """
        # Load the arrows image
        self.frame_width = 1200
        self.frame_heigth = 825
        self.image = pygame.image.load(os.path.join("images", "arrows.png"))

        # # Select a random width and height for the size of the arrows sprite
        # self.width = random.randint(100, 200)
        # self.height = random.randint(100, 200)

        # Randomize x and y positions
        self.x_position = random.randint(900, 1200)
        self.y_position = random.randint(600, 800)

        # Get the dimensions of the surface
        self.rect = self.image.get_rect()
        self.rect.x = self.x_position
        self.rect.y = self.y_position

        # Set the velocity of the object
        self.velocity = random.randint(20, 50)
    
    def update(self):
        """
        This method updates the position of the arrows -- causes the arrows
        to appear as through they are flying
        """
        self.rect.x -= self.velocity

    def add_arrows(self):
        """
        This method adds more instances of the arrows -- recalls the class in order
        to add more arrows on the screen
        """
        x = self.frame_width + self.width
        y = self.frame_height - self.height
        obstacle = Arrows()
        obstacle_list = []
        obstacle_list.append(obstacle)
