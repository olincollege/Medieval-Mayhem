import pygame
import unittest
from player import Player as Pl
from obstacle import Castle as Co
from background import Background as Bg
from controller import Controller
from model import DragonModel

pygame.init()


class TestDragonGame(unittest.TestCase):
    def test_player(self):
        player = Pl()
        player.rect.x = 100
        player.rect.y = 200
        self.assertEqual(player.rect.x, 100)
        self.assertEqual(player.rect.y, 200)
        player.update()
        self.assertEqual(player.rect.y, 200)

    def test_castle(self):
        castle = Co(0, 0, 100, 100)
        castle.add_obstacle(100, 100, Co.obstacle_list)
        self.assertEqual(len(Co.obstacle_list), 1)
        castle.update()
        self.assertEqual(castle.rect.x, -10)

    def test_controller(self):
        controller = Controller()
        player = Pl()
        controller.controller(player, 0)
        self.assertEqual(player.rect.y, 0)
        controller.controller(player, -100)
        self.assertEqual(player.rect.y, 0)

    def test_dragon_model(self):
        dragon = DragonModel()
        dragon.add_dragon()
        self.assertEqual(len(Pl.player_list), 1)
        dragon.collision()
        self.assertEqual(dragon.score, 1)
        dragon.player.rect.x = -10
        dragon.update_dragon()
        self.assertEqual(dragon.player.rect.x, 0)


if __name__ == "__main__":
    unittest.main()
