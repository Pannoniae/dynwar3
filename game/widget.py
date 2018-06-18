from typing import Tuple

from pygame.rect import Rect

from game.util import get_rect_by_size

class GameObject:

    def __init__(self, game):
        self.game = game
        self.widget = None

    def reload(self):
        if not self.widget:
            self.widget = self.game.add_widget(
                    Widget(get_rect_by_size(self.game.renderer.layout.get_hex_upper_corner(self.hex),
                                            self.game.renderer.layout.size * 2), self))
            self.game.add_widget(self.widget)

        box = get_rect_by_size(self.game.renderer.layout.get_hex_upper_corner(self.hex),
                               self.game.renderer.layout.size * 2)
        self.widget.update(box)


class Widget:

    def __init__(self, box: Rect, parent: GameObject = None):
        self.parent = parent
        self.box: Rect = box
        self.parent = parent
        self.active = False

    def is_in_box(self, pos: Tuple[int, int]):
        return self.box.collidepoint(*pos)

    def update(self, box):
        self.box = box

    def handle(self, pos):
        if not self.active and self.is_in_box(pos):
            self.on_enter()
        if self.active and not self.is_in_box(pos):
            self.on_exit()

    def on_enter(self):
        self.active = True
        print('entered')

    def on_exit(self):
        self.active = False
        print('exited')

    def __eq__(self, other):
        return self.box == other.box