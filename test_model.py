import pytest
import pygame
from model import DragonModel
from obstacle import Castle, Arrows
from player import Player

player = Player()
model_test = [
    (DragonModel(player), Castle(800, 500, 100, 100), Arrows(800, 500))
    for _ in range(100)
]


@pytest.mark.parametrize("model, castle, arrows", model_test)
def test_update_background(model, castle, arrows):
    """
    Test function for the update_background method of the DragonModel class.

    Args:
    - model: The instance of the DragonModel class to be tested.
    - castle: The instance of the Castle class to be used in the test.
    - arrows: The instance of the Arrows class to be used in the test.
    """
    model.castle = castle
    model.arrows = arrows
    model.update_background()
    assert model.position == -10


@pytest.mark.parametrize("model, castle, arrows", model_test)
def test_update_dragon(model, castle, arrows):
    """
    Test function for the update_dragon method of the DragonModel class.

    Args:
     - model: The instance of the DragonModel class to be tested.
    - castle: The instance of the Castle class to be used in the test.
    - arrows: The instance of the Arrows class to be used in the test.
    """
    model.castle = castle
    model.arrows = arrows
    model.player.rect.y = 50
    model.update_dragon()
    assert model.player.rect.y == 50


@pytest.mark.parametrize("model, castle, arrows", model_test)
def test_castle_collision(model, castle, arrows):
    """
    Test function for the collision method of the DragonModel class with the Castle obstacle.

    Args:
     - model: The instance of the DragonModel class to be tested.
    - castle: The instance of the Castle class to be used in the test.
    - arrows: The instance of the Arrows class to be used in the test.
    """
    model.castle = castle

    # test collision with castle obstacle
    for i in range(len(castle.obstacle_list)):
        castle.obstacle_list[i].rect.x = 1000
        castle.obstacle_list[i].rect.y = 1000
    model.player.rect.x = 50
    model.player.rect.y = 800
    assert model.collision() == True

    # test no collision
    castle.obstacle_list.empty()
    assert model.collision() == False

    for i in range(len(arrows.arrows_list)):
        arrows.arrows_list[i].rect.x = 1000
        arrows.arrows_list[i].rect.y = 1000
    model.player.rect.x = 50
    model.player.rect.y = 130
    assert model.collision() == True

    # test no collision
    arrows.arrows_list.empty()
    assert model.collision() == False


@pytest.mark.parametrize("model, castle, arrows", model_test)
def test_update_castle(model, castle, arrows):
    """
    Test function for the collision method of the DragonModel class with the Castle obstacle.

    Args:
     - model: The instance of the DragonModel class to be tested.
    - castle: The instance of the Castle class to be used in the test.
    - arrows: The instance of the Arrows class to be used in the test.
    """
    # Instance of castle and arrows for test
    model.castle = castle
    model.arrows = arrows

    # Count of obstacles
    initial_obstacle_count = len(model.castle.obstacle_list.sprites())

    # Loop through the updates for each castle object
    for _ in range(10):
        model.update_castle()

    # Check that current obstacle count is greater than previous
    assert len(model.castle.obstacle_list.sprites()) >= initial_obstacle_count
