import pygame
import random
import os
import background as Background


import pygame
import random
import os
import background as Background


class Castle(pygame.sprite.Sprite):
    obstacle_list = pygame.sprite.Group()

    def __init__(self, x, y, width, height):
        super().__init__()
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(
                os.path.join("images", "tower" + str(i) + ".png")
            ).convert()
            img = pygame.transform.scale(img, (width, height))
            self.images.append(img)
        self.image = self.images[random.randint(0, 1)]

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.velocity = 10  # change this value to control the speed of the obstacle

    def update(self):
        self.rect.x -= self.velocity

    def add_obstacle(self, worldx, worldy, obstacle_list):
        width = 200
        height = random.randint(200, 500)
        x = worldx + width
        y = worldy - height
        obstacle = Castle(x, y, width, height)
        obstacle_list.add(obstacle)
