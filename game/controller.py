import logging

import cairo
import pygame
from pygame.rect import Rect

from game.io.eventhandler import EventHandler
from game.hexmap import HexMap
from game.io.gameio import SaveGameLoader
from game.io.renderer import Renderer
from game.widget import Widget, GameObject


class Game:

    _inst = None
    def __new__(cls, *args, **kwargs):
        if cls._inst is not None:
            logging.warning('More than one Game() instance has been instantiated. This is probably a programming error.')
        cls._inst = object.__new__(cls)
        return cls._inst

    def __init__(self, screen: pygame.Surface, surf: cairo.Surface, debug = False):

        self.debug = debug

        self.surf = surf

        self.event_handler = EventHandler(self)
        self.clock = pygame.time.Clock()
        self.widgets = []
        self.hovered_widget: Widget = None
        self.active_widget: Widget = None

        self.hexmap: HexMap = None

        self.renderer = Renderer(screen, self)

        self.loader = SaveGameLoader(self, 'data/save.yml')
        self.loader.load_game()

        self.active_faction = 0
        self.turn = 0

        while 1:
            self.main_loop()


    def main_loop(self):
        self.event_handler.handle_events()
        pos = pygame.mouse.get_pos()
        self.renderer.draw(pos)
        pygame.display.update()
        self.clock.tick()
        #print(self.clock.get_fps())

    def end_turn(self):
        if self.active_faction == 0:
            self.active_faction = 1
        elif self.active_faction == 1:
            self._end_turn()

    def _end_turn(self):
        """ End turn if all players are ready. """
        self.turn += 1
        self.active_faction = 0

    def remove_widget(self, widget: Widget):
        self.widgets.remove(widget)

    def _add_widget(self, widget: Widget):
        self.widgets.append(widget)
        return widget

    def add_widget(self, box: Rect, parent: GameObject = None):
        w = Widget(self, box, parent)
        return self._add_widget(w)


