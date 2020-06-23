# Removes "Hello from the pygame community" message.
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame as pg
import sys
from keyboardListener import KeyboardListener
from constants import *

class Controller:
    def __init__ (self, grid, block):
        self.grid = grid
        self.block = block

    # Left movement
    def move_left(self):
        new_grid = self.grid
        new_grid[self.block.row][self.block.col] = 0
        new_grid[self.block.row][self.block.col-1] = self.block.val
        return new_grid, self.block.row, self.block.col-1
    # Right movement
    def move_right(self):
        new_grid = self.grid
        new_grid[self.block.row][self.block.col] = 0
        new_grid[self.block.row][self.block.col+1] = self.block.val
        return new_grid, self.block.row, self.block.col+1

    # TODO: Drop
    def drop_block (self):
        new_grid = grid
        new_grid[self.block.row-1][self.block.col] = 1
        return new_grid, 0, 4

    # TODO: Rotate
    # Rotate block counter or clockwise. If it collides, then don't rotate.
    def rotate_block ():
        return

    # L/R movement: detects collision with walls.
    # Drop: ???
    # Rotation: ???
    def movement (self):
        kl = KeyboardListener()
        if kl.listener() == "left" and self.block.col > 0:
            return self.move_left()
        if kl.listener() == "right" and self.block.col < 9:
            return self.move_right()
        return self.grid, self.block.row, self.block.col

    # Check collision between blocks. This should signal game over if True.
    def check_collision (self):
        if self.block.col < 9 or self.block.col > 0:
            return False
        return True
