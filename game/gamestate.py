import cairo
import pygame

from game.io.eventhandler import EventHandler
from game.hexmap import HexMap
from game.io.gameio import SaveGameLoader
from game.io.renderer import Renderer
from game.widget import Widget


class Game:
    def __init__(self, screen: pygame.Surface, surf: cairo.Surface, debug = False):

        self.debug = debug

        self.surf = surf

        self.event_handler = EventHandler(self)
        self.clock = pygame.time.Clock()
        self.widgets = []
        self.active_widget: Widget = None

        self.hexmap: HexMap = None

        self.loader = SaveGameLoader(self, 'data/save.yml')
        self.loader.load_game()

        self.renderer = Renderer(screen, self)

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