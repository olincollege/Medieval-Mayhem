import pygame
from background import Background
from obstacle import Castle
from player import Player
from controller import Controller
from obstacle import Arrows
from endscreen import EndScreen


class DragonModel:
    """
    Docstring
    """

    steps = 10
    # collision = False
    player = Player()  # spawn player
    obstacle = Castle(0, 0, 100, 100)
    arrows = Arrows(0, 0)
    endscreen = EndScreen(Background.frame_width, Background.frame_height)

    # def __init__(self, player, background, tower1, tower2, tower3):
    def __init__(self):
        self.score = 0
        self.position = 0
        self.clock = pygame.time.Clock()
        self.frame_count = 0
        self.arrows_frame_count = 0
        self.player_done = False
        # spawn player

    def background(self):
        # background = self.player.Background()

        # bg_x = 0  # rename to positon
        # clock = pygame.time.Clock()
        self.position -= self.steps
        if self.position < -Background.bg_width:
            self.position = 0
        Background.world.blit(Background.background_image, (self.position, 0))
        Background.world.blit(
            Background.background_image, (self.position + Background.bg_width, 0)
        )

    def add_dragon(self):
        self.player.rect.x = 50  # go to x
        self.player.rect.y = 0  # go to y
        Player.player_list.add(self.player)

    def update_dragon(self):
        control = Controller()
        control.controller(self.player, self.steps)
        self.player.check_bounds(
            self.player, Background.frame_width, Background.frame_height
        )
        self.player.update()

        Player.player_list.draw(Background.world)

    def collision(self):
        if pygame.sprite.spritecollide(
            self.player, Castle.obstacle_list, False
        ) or pygame.sprite.spritecollide(self.player, Arrows.arrows_list, False):
            self.player_done = True
            return self.player_done
        else:
            self.score += 1
            font = pygame.font.Font(None, 50)
            white = pygame.Color("white")
            score_image = font.render(f"Your Score: {self.score}", True, white)
            Background.world.blit(score_image, (940, 10))
            pygame.display.update()

    def add_castle(self):
        self.frame_count += 1
        if self.frame_count == 90:
            self.frame_count = 0
            self.obstacle.add_obstacle(
                Background.frame_width, Background.frame_height, Castle.obstacle_list
            )

        Castle.obstacle_list.update()
        Castle.obstacle_list.draw(Background.world)

    def add_arrows(self):
        self.arrows_frame_count += 1
        if self.arrows_frame_count == 80:
            self.arrows_frame_count = 0
            self.arrows.add_arrows(Background.frame_width, Arrows.arrows_list)

        Arrows.arrows_list.update()
        Arrows.arrows_list.draw(Background.world)

    def end_screen(self):
        if self.collision():
            if self.endscreen.display():
                self.add_dragon()
