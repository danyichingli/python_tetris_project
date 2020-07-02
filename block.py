import pygame as pg
import constants as c
from copy import deepcopy

class Block:

    def __init__ (self, template):
        self.template   = template
        self.start_pos  = []
        self.color      = ()
        self.curr_pos   = []
        self.dropped    = False

    def get_color (self):
        return self.color

    def clone (self):
        self.start_pos  = deepcopy(c.BLOCKS[self.template][0])
        self.color      = deepcopy(c.BLOCKS[self.template][1])
        self.curr_pos   = self.start_pos
