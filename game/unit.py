from game.util import get_rect_by_size
from game.widget import GameObject, Widget


class Unit(GameObject):
    def __init__(self, game, hex):
        super().__init__(game)
        self.game = game
        self.hex = hex

        self.hp = 10

        self.reload()

    def move(self, direction):
        self.game.hm.move_unit(self, direction)
        self.reload()

    def can_attack(self, other):
        if not self.game.hexmap.is_adjacent(self.hex, other.hex):
            return False
        else:
            return True

    def attack(self, other):
        if not self.can_attack(other):
            return

        # DUMMY
        other.hp -= 2
        self.hp -= 1

    def reload(self):
        if not self.widget:
            self.widget = self.game.add_widget(
                    Widget(self.game, get_rect_by_size(self.game.renderer.layout.get_hex_upper_corner(self.hex),
                                            self.game.renderer.layout.size * 2), self))
        else:
            box = get_rect_by_size(self.game.renderer.layout.get_hex_upper_corner(self.hex),
                                   self.game.renderer.layout.size * 2)
            self.widget.update(box)

class Infantry(Unit):
    pass