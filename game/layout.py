import math
from math import pi, cos, sin
from typing import Optional, Tuple


class HexMapLayout:

    def __init__(self, size: int = 20, offset: Optional[tuple] = None):
        if offset is None:
            offset = (0, 0)
        if type(offset) == tuple:
            offset = list(offset)
        self.size = size
        self.offset = offset

    def get_hex_position(self, pos: Tuple[float, float]) -> Tuple[float, float]:
        x = self.size * (3 / 2 * pos[0])
        y = self.size * (math.sqrt(3) / 2 * pos[0] + math.sqrt(3) * pos[1])
        x += self.offset[0]
        y += self.offset[1]
        return x, y

    def get_hex_upper_corner(self, pos: Tuple[float, float]) -> Tuple[float, float]:
        x, y = self.get_hex_position(pos)
        x -= self.size
        y -= self.size
        return x, y

    def pixel_to_hex(self, pos: Tuple[float, float]) -> Tuple[float, float]:
        _position = list(pos)
        _position[0] -= self.offset[0]
        _position[1] -= self.offset[1]
        x = (2 / 3 * _position[0]) / self.size
        y = (-1 / 3 * _position[0] + math.sqrt(3) / 3 * _position[1]) / self.size
        return self.hex_round((x, y))

    def hex_round(self, pos: Tuple[float, float]):
        """ USE THIS, otherwise results WILL be inexact """
        hex = _axial_to_cube(pos)
        cube = _cube_round(hex)
        hex2 = _cube_to_axial(cube)
        return hex2

    def get_containing_hex_center(self, pos: Tuple[float, float]) -> Tuple[float, float]:
        hex = self.pixel_to_hex(pos)
        return self.get_hex_position(hex)

    def flat_hex_corner(self, pos: Tuple[float, float], size: int, i: int):
        angle_deg = 60 * i
        angle_rad = pi / 180 * angle_deg
        return pos[0] + size * cos(angle_rad), pos[1] + size * sin(angle_rad)

def _cube_round(cube):
    rx = round(cube[0])
    ry = round(cube[1])
    rz = round(cube[2])

    x_diff = abs(rx - cube[0])
    y_diff = abs(ry - cube[1])
    z_diff = abs(rz - cube[2])

    if x_diff > y_diff and x_diff > z_diff:
        rx = -ry-rz
    elif y_diff > z_diff:
        ry = -rx-rz
    else:
        rz = -rx-ry

    return rx, ry, rz

def _cube_to_axial(cube: tuple):
    x = cube[0]
    y = cube[2]
    return x, y

def _axial_to_cube(hex: tuple):
    x = hex[0]
    z = hex[1]
    y = -x-z
    return x, y, z