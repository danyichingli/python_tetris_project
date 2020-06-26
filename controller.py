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
        # Leftmost column
        leftmost = min(self.block.pos, key=lambda x:x[1])[1]
        # Rightmost column
        rightmost = max(self.block.pos, key=lambda x:x[1])[1]
        # Closest part of block near the bottom for collision
        botmost = max(self.block.pos, key=lambda x:x[0])[0]
        # Closest row on grid near the bottom for collision
        topmost = 0
        # print("---TEST---")
        # print(self.block.pos)
        for i, row in enumerate(new_grid):
            if i == 19:
                topmost = i
            elif i >= botmost+1:
                row = row[leftmost:rightmost+1]
                if not all(j == 0 for j in row):
                    print(i,row)
                    topmost = i - 1
                    print(topmost,botmost)
                    break
        dist = self.drop_dist(botmost, topmost)
        for i in range(4):
            row = self.block.pos[i][0]
            col = self.block.pos[i][1]
            self.block.pos[i] = (row+dist, col)
            new_grid[row][col] = 0
            new_grid[row+dist][col] = self.block.val
        # print(self.block.pos)
        # print(botmost+1, topmost+1)
        return new_grid

    # TODO: Rotate
    # Rotate block counter or clockwise. If it collides, then don't rotate.
    def rotate_block ():
        return

    def event_listener (self):
        event = KeyboardListener().listener()
        if event == "quit":
            pg.quit()
        elif event == "left" and self.wall_collision("left"):
            return self.move_left()
        elif event == "right" and self.wall_collision("right"):
            return self.move_right()
        elif event == "down":
            self.block.dropped = True
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

    def drop_dist (self, row1, row2):
        # row1 = lowest row for block pos
        # row2 = highest row on grid that has a row filled in
        if row2 > 19:
            return 19 - row1

        return row2 - row1
