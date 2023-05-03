import pygame
import pytest
from player import Player
from obstacle import Castle
from background import Background
from controller import Controller
from model import DragonModel


pygame.init()



def test_y_pos():
    """
    Test that the y position of the dragon sprite is constant after updating
    the x position
    """
    player = Player()
    player.rect.x = 100
    player.rect.y = 200
    assert player.rect.x == 100
    assert player.rect.y == 200
    player.update()
    assert player.rect.y == 200

def test_castle():
    """
    Test that the castles move 15 units to the left
    """
    castle = Castle(0, 0, 100, 100)
    castle.add_obstacle(100, 100, Castle.obstacle_list)
    assert len(Castle.obstacle_list) == 1
    castle.update()
    assert castle.rect.x == -10

def test_controller():
    controller = Controller()
    player = Player()
    controller.update(player, 0)
    assert player.rect.y == 0
    controller.update(player, -100)
    assert player.rect.y == 0

def test_dragon_model():
    dragon = DragonModel()
    dragon.add_dragon()
    assert len(Player.player_list) == 1
    dragon.collision()
    assert dragon.score == 1
    dragon.player.rect.x = -10
    dragon.update_dragon()
    assert dragon.player.rect.x == 0
