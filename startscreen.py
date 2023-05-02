import pygame
from pygame.locals import *

pygame.font.init()


class StartScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.font = pygame.font.Font(None, 50)
        self.title_text = self.font.render("Dragon Game", True, (255, 255, 255))
        self.start_button_rect = pygame.Rect(200, 200, 200, 100)
        self.start_button_text = self.font.render("Start", True, (0, 0, 0))

    def display(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.start_button_rect.collidepoint(mouse_pos):
                        return "start"

            self.screen.fill((0, 0, 0))
            self.screen.blit(
                self.title_text, (self.width / 2 - self.title_text.get_width() / 2, 100)
            )
            pygame.draw.rect(self.screen, (255, 255, 255), self.start_button_rect)
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
