from ruamel.yaml import YAML

from game.hexmap import HexMap, Hex, TerrainType


class GameIO:
    pass

class Loader(GameIO):
    pass

class Saver(GameIO):
    pass

class SaveGameLoader(Loader):

    def __init__(self, game, file):
        self.game = game
        with open(file) as f:
            self.file = f.read()
        self.save = None

    def load_game(self):
        file = self.file
        yaml = YAML(typ = 'unsafe') # to get a proper dict
        self.save = yaml.load(file)
        self.parse_game()

    def parse_game(self):
        x, y = self.save['size']['x'], self.save['size']['y']
        self.game.hexmap = HexMap(x, y)
        for index, row in enumerate(self.save['terrain_map']):
            for index2, _hex in enumerate(list(row)):
                if _hex == 'c':
                    hex = Hex(index, index2, TerrainType.t_clr)
                if _hex == 'h':
                    hex = Hex(index, index2, TerrainType.t_hll)
                #else:
                #    raise ValueError
                self.game.hexmap.set_hex((index, index2), hex)

class SaveGameSaver(Saver):
    pass