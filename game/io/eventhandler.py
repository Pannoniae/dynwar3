import logging
import sys

import pygame


class AbstractEventHandler:

    """ Generic EventHandler. Feel free to reuse! """

    def handle_events(self):
        for e in pygame.event.get():
            if e.type == pygame.ACTIVEEVENT:
                self.on_focus(e.gain, e.state)
            if e.type == pygame.KEYDOWN:
                self.on_key_press(e.unicode, e.key, e.mod)
            if e.type == pygame.QUIT:
                self.on_quit()
            if e.type == pygame.MOUSEMOTION:
                self.on_mouse_motion(e.pos, e.rel, e.buttons)

    def on_quit(self):
        pass

    def on_focus(self, gain, state):
        pass

    def on_key_press(self, unicode, key, mod):
        pass

    def on_key_release(self, key, mod):
        pass

    def on_mouse_motion(self, pos, rel, buttons):
        pass

    def on_mouse_release(self, pos, button):
        pass

    def on_mouse_press(self, pos, button):
        pass

    def on_resize(self, size, width, height):
        pass

    def on_video_expose(self):
        """ I do not understand this """
        pass

    def on_user_event(self, code):
        """ Handle it yourself! """
        logging.warning(f'UserEvent with code {code} not handled! This may be intentional, but normally this is a sign of error.')

class EventHandler(AbstractEventHandler):
    def __init__(self, game):
        self.game = game

    def on_quit(self):
        sys.exit()

    def on_key_press(self, unicode, key, mod):
        if key == pygame.K_LEFT:
            self.game.renderer.layout.offset[0] -= 10
            self.game.renderer.reload()
        if key == pygame.K_RIGHT:
            self.game.renderer.layout.offset[0] += 10
            self.game.renderer.reload()
        if key == pygame.K_UP:
            self.game.renderer.layout.offset[1] -= 10
            self.game.renderer.reload()
        if key == pygame.K_DOWN:
            self.game.renderer.layout.offset[1] += 10
            self.game.renderer.reload()

    def on_mouse_motion(self, pos, rel, buttons):
        for widget in self.game.widgets:
            widget.handle(pos)
