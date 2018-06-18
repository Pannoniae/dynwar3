import math
import sys
from typing import List

import cairo
import pygame

from game.game import Game
from game.hexmap import flat_hex_corner, Hex, HexMap, TerrainType
from game.layout import HexMapLayout
from game.unit import Infantry
from game.util import get_cairo_surface

width, height = 1920, 1080




pygame.display.init()

# Initialize pygame with 32-bit colors. This setting stores the pixels
# in the format 0x00rrggbb.
pygame.init()
screen = pygame.display.set_mode((width, height), 0, 32)

# Get a reference to the memory block storing the pixel data.
pixels = pygame.surfarray.pixels2d(screen)

# Set up a Cairo surface using the same memory block and the same pixel
# format (Cairo's RGB24 format means that the pixels are stored as
# 0x00rrggbb; i.e. only 24 bits are used and the upper 16 are 0).
cairo_surface = get_cairo_surface(screen)

game = Game(screen)