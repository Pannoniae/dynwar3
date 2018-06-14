import math

from game.hexmap import HexMap, Hex, TerrainType


class HexMapLayout:

    EDGE_COLOR = 0.8, 0.6, 0.6
    colors = {TerrainType.t_clr: (0.5, 0.3, 0.1),
              TerrainType.t_hll: (0.7, 0.2, 0.3)}

    def __init__(self, hexmap: HexMap, size = 20, offset = (0, 0)):
        self.size = size
        self.offset = offset

    def get_hex_position(self, hex: Hex):
        x = self.size * (3 / 2 * hex.x)
        y = self.size * (math.sqrt(3) / 2 * hex.x + math.sqrt(3) * hex.y)
        x += self.offset[0]
        y += self.offset[1]
        return x, y
        #pos1 = 0
        #x = self.size * 1.5
        #for i in range(hex.x):
        #    pos1 += x
        #pos2 = hex.y * (math.sqrt(3) * self.size)
        #for i in range(hex.x):
        #    pos2 += (math.sqrt(3) * self.size) / 2
        #pos1 += self.offset[0]
        #pos2 += self.offset[1]
        #return pos1, pos2
