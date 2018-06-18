import ctypes

import cairo
from PIL import Image


def bgra_surf_to_rgba_string(cairo_surface):
    # We use PIL to do this
    img = Image.frombuffer(
        'RGBA', (cairo_surface.get_width(),
                 cairo_surface.get_height()),
        cairo_surface.get_data().tobytes(), 'raw', 'BGRA', 0, 1)
    return img.tobytes('raw', 'RGBA', 0, 1)


def get_cairo_surface(pygame_surface):

    """ Black magic. """

    class Surface(ctypes.Structure):
        _fields_ = [
         (
          'HEAD', ctypes.c_byte * object.__basicsize__),
         (
          'SDL_Surface', ctypes.c_void_p)]

    class SDL_Surface(ctypes.Structure):
        _fields_ = [
         (
          'flags', ctypes.c_uint),
         (
          'SDL_PixelFormat', ctypes.c_void_p),
         (
          'w', ctypes.c_int),
         (
          'h', ctypes.c_int),
         (
          'pitch', ctypes.c_ushort),
         (
          'pixels', ctypes.c_void_p)]

    surface = Surface.from_address(id(pygame_surface))
    ss = SDL_Surface.from_address(surface.SDL_Surface)
    #pixels_ptr = ctypes.pythonapi.PyBuffer_FromReadWriteMemory(ctypes.c_void_p(ss.pixels), ss.pitch * ss.h)
    pixels_ptr = ctypes.pythonapi.PyMemoryView_FromMemory(ctypes.c_void_p(ss.pixels),
                                                          ss.pitch * ss.h,
                                                          0x200)
    pixels = ctypes.cast(pixels_ptr, ctypes.py_object).value
    print(pixels.readonly)
    return cairo.ImageSurface.create_for_data(pixels, cairo.FORMAT_RGB24, ss.w, ss.h, ss.pitch)