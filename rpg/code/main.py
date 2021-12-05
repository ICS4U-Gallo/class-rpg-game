import pygame
from config import *
from sprites import *
from pathfinder import *
from overworld import Overworld
from game import Game

pygame.init()

g = Game(Overworld())

g.run()