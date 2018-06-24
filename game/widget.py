from typing import Tuple

from pygame.rect import Rect


class NoActiveWidgetError(Exception):
    pass


class GameObject:

    def __init__(self, game):
        self.game = game
        self.widget = None

    def on_click(self):
        if self.game.active_widget is None:
            self.game.active_widget = self.widget
        if issubclass(type(self), type(self.game.active_widget.parent)):
            if self.widget == self.game.active_widget:
                return
        return True # if returned True, execution can continue




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

    def destroy(self):
        self.game.remove_widget(self)

    def handle(self, pos: Tuple[int, int]):
        """ Have to refactor this, this is a mess due to the bandaids fixing the bugs """
        if self.active and self.game.hovered_widget is None:
            self.on_exit()
        if not self.is_in_box(pos) and self.game.hovered_widget is not None and self.game.hovered_widget == self:
            self.on_exit()
        if (self.game.hovered_widget is None or self.game.hovered_widget != self)\
                and self.is_in_box(pos)\
                and (self.game.hovered_widget is None or not self.game.hovered_widget.is_in_box(pos)):
            self.on_enter()

    def click_handle(self, pos: Tuple[int, int]):
        """ Handle clicking. """
        if self.is_in_box(pos):
            self.on_click()

    def on_enter(self):
        self.game.hovered_widget = self
        self.active = True

    def on_exit(self):
        self.game.hovered_widget = None
        self.active = False

    def on_click(self):
        self.parent.on_click()

    def __eq__(self, other):
        return self.box == other.box