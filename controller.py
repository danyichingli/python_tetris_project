# Removes "Hello from the pygame community" message.
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame as pg
import sys
from constants import *

def move_left(grid, row, col):
    new_grid = grid
    new_grid[row][col] = 0
    new_grid[row][col-1] = 1
    return new_grid, row, col-1

def move_right(grid, row, col):
    new_grid = grid
    new_grid[row][col] = 0
    new_grid[row][col+1] = 1
    return new_grid, row, col+1

# Drop block down on top of bottom or another block (matrix).
def drop_block ():
    return

# Rotate block counter or clockwise. If it collides, then don't rotate.
def rotate_block ():
    return

# Check collision between blocks. This should signal game over if True.
def check_collision ():
    return
