import math
import pygame as py
import time
import os


def scroll(background):
    py.init()

    clock = py.time.Clock()

    FrameHeight = 600
    FrameWidth = 1200

    # Pygame frame window
    py.display.set_caption("Endless Scrolling in pygame")
    screen = py.display.set_mode((FrameWidth, FrameHeight))

    # Load background image
    bg = py.image.load(os.path.join("images", background))

    # Define main variables in scrolling
    scroll = 0

    # Fix potential buffering issues
    tiles = math.ceil(FrameWidth / bg.get_width()) + 1

    # Set time to 0
    t = 0
    # Run for 60 seconds
    while t < 60:
        # Manage speed of scrolling
        clock.tick(33)

        # Append the image to the back of the same image
        i = 0
        while i < tiles:
            screen.blit(bg, (bg.get_width() * i + scroll, 0))
            i += 1
        # Frame for scrolling
        scroll -= 6

        # Reset scroll frame
        if abs(scroll) > bg.get_width():
            scroll = 0
        # Close frame of scrolling
        for event in py.event.get():
            if event.type == py.QUIT:
                quit()

        py.display.update()
        time.sleep(0.01)
        t += 1

    py.quit()