import pygame as pg
import random as rand
import sys
import constants as c
from block import Block
from controller import Controller

class GameData:
    def __init__ (self):
        self.curr_block = None
        self.next_block = None
        self.grid = []
        self.score = 0
        self.level = 0

    def get_curr_block (self):
        return self.curr_block

    def set_curr_block (self, block):
        self.curr_block = block

    def get_next_block (self):
        return self.next_block

    def set_next_block (self, block):
        self.next_block = block

    def get_grid (self):
        return self.grid

    def set_grid (self, grid):
        self.grid = grid

    def get_score (self):
        return self.score

    def set_score (self, score):
        self.score += score

    def get_level (self):
        return self.level

    def set_level (self, level):
        self.level += level

    def block_generate (self):
        block_list = ['O', 'I', 'L', 'J', 'T', 'S', 'Z']
        # Current block
        if self.curr_block == None:
            self.set_curr_block(Block(rand.choice(block_list)))
            self.curr_block.create_block()
        else:
            self.set_curr_block(Block(self.next_block.template))
            self.curr_block.create_block()
        # Next block
        self.set_next_block(Block(rand.choice(block_list)))
        self.next_block.create_block()
        # # ---TESTING---
        # self.set_curr_block(Block('O'))
        # self.curr_block.create_block()
        # self.set_next_block(Block('O'))
        # self.next_block.create_block()

    # Load block into game where the top-left part of block is placed at (0,4)
    def block_load (self):
        self.block_generate()

        # Check if we can still load block without overlapping
        for pos in self.curr_block.shape:
            row = pos[0]
            col = pos[1]
            if self.block_overlap(row, col):
                pg.quit()
                break
            self.grid[row][col] = self.curr_block.val

    # If the block can't be loaded without overlapping a block, then game over.
    def block_overlap (self, row, col):
        if self.grid[row][col] > 0:
            print("Game Over!")
            return True
        return False

    def grid_generate (self):
        # Create board of 0's with the same shape as the grid.
        grid = [[0 for column in range(c.COLUMN_COUNT)]
                    for row in range(c.ROW_COUNT)]
        self.set_grid(grid)

    # Check if row(s) on grid is filled up.
    def check_line_clear (self):
        clear_counter = 0
        for i, row in enumerate(self.grid):
            if all(val != 0 for val in row):
                self.grid[i] = [-1] * 10
                # TODO: Make it flash white before it disappears
                self.remove_line(i)
                clear_counter += 1
                print(clear_counter)
        self.scoring(clear_counter)

    def remove_line (self, row_index):
        del self.grid[row_index]
        self.grid.insert(0, [0] * c.COLUMN_COUNT)

    # Scoring based on original Nintendo scoring system
    def scoring (self, lines):
        n = self.get_level()
        if lines == 1:
            self.set_score(40 * (n + 1))
        elif lines == 2:
            self.set_score(100 * (n + 1))
        elif lines == 3:
            self.set_score(300 * (n + 1))
        elif lines == 4:
            self.set_score(1200 * (n + 1))

    # Block will move left, move right, drop, or rotate
    def get_events (self):
        control = Controller(self.grid, self.curr_block)
        self.set_grid(control.event_listener())
        if self.curr_block.dropped:
            self.check_line_clear()
            self.block_load()
