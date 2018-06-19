import cairo
import pygame

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
        self.active_widget: Widget = None

        self.hm = HexMap(10)
        i = Hex(2, 2)
        i2 = Hex(3, 2)
        u = Infantry(self, i)
        u2 = Infantry(self, i2)
        i.terrain = TerrainType.t_hll
        i2.terrain = TerrainType.t_hll
        i.set_unit(u)
        i2.set_unit(u2)
        self.hm.set_hex((2, 2), i)
        self.hm.set_hex((3, 2), i2)

        self.renderer = Renderer(screen, self)

        u.reload()
        u2.reload()

        self.ctr = 0
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