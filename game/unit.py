from pygame.rect import Rect

from game.hexmap import Hex, Direction
from game.util import get_rect_by_size
from game.widget import Widget


class Unit:
    def __init__(self, game, hex: Hex):
        self.game = game
        self.hex = hex
        self.reload()

    def move(self, direction: Direction):
        self.game.hm.move_unit(self, direction)
        self.reload()

    def reload(self):
        self.widget = Widget(Rect(
                get_rect_by_size(self.game.renderer.layout.get_hex_upper_corner(self.hex),
                                 self.game.renderer.layout.size)))


class Infantry(Unit):
    pass