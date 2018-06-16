""" Example functions copied from the Internet. Probably, we should not use them; they are here to test PyCairo. """
import numpy

import cairo
import pygame
import array
import math
import sys


def draw(surface):
    x, y, radius = (250, 250, 200)
    ctx = cairo.Context(surface)
    ctx.set_line_width(15)
    ctx.arc(x, y, radius, 0, 2.0 * math.pi)
    ctx.set_source_rgb(0.8, 0.8, 0.8)
    ctx.fill_preserve()
    ctx.set_source_rgb(1, 1, 1)
    ctx.stroke()


def input(events):
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit(0)

        # Create Cairo Surface


Width, Height = 512, 512
#data = array.array('c', chr(0) * Width * Height * 4)
data = numpy.empty(Width * Height * 4, dtype = numpy.int8)
stride = Width * 4
surface = cairo.ImageSurface.create_for_data(data, cairo.FORMAT_ARGB32, Width, Height, stride)
# init PyGame
pygame.init()
window = pygame.display.set_mode((Width, Height))
screen = pygame.display.get_surface()
# Draw with Cairo
draw(surface)
# Create PyGame surface from Cairo Surface
image = pygame.image.frombuffer(data, (Width, Height), "ARGB")
# Tranfer to Screen


while True:
    x, y, radius = (350, 150, 100)
    ctx = cairo.Context(surface)
    ctx.set_line_width(15)
    ctx.arc(x, y, radius, 0, 2.0 * math.pi)
    ctx.set_source_rgb(0.8, 0.8, 0.8)
    ctx.fill_preserve()
    ctx.set_source_rgb(1, 1, 1)
    ctx.stroke()
    image = pygame.image.frombuffer(data.tostring(), (Width, Height), "ARGB")
    screen.blit(image, (0, 0))
    pygame.display.flip()
    input(pygame.event.get())