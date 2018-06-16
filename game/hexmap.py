from math import cos, sin, pi
from typing import Optional

from game.unit import Unit


class TerrainType:
    t_sea = 0
    t_clr = 10
    t_mtn = 20
    t_hll = 21
    t_for = 30
    t_cty = 40
    t_des = 50

    @classmethod
    def major_type_for(cls, terrain):
        return terrain - (terrain % 10)

    @classmethod
    def is_major_type(cls, terrain):
        return terrain % 10 == 0

    @classmethod
    def is_minor_type(cls, terrain):
        return not cls.is_major_type(terrain)

class UnitNotFound(Exception):
    pass

class Hex:

    # Just a singleton, but we like to write unreadable code
    #_insts = {}
    #def __new__(cls, *args, **kwargs):
    #    x, y, *rest = args
    #    if (x, y) not in cls._insts.keys():
    #        cls._insts[(x, y)] = object.__new__(cls)
    #    return cls._insts[(x, y)]

    def __init__(self, x: int, y: int, terrain = TerrainType.t_clr):
        """ Are you surprised? """
        self.x = x
        self.y = y
        self.terrain = terrain
        self.unit: Optional[Unit] = None

    def get_unit(self):
        if self.unit is None:
            raise UnitNotFound('No unit in this hex')

    def set_unit(self, unit: Unit):
        self.unit = unit

    def has_unit(self):
        return self.unit is not None

    def __add__(self, other):
        return Hex(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Hex(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f'<Hex({self.x}, {self.y})>'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.terrain == other.terrain

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.x) * 10 + hash(self.y)



class Direction:
    SOUTHEAST = 0
    NORTHEAST = 1
    NORTH = 2
    NORTHWEST = 3
    SOUTHWEST = 4
    SOUTH = 5


class HexMap:
    neighbors = [Hex(+1, 0),
                 Hex(+1, -1),
                 Hex(0, -1),
                 Hex(-1, 0),
                 Hex(-1, +1),
                 Hex(0, +1)]

    def __init__(self, sizex: int, sizey: int = None):
        if not sizey:
            sizey = sizex
        self.map = {(x, y): Hex(x, y) for x in range(sizex) for y in range(sizey)}
        self.sizex = sizex
        self.sizey = sizey

    def get_neighbor(self, hex: Hex, direction):
        return hex + self.neighbors[direction]

    @staticmethod
    def get_hexes_in_range(hex: Hex, n: int):
        for x in range(-n, n+1):
            for y in range(max(-n, -x - n), min(n, -x + n) + 1):
                yield hex + Hex(x, y)

    @staticmethod
    def distance(hex: Hex, other: Hex):
        return (abs(hex.x - other.x) + + abs(hex.x + hex.y - other.x - other.y) + abs(hex.y - other.y)) / 2

    def __repr__(self):
        return f'<HexMap({self.sizex}, {self.sizey})>'

    def __iter__(self):
        for hex in self.map.values():
            yield hex

    def set_hex(self, position: tuple, hex: Hex):
        self.map[position] = hex

    def get_hex(self, position: tuple):
        return self.map[position]


def flat_hex_corner(center: Hex, size, i):
    angle_deg = 60 * i
    angle_rad = pi / 180 * angle_deg
    return center.x + size * cos(angle_rad), center.y + size * sin(angle_rad)