import pygame

from .game import Game

pygame.init()
pygame.font.init()

game = Game()
game.run()
