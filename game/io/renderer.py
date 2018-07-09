import logging
import math
from typing import List

import cairo
import pygame
from game.hexmap import Hex, TerrainType
from game.layout import HexMapLayout
from game.state import F_GER, F_SOV


class Renderer:


    def __init__(self, screen: pygame.Surface, game):

        self.drawing = {
            'edge': (0.0, 0.5, 1.0),
            'HP': (0.9, 0.3, 0.0),
            TerrainType.t_clr: (0.5, 0.3, 0.1),
            TerrainType.t_hll: self.draw_mountain # (0.7, 0.2, 0.3)}
        }

        self.ctx = cairo.Context(game.surf)
        self.screen = screen
        self.game = game
        self.clock = pygame.time.Clock()
        self.layout = HexMapLayout(32, (100, 100))

    def hex_outline(self, hex: Hex):
        for corner in range(0, 7):
            x, y = self.layout.flat_hex_corner(self.layout.get_hex_position(hex.pos), self.layout.size, corner)
            self.ctx.line_to(x, y)

    def draw_mountain(self, x: int, y: int):
        self.ctx.save()

        self.ctx.set_source_rgba(0.5, 0.5, 0.5, 1)
        self.ctx.set_line_width(3)
        size = self.layout.size * 2
        self.ctx.move_to(x + size / 4, y + size / 2)
        self.ctx.line_to(x + size * 3 / 8, y + size / 3)
        self.ctx.line_to(x + size / 2, y + size / 2)
        self.ctx.line_to(x + size * 5 / 8, y + size / 3)
        self.ctx.line_to(x + size * 3 / 4, y + size / 2)
        self.ctx.stroke()

        self.ctx.restore()

    def draw_hex(self, hex: Hex):
        self.hex_outline(hex)
        self.ctx.fill()

    def draw(self, mouse_pos):

        self.ctx.set_source_rgba(0, 0, 0, 1)
        self.ctx.paint()

        self.ctx.set_line_width(1)

        units: List[Hex] = []

        for hex in self.game.hexmap:

            val = self.drawing[hex.terrain]
            if callable(val):
                r, g, b = self.drawing[TerrainType.t_clr]
                self.ctx.set_source_rgba(r, g, b, 1)
                self.draw_hex(hex)
                val(*self.layout.get_hex_upper_corner(hex.pos))

            elif isinstance(val, tuple):
                r, g, b = val
                self.ctx.set_source_rgba(r, g, b, 1)
                self.draw_hex(hex)

            else:
                logging.warning(f'No handling for drawer {val}! Drawing nothing.')
                self.ctx.set_source_rgba(1, 1, 1, 1)
                self.draw_hex(hex)


            self.hex_outline(hex)

            self.select_country_color(hex)

            #else:
            #    self.ctx.set_source_surface(self.game.surf.create_from_png(f'data/terrain/grass.png'),
            #                                *self.layout.get_hex_upper_corner(hex.pos))
            #    self.ctx.paint()

            self.ctx.set_source_rgba(*self.drawing['edge'], 1)
            for corner in range(0, 7):
                x, y = self.layout.flat_hex_corner(self.layout.get_hex_position(hex.pos), self.layout.size, corner)
                self.ctx.line_to(x, y)
            if hex.unit:
                units.append(hex)
            self.ctx.stroke()

        for hex in units:
            self.ctx.set_source_surface(self.game.surf.create_from_png('data/units/inf.png'),
                                        *self.layout.get_hex_upper_corner(hex.pos))
            self.ctx.paint()
            self.draw_hp(hex)
            self.draw_flag(hex)
        self.ctx.set_line_width(1)
        self.ctx.set_line_cap(cairo.LINE_CAP_BUTT)
        if self.game.debug:
            for widget in self.game.widgets:
                self.ctx.move_to(*widget.box.topleft)
                self.ctx.set_source_rgba(*self.drawing['edge'], 1)
                for pos in ("topleft", "topright", "bottomright", "bottomleft"):
                    self.ctx.line_to(*getattr(widget.box, pos))
                self.ctx.close_path()
            self.ctx.stroke()

        if mouse_pos:
            self.ctx.set_source_rgba(1, 0, 0, 1)
            self.ctx.arc(*self.layout.get_containing_hex_center(mouse_pos), self.layout.size / 4, 0, math.pi * 2)
            self.ctx.stroke()

    def draw_hp(self, hex):
        self.ctx.move_to(*self.layout.get_hex_position(hex.pos))
        self.ctx.set_source_rgba(*self.drawing['HP'], 1)
        self.ctx.set_line_width(5)
        self.ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        self.ctx.rel_move_to(-(self.layout.size / 2), self.layout.size / 2)
        self.ctx.rel_line_to(self.layout.size * hex.unit.hp / 10, 0)
        self.ctx.stroke()

    def draw_flag(self, hex):
        self.ctx.move_to(*self.layout.get_hex_upper_corner(hex.pos))
        if hex.unit.country == F_GER:
            self.ctx.set_source_rgba(0.2, 0.2, 0.2, 1)
        elif hex.unit.country == F_SOV:
            self.ctx.set_source_rgba(1, 0, 0, 1)

        self.ctx.rel_line_to(8, 0)
        self.ctx.rel_line_to(0, 8)
        self.ctx.rel_line_to(-8, 0)
        self.ctx.rel_line_to(0, -8)
        self.ctx.fill()

    def select_country_color(self, hex):
        if hex.country == 0:
            self.ctx.set_source_rgba(0.0, 0.0, 0.0, 0.2)
        elif hex.country == 1:
            self.ctx.set_source_rgba(1.0, 0.0, 0.2, 0.2)
        self.ctx.fill()

    def reload(self):
        for widget in self.game.widgets:
            widget.parent.reload()
