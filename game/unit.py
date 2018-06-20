from game.util import get_rect_by_size
from game.widget import GameObject, Widget


class Unit(GameObject):
    def __init__(self, game, hex):
        super().__init__(game)
        self.game = game
        self.hex = hex
        self.reload()

    def move(self, direction):
        self.game.hm.move_unit(self, direction)
        self.reload()

    def reload(self):
        if not self.widget:
            self.widget = self.game.add_widget(
                    Widget(self.game, get_rect_by_size(self.game.renderer.layout.get_hex_upper_corner(self.hex),
                                            self.game.renderer.layout.size * 2), self))
            self.game.add_widget(self.widget)
        else:
            box = get_rect_by_size(self.game.renderer.layout.get_hex_upper_corner(self.hex),
                                   self.game.renderer.layout.size * 2)
            self.widget.update(box)

class Infantry(Unit):
    pass