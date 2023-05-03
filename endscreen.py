"""
File containing EndScreen class
"""

import pygame
from background import Background as Bg


pygame.font.init()


class EndScreen:
    """
    Theis class details functions for the endscreen when a
    player hits an obstacle:

    Methods:
        __init__(self, width, height): Initalizes an endscreen object
        display(self): Displays Endscreen in game world and defines
        exit button
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

        # Create font objects for end screen text and button text
        self.end_font = pygame.font.Font(None, 60)
        self.end_text = self.end_font.render("Game Over!", True, (255, 0, 0))
        self.end_rect = self.end_text.get_rect(center=(self.width / 2, self.height / 2))
        self.button_font = pygame.font.Font(None, 30)
        self.button_text = self.button_font.render("Exit", True, (0, 0, 0))
        self.button_rect = self.button_text.get_rect(
            center=(self.width / 2, self.height / 2 + 100)
        )

        # Initialize done flag to False
        self.done = False

    def display(self):
        """
        Display the end screen until the user
        clicks the Exit button or closes the window.

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
                    if self.button_rect.collidepoint(x_position, y_position):
                        self.done = True
                        return True

            # Blit the end screen text, button background,
            # and button text onto the game window
            Bg.world.blit(self.end_text, self.end_rect)
            pygame.draw.rect(Bg.world, (255, 255, 255), self.button_rect)
            Bg.world.blit(self.button_text, self.button_rect)

            # Update the display to show the changes

            pygame.display.flip()

        # Quit pygame and exit the program when the done flag is set to True
        pygame.quit()
