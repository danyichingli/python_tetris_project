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
        # Erase the block's current position, fill in new position to left
        new_grid = self.grid
        for i in range(4):
            row = self.block.pos[i][0]
            col = self.block.pos[i][1]
            self.block.pos[i] = (row, col-1)
            new_grid[row][col] = 0
            new_grid[row][col-1] = self.block.val
        return new_grid
    # Right movement
    def move_right(self):
        # Erase the block's current position, fill in new position to right
        # ***If I used range(4), I'd be erasing the left side of the block in
        # its new position.
        new_grid = self.grid
        for i in range(3,-1,-1):
            row = self.block.pos[i][0]
            col = self.block.pos[i][1]
            self.block.pos[i] = (row, col+1)
            new_grid[row][col] = 0
            new_grid[row][col+1] = self.block.val
        return new_grid

    # TODO: Drop
    def drop_block (self):
        new_grid = self.grid
        curr_pos = self.block.pos
        next_pos = curr_pos
        hit = False
        while True:
            # Check for hit
            hit = self.block_collision()
            if hit:
                for i in range(4):
                    row = curr_pos[i][0]
                    col = curr_pos[i][1]
                    new_grid[row][col] = self.block.val
                break
            for i in range(4):
                curr_pos[i] = (row+1, col)
        return

    # TODO: Rotate
    # Rotate block counter or clockwise. If it collides, then don't rotate.
    def rotate_block ():
        return

    # L/R movement: detects collision with walls.
    # Drop: ???
    # Rotation: ???
    def movement (self):
        kl = KeyboardListener()
        if kl.listener() == "left" and self.wall_collision("left"):
            return self.move_left()
        if kl.listener() == "right" and self.wall_collision("right"):
            return self.move_right()
        if kl.listener() == "down":
            return self.drop_block()
        return self.grid

    # Check collision between blocks. This should signal game over if True.
    def wall_collision (self, side):
        if side == "left":
            leftmost = min(self.block.pos, key=lambda x:x[1])[1]
            if leftmost <= 0:
                return False
        else:
            rightmost = max(self.block.pos, key=lambda x:x[1])[1]
            if rightmost >= 9:
                return False
        return True

    def block_collision (self):
        temp_grid = self.grid
        for i in range(4):
            row = self.block.pos[i][0]
            col = self.block.pos[i][1]
            if temp_grid[row+1][col] > 0:
                return True
        return False
