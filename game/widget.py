from typing import Tuple

from pygame.rect import Rect

class Widget:

    def __init__(self, box: Rect, parent = None):
        self.parent = parent
        self.box: Rect = box
        self.active = False

    def is_in_box(self, pos: Tuple[int, int]):
        return self.box.collidepoint(*pos)

    def handle(self, pos):
        if not self.active and self.is_in_box(pos):
            self.on_enter()
        if self.active and not self.is_in_box(pos):
            self.on_exit()

    def on_enter(self):
        self.active = True
        print('entered')

    def on_exit(self):
        self.active = False
        print('exited')