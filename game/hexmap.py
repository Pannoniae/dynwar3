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



class Hex:
    def __init__(self, x: int, y: int, terrain = TerrainType.t_clr):
        """ Are you surprised? """
        self.x = x
        self.y = y
        self.terrain = terrain

    def __add__(self, other):
        return Hex(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Hex(self.x - other.x, self.y - other.y)



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
        self.map = [[Hex(x, y) for x in range(sizex)] for y in range(sizey)]
        self.sizex = sizex
        self.sizey = sizey

    def get_neighbor(self, hex: Hex, direction):
        return Hex + self.neighbors[direction]

    def __str__(self):
        return f'<HexMap({self.sizex}, {self.sizey})>'