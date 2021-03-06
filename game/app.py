import sys

import pygame

from game.controller import Game
from game.util import get_cairo_surface

#width, height = 1920, 1080
width, height = 800, 600

pygame.init()
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('DynWar v0.1-dev', 'DynWar')
cairo_surface = get_cairo_surface(screen)

try:
    debug = sys.argv[1] == 'debug'
except IndexError:
    debug = False
print(f'Debug mode: {debug}')
game = Game(screen, cairo_surface, debug = debug)