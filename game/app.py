import pygame

from game.gamestate import Game
from game.util import get_cairo_surface

width, height = 1920, 1080

pygame.init()
screen = pygame.display.set_mode((width, height), 0, 32)
cairo_surface = get_cairo_surface(screen)

game = Game(screen, cairo_surface)