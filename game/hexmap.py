class Hex:
    def __init__(self, x: int, y: int):
        """ Are you surprised? """
        self.x = x
        self.y = y

class HexMap:
    def __init__(self, sizex: int, sizey: int = None):
        self.map = #todo
        for x in range(sizex):
            for y in range(sizey):
                self.map[x][y] = Hex(x, y)