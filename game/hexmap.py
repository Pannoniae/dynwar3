from game.hex import Hex


class HexMap:
    def __init__(self, sizex: int, sizey: int = None):
        if not sizey:
            sizey = sizex
        self.map = [[Hex(x, y) for x in range(sizex)] for y in range(sizey)]
        self.sizex = sizex
        self.sizey = sizey

    def __str__(self):
        return f'<HexMap({self.sizex}, {self.sizey})>'