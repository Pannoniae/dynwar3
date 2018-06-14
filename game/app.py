import numpy

import cairo
import pygame

from game.util import bgra_surf_to_rgba_string

width, height = 800, 600

pygame.display.init()
screen = pygame.display.set_mode((width, height), 0, 32)

data = numpy.empty(width * height * 4, dtype = numpy.int8)
cairo_surface = cairo.ImageSurface.create_for_data(
    data, cairo.FORMAT_ARGB32, width, height, width * 4)
ctx = cairo.Context(cairo_surface)
data_string = bgra_surf_to_rgba_string(cairo_surface)

# Create PyGame surface
pygame_surface = pygame.image.frombuffer(
    data_string, (width, height), 'RGBA')

screen.blit(pygame_surface, (0,0))
pygame.display.update()

clock = pygame.time.Clock()
while not pygame.QUIT in [e.type for e in pygame.event.get()]:
    clock.tick(30)