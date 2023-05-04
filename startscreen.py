"""
File containing StartScreen class
"""

import os
import pygame
from pygame.locals import MOUSEBUTTONDOWN
from pygame.locals import QUIT


pygame.font.init()


class StartScreen:
    """
    A class representing the start screen of a game.

    Attributes:
    - width: an int representing the width of the screen.
    - height: an int representing The height of the screen.
    - screen: The Pygame surface object representing the screen.
    - font: The Pygame font object used for rendering text.
    - title_text: The Pygame surface object representing the title text.
    - start_button_rect: The Pygame rect object representing the
    start button.
    - start_button_text: The Pygame surface object representing
    the start button text.

    """

    def __init__(self, width, height) -> None:
        """
        Initializes the StartScreen object.

        Args:
        - width: an int representing the width of the screen.
        - height: an int representing The height of the screen.
        """
        # Initialize the StartScreen object with the specified width and height.
        self.width = width
        self.height = height
        self.img = pygame.image.load(
            os.path.join("images", "start_screen.PNG")
        ).convert()
        self.img.convert_alpha()
        self.screen = pygame.display.set_mode((width, height))
        self.font = pygame.font.Font(None, 50)
        self.start_button_rect = pygame.Rect(450, 200, 300, 125)
        self.start_button_text = self.font.render("Start", True, (0, 0, 0))
        self.image = pygame.transform.scale(self.img, (1200, 825))

    def display(self):
        """
        Displays the start screen and waits for
        the user to click the start button.

        Returns:
        - str: The string "start".
        """
        # Display the start screen and wait for user input.
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    # Quit the game if the user clicks the close button.
                    pygame.quit()
                    return None
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # If the user clicks the start button, return "start".
                    if self.start_button_rect.collidepoint(mouse_pos):
                        return "start"

            # Draw the start screen elements.
            self.screen.blit(self.image, (0, 0))
            pygame.draw.rect(
                self.screen, (255, 255, 255), self.start_button_rect
            )
            self.screen.blit(
                self.start_button_text,
                (
                    self.start_button_rect.centerx
                    - self.start_button_text.get_width() / 2,
                    self.start_button_rect.centery
                    - self.start_button_text.get_height() / 2,
                ),
            )
            pygame.display.flip()
