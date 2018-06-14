from game.hexmap import HexMap, Hex


class HexMapLayout:

    def __init__(self, hexmap: HexMap, offset = (0, 0)):
        self.offset = offset

    def get_hex_position(self, hex: Hex):
        pos1 = 0
        x = 30
        for i in range(hex.x):
            pos1 += x
        pos2 = hex.y * 20
        pos1 += self.offset[0]
        pos2 += self.offset[1]
        return pos1, pos2
