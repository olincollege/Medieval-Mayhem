"""
This file contains code for the controller class
"""

import pygame
import sys


class Controller:
    """
    A class that handles user input events and updates the state of the player object accordingly.

    Attributes:
        None

    Methods:
        controller(player, steps):
            Handles user input events and updates the state of the player object accordingly.

    """

    def __init__(self):
        """
        Initializes an instance of the Controller class.
        """
        pass

    def controller(self, player, steps):
        """
        Handles user input events and updates the state of the player object accordingly.

        This method loops through all the events in the event queue and updates the state
        of the player object based on the events detected. It handles keydown and keyup events
        for the up and down arrow keys, as well as the 'w' and 's' keys. It also handles the event
        when the user clicks the 'x' button to quit the program.

        Args:
            player: An instance of the Player class that represents the player object.
            steps: An int representing the number of pixels to move the player object
            by on each key press or release event.

        Returns:
            None
        """
        # Loop through all the events in the event queue
        for event in pygame.event.get():
            # Handle the event when the user clicks the 'x' button
            if event.type == pygame.QUIT:
                # Quit pygame and exit the program
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False

            # Handle keydown events
            if event.type == pygame.KEYDOWN:
                # Handle the event when the user presses the 'q' key
                if event.key == ord("q"):
                    # Quit pygame and exit the program
                    pygame.quit()
                    try:
                        sys.exit()
                    finally:
                        main = False
                # Handle the event when the user presses the up arrow or the 'w' key
                if event.key == pygame.K_UP or event.key == ord("w"):
                    # Move the player object up
                    player.control(0, -steps, 5)
                    # Update the player object's image
                    player.update_image()
                # Handle the event when the user presses the down arrow or the 's' key
                if event.key == pygame.K_DOWN or event.key == ord("s"):
                    # Move the player object down
                    player.control(0, steps, 5)
                    # Update the player object's image
                    player.update_image()

            # Handle keyup events
            if event.type == pygame.KEYUP:
                # Handle the event when the user releases the up arrow or the 'w' key
                if event.key == pygame.K_UP or event.key == ord("w"):
                    # Stop the player object's upward movement
                    player.control(0, steps, 0)
                    # Update the player object's image
                    player.update_image()
                # Handle the event when the user releases the down arrow or the 's' key
                if event.key == pygame.K_DOWN or event.key == ord("s"):
                    # Stop the player object's downward movement
                    player.control(0, -steps, 0)
                    # Update the player object's image
                    player.update_image()
