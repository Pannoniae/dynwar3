import math
from typing import List

import cairo
import pygame
from game.app import cairo_surface
from game.game import Game
from game.hexmap import Hex, flat_hex_corner
from game.layout import HexMapLayout


class Renderer:

    def __init__(self, screen: pygame.Surface, game: Game):
        self.ctx = cairo.Context(cairo_surface)
        self.screen = screen
        self.game = game
        self.clock = pygame.time.Clock()
        self.layout = HexMapLayout(self.game.hm, 20, (100, 100))
    def draw(self, ctx, mouse_pos):

        ctx.set_source_rgba(0, 0, 0, 1)
        ctx.paint()

        ctx.set_line_width(1)
        ctx.set_source_rgba(0.6, 0, 0.4, 1)
        units: List[Hex] = []
        for hex in self.game.hm:
            r, g, b = self.layout.colors[hex.terrain]
            ctx.set_source_rgba(r, g, b, 1)
            for corner in range(0, 7):
                x, y = flat_hex_corner(Hex(*self.layout.get_hex_position(hex)), self.layout.size, corner)
                ctx.line_to(x, y)
            ctx.fill()
            ctx.set_source_rgba(*self.layout.EDGE_COLOR, 1)
            for corner in range(0, 7):
                x, y = flat_hex_corner(Hex(*self.layout.get_hex_position(hex)), self.layout.size, corner)
                ctx.line_to(x, y)
            ctx.stroke()
            if hex.has_unit():
                units.append(hex)
        for hex in units:
            ctx.set_source_surface(cairo_surface.create_from_png('data/inf.png'), *self.layout.get_hex_upper_corner(hex))
            ctx.paint()

        if mouse_pos:
            ctx.set_source_rgba(1, 0, 0, 1)
            ctx.arc(*self.layout.get_containing_hex_center(mouse_pos), self.layout.size / 4, 0, math.pi * 2)
            ctx.stroke()