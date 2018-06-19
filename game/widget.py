from typing import Tuple

from pygame.rect import Rect

class GameObject:

    def __init__(self, game):
        self.game = game
        self.widget = None



class Widget:

    def __init__(self, game, box: Rect, parent: GameObject = None):
        self.game = game
        self.parent = parent
        self.box: Rect = box
        self.parent = parent
        self.active = False

    def is_in_box(self, pos: Tuple[int, int]):
        return self.box.collidepoint(*pos)

    def update(self, box):
        self.box = box

    def handle(self, pos):
        if self.active and ((not self.is_in_box(pos)) or (self.game.active_widget is not None and self.game.active_widget != self)):
            self.on_exit()
        if not self.active and self.is_in_box(pos) and not (self.game.active_widget is not None and self.game.active_widget.is_in_box(pos)):
            self.on_enter()

    def on_enter(self):
        self.active = True
        self.game.active_widget = self
        print('entered')

    def on_exit(self):
        self.active = False
        self.game.active_widget = None
        print('exited')

    def __eq__(self, other):
        return self.box == other.box