import random
import pygame
from player import Player as Pl
from obstacle import Castle as Co
from obstacle import Arrows
from background import Background as Bg
from controller import Controller


clock = pygame.time.Clock()
pygame.init()
main = True
obstacle = Co(0, 0, 100, 100)
arrows = Arrows()

bg_x = 0
frame_count = 0
arrows_frame_count = 0
player_done = False

player = Pl()  # spawn player

player.rect.x = 50  # go to x
player.rect.y = 0  # go to y
Pl.player_list.add(player)
steps = 10

"""
Main Loop
"""

# Load the background image and get its dimensions

while not player_done:
    control = Controller()
    control.controller(player, steps)

    # Move the background image
    bg_x -= steps
    if bg_x < -Bg.bg_width:
        bg_x = 0

    # Draw the background image twice to simulate scrolling
    Bg.world.blit(Bg.background_image, (bg_x, 0))
    Bg.world.blit(Bg.background_image, (bg_x + Bg.bg_width, 0))

    # Check if player is out of bounds and adjust position if necessary
    player.check_bounds(player, Bg.worldx, Bg.worldy)
    # Create a new Castle instance every 90 frames
    frame_count += 1
    if frame_count == 90:
        frame_count = 0
        obstacle.add_obstacle(Bg.worldx, Bg.worldy, Co.obstacle_list)
    
    # Create a new Arrows instance every 80 frames
    if arrows_frame_count == 80:
        arrows_frame_count = 0
        arrows.add_arrows()

    player.update()
    Pl.player_list.draw(Bg.world)

    Co.obstacle_list.update()
    # Draw the obstacles
    Co.obstacle_list.draw(Bg.world)

    if pygame.sprite.spritecollide(player, Co.obstacle_list, False):
        player_done = True

    pygame.display.flip()
    clock.tick(Bg.fps)

pygame.quit
