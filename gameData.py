import pygame as pg
import random as rand
import constants as c
from block import Block

class GameD ata:
    def __init__ (self):
        self.curr_block = None
        self.next_block = None
        self.grid = []
        self.score = 0
        self.level = 0
        self.clock = pg.time.Clock()
        self.fall_time = 0
        self.fall_speed = 0.27

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
            self.set_curr_block(Block(rand.choice(block_list)).clone())
        else:
            self.set_curr_block(Block(self.next_block.template).clone())
        # Next block
        self.set_next_block(Block(rand.choice(block_list)).clone())
        # # ---TESTING---
        # self.set_curr_block(Block('O'))
        # self.set_curr_block(self.curr_block.clone())
        # self.set_next_block(Block('O'))
        # self.set_next_block(self.next_block.clone())

    def grid_generate (self):
        # Create a grid with color other than black.
        grid = [[c.GREY for column in range(c.COLUMN_COUNT)]
                    for row in range(c.ROW_COUNT)]
        self.set_grid(grid)
