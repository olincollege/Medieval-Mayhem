"""
File containing View class
"""

import pygame
# from player import Player as Pl
# from obstacle import Castle as Co
from background import Background
# from controller import Controller
from model import DragonModel


pygame.init()

# Create an instance of DragonModel
dragon = DragonModel()

# Draw the dragon onto the screen
dragon.add_dragon()

# Run the loop while player_done is False
while not dragon.player_done:
    # Draw the background
    dragon.background()

    # Update the position of the dragon
    dragon.update_dragon()

    # Add castles and arrows
    dragon.add_castle()
    dragon.add_arrows()
    
    # Check if there is a collision
    collision = dragon.collision()

    # Move to the endscreen if a collision has occurred
    if collision:
        dragon.end_screen()
    pygame.display.flip()
    dragon.clock.tick(Background.frames_per_second)
pygame.quit()
