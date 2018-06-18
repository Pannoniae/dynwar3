from typing import Tuple

from pygame.rect import Rect


class Widget:

    def __init__(self, box: Rect, parent = None):
        self.parent = parent
        self.box = box

    def is_in_box(self, pos: Tuple[int, int]):
        return self.box.collidepoint(*pos)
