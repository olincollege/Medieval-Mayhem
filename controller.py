import pygame
import sys


class Controller:
    def __init__(self):
        pass

    def controller(self, player, steps):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False

            if event.type == pygame.KEYDOWN:
                if event.key == ord("q"):
                    pygame.quit()
                    try:
                        sys.exit()
                    finally:
                        main = False
                if event.key == pygame.K_UP or event.key == ord("w"):
                    player.control(0, -steps, 5)
                    player.update_image()
                if event.key == pygame.K_DOWN or event.key == ord("s"):
                    player.control(0, steps, 5)
                    player.update_image()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == ord("w"):
                    player.control(0, steps, 0)
                    player.update_image()

                if event.key == pygame.K_DOWN or event.key == ord("s"):
                    player.control(0, -steps, 0)
                    player.update_image()
