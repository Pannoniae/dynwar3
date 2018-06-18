import sys

import pygame

from game.gamestate import Game
from game.util import get_cairo_surface

width, height = 1920, 1080

pygame.init()
screen = pygame.display.set_mode((width, height), 0, 32)
cairo_surface = get_cairo_surface(screen)

try:
    sys.argv[1]
    debug = True
except IndexError:
    debug = False
print(f'Debug mode: {debug}')

game = Game(screen, cairo_surface, debug = debug)