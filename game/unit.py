from game.widget import GameObject


class Unit(GameObject):
    def __init__(self, game, hex):
        super().__init__(game)
        self.game = game
        self.hex = hex

    def move(self, direction):
        self.game.hm.move_unit(self, direction)
        self.reload()

class Infantry(Unit):
    pass