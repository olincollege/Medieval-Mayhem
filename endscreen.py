"""
File containing EndScreen class
"""

import pygame
from background import Background as Bg

pygame.font.init()


class EndScreen:
    """
    This class details functions for the endscreen when
    a player hits an obstacle:

    Methods:
        __init__(self, width, height): Initializes an endscreen object
        display(self): Displays Endscreen in game world and
        defines exit and try again buttons
    """

    def __init__(self, width, height):
        """
        Initialize EndScreen object.

        Args:
            width: An int representing width of the game window
            height: An int representing height of the game window
        """
        self.width = width
        self.height = height

        # Create font objects for end screen text and exit button text
        self.end_font = pygame.font.Font(None, 60)
        self.end_text = self.end_font.render("Game Over!", True, (255, 0, 0))
        self.end_rect = self.end_text.get_rect(
            center=(self.width / 2, self.height / 2)
        )
        self.exit_button_font = pygame.font.Font(None, 30)
        self.exit_button_text = self.exit_button_font.render(
            "Exit", True, (0, 0, 0)
        )
        self.exit_button_rect = self.exit_button_text.get_rect(
            center=(self.width / 2, self.height / 2 + 50)
        )

        # Initialize done flag to False
        self.done = False

    def display(self):
        """
        Display the end screen until the user clicks the Exit button
        or closes the window.

        Returns:
            bool: True if the Exit button is clicked, False otherwise
        """
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # If the user clicks the 'x' button in the top right corner
                    # of the window, set done flag to True
                    self.done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicks the mouse button
                    # get the position of the click
                    x_position, y_position = event.pos
                    # If the position of the click is within the bounds of the
                    # Exit button, set done flag to True
                    if self.exit_button_rect.collidepoint(
                        x_position, y_position
                    ):
                        print("exit")
                        self.done = True
                        return True
            # Blit the end screen text, Exit button background
            # and button text onto the game window
            Bg.world.blit(self.end_text, self.end_rect)
            pygame.draw.rect(Bg.world, (255, 255, 255), self.exit_button_rect)
            Bg.world.blit(self.exit_button_text, self.exit_button_rect)

            # Update the display to show the changes

            pygame.display.flip()
