import logging

import cairo
import pygame

from game.io.eventhandler import EventHandler
from game.hexmap import HexMap
from game.io.gameio import SaveGameLoader
from game.io.renderer import Renderer
from game.unit import Unit
from game.widget import Widget


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

        while 1:
            self.main_loop()

    def main_loop(self):
        self.event_handler.handle_events()
        pos = pygame.mouse.get_pos()
        self.renderer.draw(pos)
        pygame.display.update()
        self.clock.tick()
        #print(self.clock.get_fps())

    def remove_widget(self, widget: Widget):
        self.widgets.remove(widget)

    def add_widget(self, widget: Widget):
        self.widgets.append(widget)
        return widget