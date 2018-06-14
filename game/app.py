import sys

import pygame
pygame.init()

w, h = 800, 600
screen = pygame.display.set_mode((w, h))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()