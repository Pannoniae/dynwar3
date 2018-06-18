import ctypes

import cairo

PyBUF_READ = 0x100
PyBUF_WRITE = 0x200


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
    pixels_ptr = ctypes.pythonapi.PyMemoryView_FromMemory(ctypes.c_void_p(ss.pixels),
                                                          ss.pitch * ss.h,
                                                          PyBUF_WRITE)
    pixels = ctypes.cast(pixels_ptr, ctypes.py_object).value
    return cairo.ImageSurface.create_for_data(pixels, cairo.FORMAT_RGB24, ss.w, ss.h, ss.pitch)