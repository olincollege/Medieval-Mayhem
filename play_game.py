"""
Main file to run dragon game
"""
import pygame
from model import DragonModel
from view import View
from player import Player
from controller import Controller
from background import Background

pygame.init()
# Create an instance of the dragon
dragon = Player()

# Create an instance of the model
model = DragonModel(dragon)

# Create an instance of view
view = View(model)

result = view.draw_start_screen()

# Create an instance of controller
controller = Controller(model)
while not model.player_done:
    # Update controller
    controller.update()
    # Draw background, dragon, and sprites
    view.draw()
    if result == "start":
        # Update dragon, arrows, castle, and background
        model.update_dragon()
        model.update_background()
        model.update_arrows()
        model.update_castle()

        # Detect collision
        COLLISION = model.collision()

        # Move to the endscreen if a collision has occurred
        if COLLISION:
            view.draw_end_screen()
        pygame.display.flip()
        model.clock.tick(Background.frames_per_second)