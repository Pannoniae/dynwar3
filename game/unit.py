from pygame.rect import Rect

from game.util import get_rect_by_size
from game.widget import Widget


class Unit:
    def __init__(self, game, hex):
        self.game = game
        self.hex = hex
        self.widget = None
        #self.reload()

    def move(self, direction):
        self.game.hm.move_unit(self, direction)
        self.reload()

    def reload(self):
        if self.widget:
            self.game.remove_widget(self.widget)
        self.widget = self.game.add_widget(Widget(
                get_rect_by_size(self.game.renderer.layout.get_hex_upper_corner(self.hex),
                                 self.game.renderer.layout.size)))


class Infantry(Unit):
    pass