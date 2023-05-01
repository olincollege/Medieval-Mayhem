"""
File containing Model class
"""
import pygame
from background import Background
from obstacle import Castle
from player import Player
from controller import Controller
from obstacle import Arrows
from endscreen import EndScreen


class DragonModel:
    """
    This is the model class for the dragon. It

    Attributes:
        steps: an integer representing how far up and down the dragon goes
        when the up/down keys are pressed
        castle: an instance of the Castle class
        arrows: an instance of the Arrows class
        endscreen: an instance of the EndScreen class
    """

    steps = 10
    castle = Castle(0, 0, 100, 100)
    arrows = Arrows(0, 0)
    endscreen = EndScreen(Background.frame_width, Background.frame_height)

    def __init__(self, player):
        """
        Initialize an instance of the DragonModel class
        """
        self.score = 0
        self.position = 0
        self.clock = pygame.time.Clock()
        self.frame_count = 0
        self.arrows_frame_count = 0
        self.player_done = False
        self.player = player

    def update_background(self):
        """
        This method causes the background to scroll to the left by self.steps
        units
        """

        # Move the position of the background self.steps units to the left
        self.position -= self.steps

        # Reset the position to zero if the position is less than the negative
        # of the background width
        if self.position < -Background.bg_width:
            self.position = 0

    # def add_dragon(self):
    #     """
    #     This method initializes the position of the dragon and adds
    #     it to the player list
    #     """
    #     self.player.rect.x = 50
    #     self.player.rect.y = 0
    #     Player.player_list.add(self.player)

    def update_dragon(self):
        """
        This method moves the dragon when the up and down arrow keys are pressed
        """

        # Create an instance of Controller
        # control = Controller()
        # control.controller(self.player, self.steps)

        # Check the bounds to make sure the dragon does not go off the screen
        self.player.check_bounds(
            self.player, Background.frame_width, Background.frame_height
        )
        self.player.update()

    def collision(self):
        """
        This method checks to see if a collision has occurred by checking to see if
        the dragon has collided with any of the obstacle sprite groups. If it hasn't,
        the score is updated and drawn onto the screen

        Returns:
            A Boolean representing whether there has been a collision or not
        """
        # Check to see if a collision has occurred
        if pygame.sprite.spritecollide(
            self.player, Castle.obstacle_list, False
        ) or pygame.sprite.spritecollide(self.player, Arrows.arrows_list, False):
            self.player_done = True
            return self.player_done
        else:
            # Increment the score by one
            self.score += 1
            # Set the font size
            font = pygame.font.Font(None, 50)
            # Set the font color
            white = pygame.Color("white")
            # Render the image to be a different type so it can be blitted on the screen
            score_image = font.render(f"Your Score: {self.score}", True, white)
            # Blit the image on the screen
            Background.world.blit(score_image, (920, 10))
            # Update the display
            pygame.display.update()

    def update_castle(self):
        """
        This method adds a castle every 90 frames
        """
        # Increase the frame count by one
        self.frame_count += 1

        # If the frame count is 90, reset it to zero
        if self.frame_count == 90:
            self.frame_count = 0

            # Add the castle obstacle
            self.castle.add_obstacle(
                Background.frame_width, Background.frame_height, Castle.obstacle_list
            )
        # Update obstacle_list to add the new castle
        Castle.obstacle_list.update()

    def update_arrows(self):
        """
        This method adds arrows every 80 frames
        """

        # Increase the frame count by one
        self.arrows_frame_count += 1

        # Reset the frame count to zero if the frame count is 80
        if self.arrows_frame_count == 80:
            self.arrows_frame_count = 0

            # Add the arrow obstacle
            self.arrows.add_arrows(Background.frame_width, Arrows.arrows_list)
        # Update obstacle_list to add the new arrow obstacle
        Arrows.arrows_list.update()

    def end_screen(self):
        """
        This method draws the endscreen if the player has lost
        """
        if self.endscreen.display():
            Player()
