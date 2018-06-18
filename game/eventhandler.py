import sys

import pygame


class EventHandler:

    def __init__(self, game):
        self.game = game

    def handle_events(self):
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    self.game.renderer.layout.offset[0] -= 10
                if e.key == pygame.K_RIGHT:
                    self.game.renderer.layout.offset[0] += 10
                if e.key == pygame.K_UP:
                    self.game.renderer.layout.offset[1] -= 10
                if e.key == pygame.K_DOWN:
                    self.game.renderer.layout.offset[1] += 10
            if e.type == pygame.QUIT:
                sys.exit()