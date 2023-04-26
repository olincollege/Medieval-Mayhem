"""
File containing Arrows sprite class
"""
import os
import random
import pygame




class Arrows(pygame.sprite.Sprite):
    """
    This class...
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
        self.rect.x -= self.velocity

    def add_obstacle(self):
        
        x = self.frame_width + self.width
        y = self.frame_height - self.height
        obstacle = Arrows()
        obstacle_list = []
        obstacle_list.append(obstacle)
