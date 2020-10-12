import pygame as pg
import constants as c
from copy import deepcopy

class Block:

    def __init__ (self, template, type):
        self.type               = type
        self.template           = template
        self.shape              = c.SHAPES[self.template]
        # Positions on the grid
        self.start_pos          = c.BLOCKS[self.template][0]
        self.curr_pos           = c.BLOCKS[self.template][0]
        # Color based on the template of block
        self.color              = c.BLOCKS[self.template][1]
        # Values for rotation functionality
        self.rotation_states    = c.ROTATION[self.template]
        self.curr_state         = 0
        # If dropped, then use of this block is done
        self.dropped            = False
        self.num_squares        = len(c.BLOCKS[self.template][0])

    def get_type (self):
        return self.type

    def set_type (self, type):
        self.type = type

    def get_pos (self):
        return self.curr_pos

    def set_pos (self, pos):
        self.curr_pos = pos

    def get_color (self):
        return self.color

    def set_color (self, color):
        self.color = color

    def get_rotation_states (self):
        return self.rotation_states

    def get_curr_state (self):
        return self.curr_state

    def set_curr_state (self, new_state):
        self.curr_state = new_state

    def clone (self):
        new_block = deepcopy(Block(self.template, self.type))
        return new_block
