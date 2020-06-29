import pygame as pg
import sys
import constants as c

class Block:

    def __init__ (self, template):
        self.template = template            # 'O', 'I', 'L', 'J', 'T', 'S', 'Z'
        self.shape = c.templates[template][0] # Shape
        self.color = c.templates[template][1] # Color asssociated with shape
        self.val = c.templates[template][2]   # Value on grid to identify color
        self.pos = self.shape
        self.dropped = False

    def get_color(self):
        return self.color

    def get_pos (self):
        return self.pos

    def set_pos (self, pos):
        self.pos = pos

    def get_col (self):
        return self.col

    def set_col (self, col):
        self.col = col
