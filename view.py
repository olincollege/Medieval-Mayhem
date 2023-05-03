"""
File containing View class
"""

from player import Player
from obstacle import Castle
from obstacle import Arrows
from background import Background
from startscreen import StartScreen
from endscreen import EndScreen


class View:
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
        self.end_screen = EndScreen(Background.frame_width, Background.frame_height)

    def draw_start_screen(self):
        """
        This method creates an instance of StartScreen and draws the
        starting screen onto the window

        Returns:
            A String "start" representing whether the user has clicked
            the start button or not
        """
        start_screen = StartScreen(Background.frame_width, Background.frame_height)
        result = start_screen.display()
        return result


    def draw(self):
        """
        This method causes the background to scroll to the left by self.steps
        units
        """

        # Draw the background on the screen
        Background.world.blit(Background.background_image, (self.model.position, 0))
        Background.world.blit(
            Background.background_image, (self.model.position + Background.bg_width, 0)
        )

        # Draw the dragon
        Player.player_list.draw(Background.world)

        # Draw the castle
        Castle.obstacle_list.draw(Background.world)

        # Draw the arrows
        Arrows.arrows_list.draw(Background.world)
    
    def draw_end_screen(self):
        """
        This method draws the endscreen if the player has lost
        """
        if self.end_screen.display() is True:
            return True
        if self.end_screen.display() is False:
            return False
