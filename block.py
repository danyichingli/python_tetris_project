import pygame as pg
import sys
from constants import *

class Block:

    def __init__ (self, template):
        self.template = template            # 'O', 'I', 'L', 'J', 'T', 'S', 'Z'
        self.shape = templates[template][0] # Shape
        self.color = templates[template][1] # Color asssociated with shape
        self.val = templates[template][2]   # Value on grid to identify color
        self.row = 0
        self.col = 4

    def get_color(self):
        return self.color

    def get_row (self):
        return self.row

    def set_row (self, row):
        self.row = row

    def get_col (self):
        return self.col

    def set_col (self, col):
        self.col = col
