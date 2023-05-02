"""
File containing pytests for Arrows and Obstacle classes
"""

import pytest
from obstacle import Arrows, Castle
from background import Background

def test_arrow_bounds():
    """
    Test to make sure arrows stay within the bounds
    given in the class
    """
    arrows_obstacle_list = []
    for i in range(1, 50):
        arrows_obstacle_list.append(Arrows(0, 0))

    arrows.add_arrows(Background.frame_width, Arrows.arrows_list)
    y_position = arrows.height
    assert y_position >= 15 and y_position <= 250