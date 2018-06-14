from PIL import Image


def bgra_surf_to_rgba_string(cairo_surface):
    # We use PIL to do this
    img = Image.frombuffer(
        'RGBA', (cairo_surface.get_width(),
                 cairo_surface.get_height()),
        cairo_surface.get_data().tobytes(), 'raw', 'BGRA', 0, 1)
    return img.tobytes('raw', 'RGBA', 0, 1)