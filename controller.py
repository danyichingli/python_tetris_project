# Removes "Hello from the pygame community" message.
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame as pg
import sys
from keyboardListener import KeyboardListener
from constants import *

class Controller:
    def __init__ (self, grid, row, col):
        self.grid = grid
        self.row = row
        self.col = col

    # Left movement
    def move_left(self):
        new_grid = self.grid
        new_grid[self.row][self.col] = 0
        new_grid[self.row][self.col-1] = 1
        return new_grid, self.row, self.col-1
    # Right movement
    def move_right(self):
        new_grid = self.grid
        new_grid[self.row][self.col] = 0
        new_grid[self.row][self.col+1] = 1
        return new_grid, self.row, self.col+1

    # Drop block down on top of bottom or another block (matrix).
    def drop_block (self):
        new_grid = grid
        new_grid[self.row-1][self.col] = 1
        return new_grid, 0, 4

    # L/R movement. Detects collision with walls.
    def movement (self):
        kl = KeyboardListener()
        if kl.listener() == "left" and self.col > 0:
            return self.move_left()
        if kl.listener() == "right" and self.col < 9:
            return self.move_right()
        return self.grid, self.row, self.col

    # Rotate block counter or clockwise. If it collides, then don't rotate.
    def rotate_block ():
        return

    # Check collision between blocks. This should signal game over if True.
    def check_collision (self):
        if self.col < 9 or self.col > 0:
            return False
        return True
