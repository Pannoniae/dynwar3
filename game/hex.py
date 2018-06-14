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

class Hex:
    def __init__(self, x: int, y: int, terrain):
        """ Are you surprised? """
        self.x = x
        self.y = y