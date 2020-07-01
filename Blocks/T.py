import pygame as pg

class T_Block:
    def __init__ (self):
        self.shape  = [(0,4),(1,3),(1,4),(1,5)]
        self.color  = (128, 0, 128)
        self.val    = 5
        self.pos    = [(0,4),(1,3),(1,4),(1,5)]
