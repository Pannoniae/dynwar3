import math
import random
from typing import List

import cairo
import pygame
from game.hexmap import Hex, TerrainType
from game.layout import HexMapLayout


class Renderer:
    colors = {
        'edge': (0.0, 0.5, 1.0),
        'HP': (0.9, 0.3, 0.0),
        TerrainType.t_clr: (0.5, 0.3, 0.1),
        TerrainType.t_hll: (0.7, 0.2, 0.3)}

    def __init__(self, screen: pygame.Surface, game):
        self.ctx = cairo.Context(game.surf)
        self.screen = screen
        self.game = game
        self.clock = pygame.time.Clock()
        self.layout = HexMapLayout(32, (100, 100))
    def draw(self, mouse_pos):

        self.ctx.set_source_rgba(0, 0, 0, 1)
        self.ctx.paint()

        self.ctx.set_line_width(1)
        self.ctx.set_source_rgba(0.6, 0, 0.4, 1)
        units: List[Hex] = []
        for hex in self.game.hexmap:
            if self.game.debug:
                r, g, b = self.colors[hex.terrain]
                self.ctx.set_source_rgba(r, g, b, 1)
                for corner in range(0, 7):
                    x, y = self.layout.flat_hex_corner(self.layout.get_hex_position(hex.pos), self.layout.size, corner)
                    self.ctx.line_to(x, y)
                self.ctx.fill()
            else:

                self.ctx.set_source_surface(self.game.surf.create_from_png(f'data/grass.png'),
                                            *self.layout.get_hex_upper_corner(hex.pos))
                self.ctx.paint()
            if self.game.debug:
                self.ctx.set_source_rgba(*self.colors['edge'], 1)
                for corner in range(0, 7):
                    x, y = self.layout.flat_hex_corner(self.layout.get_hex_position(hex.pos), self.layout.size, corner)
                    self.ctx.line_to(x, y)
            if hex.has_unit():
                units.append(hex)
            self.ctx.stroke()

        for hex in units:
            self.ctx.set_source_surface(self.game.surf.create_from_png('data/terrain/inf.png'),
                                        *self.layout.get_hex_upper_corner(hex.pos))
            self.ctx.paint()
            self.ctx.move_to(*self.layout.get_hex_position(hex.pos))
            self.ctx.set_source_rgba(*self.colors['HP'], 1)
            self.ctx.set_line_width(5)
            self.ctx.set_line_cap(cairo.LINE_CAP_ROUND)
            self.ctx.rel_move_to(-(self.layout.size / 2), self.layout.size / 2)
            self.ctx.rel_line_to(self.layout.size * hex.unit.hp / 10, 0)
            self.ctx.stroke()
        self.ctx.set_line_width(1)
        self.ctx.set_line_cap(cairo.LINE_CAP_BUTT)
        if self.game.debug:
            for widget in self.game.widgets:
                self.ctx.move_to(*widget.box.topleft)
                self.ctx.set_source_rgba(*self.colors['edge'], 1)
                for pos in ("topleft", "topright", "bottomright", "bottomleft"):
                    self.ctx.line_to(*getattr(widget.box, pos))
                self.ctx.close_path()
            self.ctx.stroke()

        if mouse_pos:
            self.ctx.set_source_rgba(1, 0, 0, 1)
            self.ctx.arc(*self.layout.get_containing_hex_center(mouse_pos), self.layout.size / 4, 0, math.pi * 2)
            self.ctx.stroke()


    def reload(self):
        for widget in self.game.widgets:
            widget.parent.reload()