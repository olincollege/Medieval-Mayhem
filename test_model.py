"""
File containing unit tests for Model class
"""

import pytest
from model import DragonModel
from obstacle import Castle, Arrows
from player import Player

# Create an instance of Player
player = Player()

# Create multiple instances of DragonModel
model_test = [
    (DragonModel(player), Castle(800, 500, 100, 100), Arrows(800, 500))
    for _ in range(100)
]


@pytest.mark.parametrize("model, castle, arrows", model_test)
def test_update_background(model, castle, arrows):
    """
    Test function for the update_background method of the DragonModel class

    Args:
        model: The instance of the DragonModel class to be tested
        castle: The instance of the Castle class to be used in the test
        arrows: The instance of the Arrows class to be used in the test
    """
    model.castle = castle
    model.arrows = arrows
    model.update_background()
    assert model.position == -10


@pytest.mark.parametrize("model, castle, arrows", model_test)
def test_update_dragon(model, castle, arrows):
    """
    Test that the dragon position is not changed at the beginning and stays
    at x = 50

    Args:
        model: The instance of the DragonModel class to be tested
        castle: The instance of the Castle class to be used in the test
        arrows: The instance of the Arrows class to be used in the test
    """
    model.castle = castle
    model.arrows = arrows
    model.player.rect.y = 50
    model.update_dragon()
    assert model.player.rect.y == 50


@pytest.mark.parametrize("model, castle, arrows", model_test)
def test_update_castle(model, castle, arrows):
    """
    Test that the castles move

    Args:
        model: The instance of the DragonModel class to be tested
        castle: The instance of the Castle class to be used in the test
        arrows: The instance of the Arrows class to be used in the test
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
