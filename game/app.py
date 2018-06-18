import math
import sys
from typing import List

import cairo
import pygame

from game.hexmap import flat_hex_corner, Hex, HexMap, TerrainType
from game.layout import HexMapLayout
from game.unit import Infantry
from game.util import get_cairo_surface

width, height = 1920, 1080

def draw(ctx, mouse_pos):

    ctx.set_source_rgba(0, 0, 0, 1)
    ctx.paint()

    ctx.set_line_width(1)
    ctx.set_source_rgba(0.6, 0, 0.4, 1)
    units: List[Hex] = []
    for hex in hm:
        r, g, b = layout.colors[hex.terrain]
        ctx.set_source_rgba(r, g, b, 1)
        for corner in range(0, 7):
            x, y = flat_hex_corner(Hex(*layout.get_hex_position(hex)), layout.size, corner)
            ctx.line_to(x, y)
        ctx.fill()
        ctx.set_source_rgba(*layout.EDGE_COLOR, 1)
        for corner in range(0, 7):
            x, y = flat_hex_corner(Hex(*layout.get_hex_position(hex)), layout.size, corner)
            ctx.line_to(x, y)
        ctx.stroke()
        if hex.has_unit():
            units.append(hex)
    for hex in units:
        ctx.set_source_surface(cairo_surface.create_from_png('data/inf.png'), *layout.get_hex_upper_corner(hex))
        ctx.paint()

    if mouse_pos:
        ctx.set_source_rgba(1, 0, 0, 1)
        ctx.arc(*layout.get_containing_hex_center(mouse_pos), layout.size / 4, 0, math.pi * 2)
        ctx.stroke()


pygame.display.init()
screen = pygame.display.set_mode((width, height), 0, 32)

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
hm = HexMap(10)
u = Infantry()
i = Hex(2, 2)
i.terrain = TerrainType.t_hll
i.set_unit(u)
hm.set_hex((2, 2), i)
layout = HexMapLayout(hm, 20, (100, 100))
ctx = cairo.Context(cairo_surface)

clock: pygame.time.Clock = pygame.time.Clock()
while 1:

    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                layout.offset[0] -= 10
            if e.key == pygame.K_RIGHT:
                layout.offset[0] += 10
            if e.key == pygame.K_UP:
                layout.offset[1] -= 10
            if e.key == pygame.K_DOWN:
                layout.offset[1] += 10
        if e.type == pygame.QUIT:
            sys.exit()
    pos = pygame.mouse.get_pos()
    draw(ctx, pos)
    pygame.display.update()
    clock.tick()
    print(clock.get_fps())