""" Example functions copied from the Internet. Probably, we should not use them; they are here to test PyCairo. """

import math


def draw(ctx):
    ctx.set_line_width(15)
    ctx.arc(320, 240, 200, 0, 2 * math.pi)

    #                   r    g  b    a
    ctx.set_source_rgba(0.6, 0, 0.4, 1)
    ctx.fill_preserve()

    #                   r  g     b    a
    ctx.set_source_rgba(0, 0.84, 0.2, 0.5)
    ctx.stroke()

def bgra_surf_to_rgba_string(cairo_surface):
    # We use PIL to do this
    img = Image.frombuffer(
        'RGBA', (cairo_surface.get_width(),
                 cairo_surface.get_height()),
        cairo_surface.get_data(), 'raw', 'BGRA', 0, 1)

    return img.tostring('raw', 'RGBA', 0, 1)