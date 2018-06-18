import cairo
import pygame
from pygame.rect import Rect

from game.io.eventhandler import EventHandler
from game.hexmap import HexMap, Hex, TerrainType
from game.io.renderer import Renderer
from game.unit import Infantry
from game.widget import Widget


class Game:
    def __init__(self, screen: pygame.Surface, surf: cairo.Surface, debug = False):

        self.debug = debug

        self.surf = surf

        self.event_handler = EventHandler(self)
        self.clock = pygame.time.Clock()
        self.widgets = []

        self.hm = HexMap(10)
        i = Hex(2, 2)
        u = Infantry(self, i)
        i.terrain = TerrainType.t_hll
        i.set_unit(u)
        self.hm.set_hex((2, 2), i)

        self.renderer = Renderer(screen, self)

        u.reload()

        while 1:
            self.main_loop()

    def main_loop(self):
        self.event_handler.handle_events()
        pos = pygame.mouse.get_pos()
        self.renderer.draw(self.renderer.ctx, pos)
        pygame.display.update()
        self.clock.tick()
        #print(self.clock.get_fps())

    def remove_widget(self, widget: Widget):
        for widget_ in self.widgets:
            if widget_ == widget:
                self.widgets.remove(widget_)

    def add_widget(self, widget: Widget):
        self.widgets.append(widget)
        return widget