import sys

import pygame


class EventHandler:
    def handle_events(self):
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    self.layout.offset[0] -= 10
                if e.key == pygame.K_RIGHT:
                    self.layout.offset[0] += 10
                if e.key == pygame.K_UP:
                    self.layout.offset[1] -= 10
                if e.key == pygame.K_DOWN:
                    self.layout.offset[1] += 10
            if e.type == pygame.QUIT:
                sys.exit()