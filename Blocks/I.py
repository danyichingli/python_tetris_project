import pygame as pg

class I_Block:
    def __init__ (self):
        self.shape  = [(0,3),(0,4),(0,5),(0,6)]
        self.color  = (0, 255, 255)
        self.val    = 2
        self.pos    = [(0,3),(0,4),(0,5),(0,6)]
