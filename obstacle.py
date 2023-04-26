import pygame
import random


class castle_obstacle(pygame.sprite.Sprite):
    obstacle_list = pygame.sprite.Group()

    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(0)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = 10  # change this value to control the speed of the obstacle

    def update(self):
        self.rect.x -= self.velocity

    def add_obstacle(self, worldx, worldy, obstacle_list):
        width = random.randint(100, 150)
        height = random.randint(100, 500)
        x = worldx + width
        y = worldy - height
        obstacle = castle_obstacle(x, y, width, height)
        obstacle_list.add(obstacle)
