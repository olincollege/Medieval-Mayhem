import os
import pygame


class Background:
    frame_width = 1200
    frame_height = 825
    frames_per_second = 40
    ani = 10000
    world = pygame.display.set_mode([frame_width, frame_height])
    pi = 3.14
    background_image = pygame.image.load(
        os.path.join("images", "grass_background.PNG")
    ).convert()
    bg_width, bg_height = background_image.get_size()

    def __init__(self):
        pass

    # # Create draw background method
    # def draw_background(self):