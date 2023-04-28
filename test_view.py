import pygame
from player import Player as Pl
from obstacle import Castle as Co
from background import Background as Bg
from controller import Controller
from model import DragonModel

pygame.init()
dragon = DragonModel()
dragon.add_dragon()
while not dragon.player_done:
    dragon.background()
    dragon.update_dragon()
    dragon.add_castle()
    dragon.collision()
    pygame.display.flip()
    dragon.clock.tick(Bg.frames_per_second)
pygame.quit()
