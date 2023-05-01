"""
File containing View class
"""

from player import Player
from obstacle import Castle
from obstacle import Arrows
from background import Background

class View():
    """
    This class draws all the sprites and background onto the screen
    """
    def __init__(self, model):
        """
        This method initializes an instance of the class

        Args:
            model: an instance of the DragonModel class
        """
        self.model = model


    def draw(self):
        """
        This method causes the background to scroll to the left by self.steps
        units
        """

        # Draw the background on the screen
        Background.world.blit(
            Background.background_image, (self.model.position, 0)
            )
        Background.world.blit(
            Background.background_image,
            (self.model.position + Background.bg_width, 0)
        )

        # Draw the dragon
        Player.player_list.draw(Background.world)


        # Draw the castle
        Castle.obstacle_list.draw(Background.world)

        # Draw the arrows
        Arrows.arrows_list.draw(Background.world)
