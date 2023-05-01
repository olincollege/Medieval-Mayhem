"""
File containing Background class
"""
import os
import pygame


class Background:
    """
    A class for managing the background of the game.

    Attributes:
        frame_width: an int representing the width of the
        display window.
        frame_height: an int representing the height of the
        display window.
        frames_per_second: an int representing the number of frames to be
        displayed per second.
        ani : an int representing the duration of the animation in
        milliseconds.
        world : a pygame.Surface representing the display window created
        using Pygame.
        pi: a float representing the value of pi.
        background_image: a pygame.Surface representing the background
        image to be used for the display window.
        bg_width: an int representing the width of the background image.
        bg_height: an int representing the height of the background image.
    """

    # Width of display window
    frame_width = 1200
    # Height of display window
    frame_height = 825
    # Number of frames per second for animation
    frames_per_second = 40
    # Total animation frame duration
    ani = 10000

    # Create a display window using Pygame
    world = pygame.display.set_mode([frame_width, frame_height])

    # Define the value of pi
    pi = 3.14

    # Load the background image
    background_image = pygame.image.load(
        os.path.join("images", "grass_background.PNG")
    ).convert()

    # Get the width and height of the background image
    bg_width, bg_height = background_image.get_size()

    def __init__(self):
        """
        Constructor for the Background class.

        """
