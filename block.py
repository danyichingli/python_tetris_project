import pygame as pg
import constants as c
from copy import deepcopy

class Block:

    def __init__ (self, template):
        # 'O', 'I', 'L', 'J', 'T', 'S', 'Z'
        self.template           = template
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

    def get_color (self):
        return self.color

    def get_rotation_states (self):
        return self.rotation_states

    def get_curr_state (self):
        return self.curr_state

    def set_curr_state (self, new_state):
        self.curr_state = new_state

    def clone (self):
        new_block = deepcopy(Block(self.template))
        return new_block
