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
            img.set_colorkey(img.get_at((0,0)))
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


class Arrows(pygame.sprite.Sprite):

    arrows_list = pygame.sprite.Group()

    def __init__(self, x, y):
        super().__init__()
        image_width = 200
        image_height = 150
        self.image = pygame.image.load(os.path.join("images", "arrows.png")).convert()
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.image = pygame.transform.scale(self.image, (image_width, image_height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = random.randint(20, 30)

    def update(self):
        self.rect.x -= self.velocity

    def add_arrows(self, frame_width, arrows_list):
        width = random.randint(200, 400)
        height = random.randint(50, 250)
        x = frame_width + width
        y = height
        obstacle = Arrows(x, y)
        arrows_list.add(obstacle)

