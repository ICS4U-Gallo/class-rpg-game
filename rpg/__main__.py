import pygame

from .game import Game
from .title_screen import TitleScreen
from .shop_screen import ShopScreen

pygame.init()
pygame.font.init()

game = Game(ShopScreen())
game.run()
