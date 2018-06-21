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

        if self.hp <= 0:
            self.destroy()
        if other.hp <= 0:
            other.destroy()

    def destroy(self):
        self.widget.destroy()
        self.hex.unit = None

    def reload(self):
        if not self.widget:
            self.widget = self.game.add_widget(
                    Widget(self.game, get_rect_by_size(self.game.renderer.layout.get_hex_upper_corner((self.hex.x, self.hex.y)),
                                            self.game.renderer.layout.size * 2), self))
        else:
            box = get_rect_by_size(self.game.renderer.layout.get_hex_upper_corner((self.hex.x, self.hex.y)),
                                   self.game.renderer.layout.size * 2)
            self.widget.update(box)

    def on_click(self):
        if self.game.active_widget is None:
            self.game.active_widget = self.widget
        elif self.game.active_widget is self.widget:
            return
        elif self.game.active_widget is not self.widget:
            attacker = self.game.active_widget.parent
            attacker.attack(self)
            self.game.active_widget = None

class Infantry(Unit):
    pass