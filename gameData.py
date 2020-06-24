import pygame as pg
import random as rand
import sys
from block import Block
from controller import Controller
from constants import *

class GameData:
    def __init__ (self):
        self.curr_block = None
        self.next_block = None
        self.grid = []

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

    def block_generate (self):
        block_list = ['O', 'I', 'L', 'J', 'T', 'S', 'Z']
        # Current block
        if self.curr_block == None:
            self.curr_block = (Block(rand.choice(block_list)))
        else:
            self.curr_block = self.next_block
        # Next block
        self.next_block = (Block(rand.choice(block_list)))

    # Load block into game where the top-left part of block is placed at (0,4)
    def block_load (self):
        # Testing. Currently representing top-left placement for block.
        # TODO: Load full tetris blocks based on their shape
        #self.grid[0][4] = self.curr_block.val
        for i in self.curr_block.shape:
            self.grid[i[0]][i[1]] = self.curr_block.val

    # Block will move left, move right, drop, or rotate
    def block_move (self):
        control = Controller(self.grid, self.curr_block)
        self.grid = control.movement()

    def grid_generate (self):
        # Create board of 0's with the same shape as the grid.
        grid = [[0 for column in range(COLUMN_COUNT)] for row in range(ROW_COUNT)]
        # Bottom border for collision check.
        grid += [[1 for column in range(COLUMN_COUNT)]]
        self.grid = grid
