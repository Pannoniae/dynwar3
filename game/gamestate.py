import cairo
import pygame

from game.eventhandler import EventHandler
from game.hexmap import HexMap, Hex, TerrainType
from game.renderer import Renderer
from game.unit import Infantry


class Game:
    def __init__(self, screen: pygame.Surface, surf: cairo.Surface):
        self.surf = surf
        self.hm = HexMap(10)
        u = Infantry()
        i = Hex(2, 2)
        i.terrain = TerrainType.t_hll
        i.set_unit(u)
        self.hm.set_hex((2, 2), i)
        self.renderer = Renderer(screen, self)
        self.event_handler = EventHandler(self)
        self.clock = pygame.time.Clock()
        while 1:
            self.main_loop()

    def main_loop(self):
        self.event_handler.handle_events()
        pos = pygame.mouse.get_pos()
        self.renderer.draw(self.renderer.ctx, pos)
        pygame.display.update()
        self.clock.tick()