import math

from game.hexmap import HexMap, Hex


class HexMapLayout:

    def __init__(self, hexmap: HexMap, size = 20, offset = (0, 0)):
        self.size = size
        self.offset = offset

    def get_hex_position(self, hex: Hex):
        pos1 = 0
        x = self.size * 1.5
        for i in range(hex.x):
            pos1 += x
        pos2 = hex.y * (math.sqrt(3) * self.size)
        for i in range(hex.x):
            pos2 += (math.sqrt(3) * self.size) / 2
        pos1 += self.offset[0]
        pos2 += self.offset[1]
        return pos1, pos2
