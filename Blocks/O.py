import pygame as pg

class O_Block:
    def __init__ (self):
        self.shape  = [(0,4),(0,5),(1,4),(1,5)]
        self.color  = (255, 255, 0)
        self.val    = 1
        self.pos    = [(0,4),(0,5),(1,4),(1,5)]
