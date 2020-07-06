import pygame as pg
import constants as c
from copy import deepcopy

class Block:

    def __init__ (self, template):
        self.template   = template
        self.start_pos  = c.BLOCKS[self.template][0]
        self.color      = c.BLOCKS[self.template][1]
        self.curr_pos   = c.BLOCKS[self.template][0]
        self.dropped    = False

    def get_color (self):
        return self.color

    def clone (self):
        new_block = deepcopy(Block(self.template))
        return new_block
