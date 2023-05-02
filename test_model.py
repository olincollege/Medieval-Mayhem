import pytest
from player import Player
from model import DragonModel
from obstacle import Arrows
from obstacle import Castle
from background import Background

# Create instance of Player
test_player = Player()

# Create instance of DragonModel
test_model = DragonModel(test_player)

# Create instance of Arrows
test_arrows = Arrows(20, 100)
test_arrows.add_arrows(Background.frame_width, Arrows.arrows_list)

# Set y position for player
test_player.rect.y = 130

print(f"arrows x: {test_arrows.rect.x}")
print(f"arrows y: {test_arrows.rect.y}")
print(f"player x: {test_player.rect.x}")
print(f"player y: {test_player.rect.y}")



assert test_model.collision() is True
