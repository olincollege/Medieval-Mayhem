import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the width and height of the screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT - self.rect.height - 10
        self.change_x = 0

    def update(self):
        self.rect.x += self.change_x
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0


class CastleObstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 50])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 3
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

    def add_obstacle(self):
        obstacle = CastleObstacle()
        obstacle.rect.x = random.randrange(SCREEN_WIDTH - obstacle.rect.width)
        obstacle.rect.y = -obstacle.rect.height
        return obstacle


# Initialize Pygame
pygame.init()

# Set the height and width of the screen
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Castle Game")

# Create the player sprite
player = Player()

# Create groups for all sprites and obstacles
all_sprites_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()

# Add the player sprite to the all_sprites_group
all_sprites_group.add(player)

# Set the frame rate
clock = pygame.time.Clock()

# Loop until the user clicks the close button
done = False

# Main game loop
while not done:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.change_x = -6
            elif event.key == pygame.K_RIGHT:
                player.change_x = 6
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.change_x = 0

    # Spawn obstacles at random intervals
    if random.randrange(100) < 3:
        obstacle = CastleObstacle()
        all_sprites_group.add(obstacle)
        obstacle_group.add(obstacle)

    # Update all sprites
    all_sprites_group.update()

    # Clear the screen
    screen.fill(WHITE)

    # Draw all the sprites
    all_sprites_group.draw(screen)

    # Check if the player collides with any obstacles
    if pygame.sprite.spritecollide(player, obstacle_group, False):
        done = True

    # Update the screen
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
