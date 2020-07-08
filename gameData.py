import pygame as pg
import constants as c
from block import Block

class GameData:
    def __init__ (self):
        self.curr_block = None
        self.next_block = None
        self.hold_block = None
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

    def get_hold_block (self):
        return self.hold_block

    def set_hold_block (self, block):
        self.hold_block = block

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

    def grid_generate (self):
        # Create a grid with color other than black.
        grid = [[c.GREY for column in range(c.COLUMN_COUNT)]
                    for row in range(c.ROW_COUNT)]
        self.set_grid(grid)
