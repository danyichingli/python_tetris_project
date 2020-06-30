import pygame as pg
import sys
import constants as c
from Blocks.O import O_Block
from Blocks.I import I_Block
from Blocks.L import L_Block
from Blocks.J import J_Block
from Blocks.T import T_Block
from Blocks.S import S_Block
from Blocks.Z import Z_Block

class Block:

    def __init__ (self, template):
        self.template = template
        self.shape = []             # Shape
        self.color = ()             # Color asssociated with shape
        self.val = 0                # Value on grid to identify color
        self.pos = []               # Position on grid
        self.dropped = False

    def get_color (self):
        return self.color

    def create_block (self):
        if self.template == 'O':
            block = O_Block()
            self.shape = block.shape
            self.color = block.color
            self.val = block.val
            self.pos = block.pos
        elif self.template == 'I':
            block = I_Block()
            self.shape = block.shape
            self.color = block.color
            self.val = block.val
            self.pos = block.pos
        elif self.template == 'L':
            block = L_Block()
            self.shape = block.shape
            self.color = block.color
            self.val = block.val
            self.pos = block.pos
        elif self.template == 'J':
            block = J_Block()
            self.shape = block.shape
            self.color = block.color
            self.val = block.val
            self.pos = block.pos
        elif self.template == 'T':
            block = T_Block()
            self.shape = block.shape
            self.color = block.color
            self.val = block.val
            self.pos = block.pos
        elif self.template == 'S':
            block = S_Block()
            self.shape = block.shape
            self.color = block.color
            self.val = block.val
            self.pos = block.pos
        else: # self.template == 'Z'
            block = Z_Block()
            self.shape = block.shape
            self.color = block.color
            self.val = block.val
            self.pos = block.pos
