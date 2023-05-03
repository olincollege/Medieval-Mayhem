"""
File containing pytests for Arrows and Obstacle classes
"""

import random
import pytest
from obstacle import Arrows
from obstacle import Castle
from background import Background

arrows_obstacle_list = []
velocity_list = []
for i in range(0, 100):
    arrows_obstacle_list.append(Arrows(0, 0))
    velocity_list.append(random.randint(10, 50))

@pytest.mark.parametrize("arrow", arrows_obstacle_list)
def test_arrow_range(arrow):
    """
    The Arrows class randomly determines the y position of the arrows.
    This test tests that the y position of the arrows is within the range
    that is specified in the class

    Args:
        arrow: an instance of Arrows
    """
    arrow.add_arrows(Background.frame_width, Arrows.arrows_list)
    assert arrow.height >= 15 and arrow.height <= 250

@pytest.mark.parametrize("arrow, velocity", [
    (arrow, velocity) for arrow, velocity in zip(arrows_obstacle_list, velocity_list)
])
def test_arrow_position(arrow, velocity):
    """
    The position of the arrows is moved to the left by whatever number
    velocity is. This test tests that the arrows actually move left by whatever
    number velocity is
    """
    arrow.velocity = velocity
    arrow.update()
    arrow_position = 30
    assert arrow.rect.x == arrow_position - velocity


castle_obstacle_list = []
for i in range(0, 100):
    castle_obstacle_list.append(Castle(0, 0, 100, 100))

@pytest.mark.parametrize("castle", castle_obstacle_list)
def test_castle_height(castle):
    """
    The Castle class randomly generates the height of the castles.
    This tests that the height of the castle is within the range
    specified in the class
    """
    castle.add_obstacle(Background.frame_width, Background.frame_height, Castle.obstacle_list)
    assert castle.height >= 200 and castle.height <= 500


