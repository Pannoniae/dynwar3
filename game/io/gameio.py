from ruamel.yaml import YAML

from game.hexmap import HexMap, Hex, TerrainType
from game.unit import Infantry


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
                    hex = Hex(index2, index, TerrainType.t_clr)
                elif _hex == 'h':
                    hex = Hex(index2, index, TerrainType.t_hll)
                else:
                    raise ParseError('Illegal terrain type')
                self.game.hexmap.set_hex((index2, index), hex)

        for _unit in self.save['units']:
            if self.save['units'][_unit]['type'] == 'inf':
                _pos = eval(_unit)
                hex = self.game.hexmap.get_hex(_pos)
                unit = Infantry(self.game, hex)
                self.game.hexmap.set_unit(hex, unit)
            else:
                raise ParseError('Illegal unit type')

class SaveGameSaver(Saver):
    pass

class ParseError(Exception):
    pass