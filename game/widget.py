from typing import Tuple

from pygame.rect import Rect

class GameObject:

    def __init__(self, game):
        self.game = game
        self.widget = None

    def on_enter(self):
        pass

    def on_exit(self):
        pass

    def on_click(self):
        self.widget.on_click()



class Widget:

    def __init__(self, game, box: Rect, parent: GameObject = None):
        self.game = game
        self.parent = parent
        self.box: Rect = box
        self.parent = parent
        self.active = False

    def is_in_box(self, pos: Tuple[int, int]):
        return self.box.collidepoint(*pos)

    def update(self, box: Rect):
        self.box = box

    def handle(self, pos: Tuple[int, int]):
        """ Have to refactor this, this is a mess due to the bandaids fixing the bugs """
        if self.active and self.game.active_widget is None:
            self.on_exit()
        if not self.is_in_box(pos) and self.game.active_widget is not None and self.game.active_widget == self:
            self.on_exit()
        if (self.game.active_widget is None or self.game.active_widget != self) and self.is_in_box(pos) and not (self.game.active_widget is not None and self.game.active_widget.is_in_box(pos)):
            self.on_enter()

    def click_handle(self, pos: Tuple[int, int]):
        """ Handle clicking. """
        if self.is_in_box(pos):
            self.on_click()

    def on_enter(self):
        self.game.active_widget = self
        self.active = True

    def on_exit(self):
        self.game.active_widget = None
        self.active = False

    def on_click(self):
        print('clickity, clickity')

    def __eq__(self, other):
        return self.box == other.box