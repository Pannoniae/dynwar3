class TerrainType:
    t_sea = 0
    t_clr = 10
    t_mtn = 20
    t_hll = 21
    t_for = 30
    t_cty = 40
    t_des = 50

    @classmethod
    def majorType(cls, terrain):
        return terrain - (terrain % 10)

    @classmethod
    def isMajorType(cls, terrain):
        return terrain % 10 == 0

    @classmethod
    def isMinorType(cls, terrain):
        return not cls.isMajorType(terrain)


class Hex:
    def __init__(self, x: int, y: int, terrain):
        """ Are you surprised? """
        self.x = x
        self.y = y
        self.terrain = terrain

class HexMap:
    neighbors = [(),
                 (),
                 (),
                 (),
                 (),
                 ()]

    def __init__(self, sizex: int, sizey: int = None):
        if not sizey:
            sizey = sizex
        self.map = [[Hex(x, y, TerrainType.t_clr) for x in range(sizex)] for y in range(sizey)]
        self.sizex = sizex
        self.sizey = sizey

    def __str__(self):
        return f'<HexMap({self.sizex}, {self.sizey})>'