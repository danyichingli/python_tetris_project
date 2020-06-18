import pygame as pg

# Window class
class Window:
    def __init__ (self, w, h):
        self.w = w
        self.h = h

    # Display window interface with window's width and height.
    def window_display (self):
        return pg.display.set_mode((self.w, self.h))
