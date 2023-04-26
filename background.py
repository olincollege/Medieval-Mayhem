import os
import pygame


class Background:
    worldx = 960
    worldy = 720
    fps = 40
    ani = 10000
    world = pygame.display.set_mode([worldx, worldy])
    pi = 3.14
    background_image = pygame.image.load(
        os.path.join("images", "background.PNG")
    ).convert()
    bg_width, bg_height = background_image.get_size()

    def __init__(self):
        pass
