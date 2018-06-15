import math
import sys

import numpy

import cairo
import pygame

from game.hexmap import flat_hex_corner, Hex, HexMap, TerrainType
from game.layout import HexMapLayout
from game.util import bgra_surf_to_rgba_string

width, height = 800, 600

def draw(ctx, mouse_pos):
    ctx.set_line_width(1)
    ctx.set_source_rgba(0.6, 0, 0.4, 1)
    for hex in hm:
        r, g, b = layout.colors[hex.terrain]
        if hex.terrain != 10:
            print(hex.terrain)
        #print(Hex(2, 2).terrain)
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

    if mouse_pos:
        ctx.set_source_rgba(1, 0, 0, 1)
        ctx.arc(*layout.get_containing_hex_center(mouse_pos), 10, 0, math.pi * 2)
        ctx.stroke()


pygame.display.init()
screen = pygame.display.set_mode((width, height), 0, 32)

data = numpy.empty(width * height * 4, dtype = numpy.int8)
cairo_surface = cairo.ImageSurface.create_for_data(
    data, cairo.FORMAT_ARGB32, width, height, width * 4)
hm = HexMap(10)
i = Hex(2, 2)
i.terrain = TerrainType.t_hll
hm.set_hex((2, 2), i)
layout = HexMapLayout(hm, 20, (100, 100))
ctx = cairo.Context(cairo_surface)

clock = pygame.time.Clock()
while 1:
    for e in pygame.event.get():
        # if e.type == pygame.MOUSEMOTION:
        pos = pygame.mouse.get_pos()
        draw(ctx, pos)
        if e.type == pygame.QUIT:
            sys.exit()
        data_string = bgra_surf_to_rgba_string(cairo_surface)

        # Create PyGame surface
        pygame_surface = pygame.image.frombuffer(
                data_string, (width, height), 'RGBA')
        screen.blit(pygame_surface, (0, 0))
        pygame.display.update()