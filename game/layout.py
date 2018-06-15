import math

from game.hexmap import HexMap, Hex, TerrainType


class HexMapLayout:

    EDGE_COLOR = 0.8, 0.6, 0.6
    colors = {TerrainType.t_clr: (0.5, 0.3, 0.1),
              TerrainType.t_hll: (0.7, 0.2, 0.3)}

    def __init__(self, hexmap: HexMap, size: int = 20, offset: tuple = (0, 0)):
        self.size = size
        self.offset = offset

    def get_hex_position(self, hex: Hex):
        x = self.size * (3 / 2 * hex.x)
        y = self.size * (math.sqrt(3) / 2 * hex.x + math.sqrt(3) * hex.y)
        x += self.offset[0]
        y += self.offset[1]
        return x, y

    def pixel_to_hex(self, position: tuple):
        _position = list(position)
        _position[0] -= self.offset[0]
        _position[1] -= self.offset[1]
        x = (2 / 3 * _position[0]) / self.size
        y = (-1 / 3 * _position[0] + math.sqrt(3) / 3 * _position[1]) / self.size
        return self.hex_round((x, y))

    def hex_round(self, position: tuple):
        """ USE THIS, otherwise results WILL be inexact """
        hex = _axial_to_cube(position)
        cube = _cube_round(hex)
        hex2 = _cube_to_axial(cube)
        return Hex(*hex2)


    def get_containing_hex_center(self, position: tuple):
        hex = self.pixel_to_hex(position)
        print(self.get_hex_position(hex))
        return self.get_hex_position(hex)

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