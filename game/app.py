import numpy

import cairo
import pygame
import math

from game.example import bgra_surf_to_rgba_string

def draw(ctx):
    ctx.set_line_width(15)
    ctx.arc(320, 240, 200, 0, 2 * math.pi)

    #                   r    g  b    a
    ctx.set_source_rgba(0.6, 0, 0.4, 1)
    ctx.fill_preserve()

    #                   r  g     b    a
    ctx.set_source_rgba(0, 0.84, 0.2, 0.5)
    ctx.stroke()

width, height = 800, 600

pygame.display.init()
screen = pygame.display.set_mode((width, height), 0, 32)

# Create raw surface data (could also be done with something else than
# NumPy)
data = numpy.empty(width * height * 4, dtype=numpy.int8)

# Create Cairo surface
cairo_surface = cairo.ImageSurface.create_for_data(
    data, cairo.FORMAT_ARGB32, width, height, width * 4)

# Draw with Cairo on the surface
ctx = cairo.Context(cairo_surface)
draw(ctx)
 # On little-endian machines (and perhaps big-endian, who knows?),
# Cairo's ARGB format becomes a BGRA format. PyGame does not accept
# BGRA, but it does accept RGBA, which is why we have to convert the
# surface data. You can check what endian-type you have by printing
# out sys.byteorder
data_string = bgra_surf_to_rgba_string(cairo_surface)

# Create PyGame surface
pygame_surface = pygame.image.frombuffer(
    data_string, (width, height), 'RGBA')

screen.blit(pygame_surface, (0,0))
pygame.display.flip()

clock = pygame.time.Clock()
while not pygame.QUIT in [e.type for e in pygame.event.get()]:
    clock.tick(30)