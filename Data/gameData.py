import pygame as pg
import constants as c
from BlockStuff.block import Block
from BlockStuff.square import Square

class GameData:
    def __init__ (self):
        self.new_game = True
        self.curr_block = None
        self.next_block = None
        self.hold_block = None
        self.ghost_block = None
        self.grid = []
        self.score = 0
        self.lines_cleared = 0
        self.level = 1
        self.clock = pg.time.Clock()
        self.fall_time = 0
        self.fall_delay = 1000
        self.fall_level = 5
        self.signal = ""

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

    def get_lines_cleared (self):
        return self.lines_cleared

    def set_lines_cleared (self, lines_cleared):
        self.lines_cleared = lines_cleared

    def get_level (self):
        return self.level

    def set_level (self, level):
        self.level = level

    def get_fall_time (self):
        return self.fall_time

    def set_fall_time (self, increment):
        self.fall_time = increment

    def get_fall_delay (self):
        return self.fall_delay

    def set_fall_delay (self, delay):
        self.fall_delay = delay

    def get_fall_level (self):
        return self.fall_level

    def set_fall_level (self, level):
        self.fall_level = level

    def get_signal (self):
        return self.signal

    def set_signal (self, signal):
        self.signal = signal

    def grid_generate (self):
        # Create a grid with color other than black.
        grid = [[Square(c.GREY, "EMPTY") for column in range(c.COLUMN_COUNT)]
                    for row in range(c.ROW_COUNT)]
        self.set_grid(grid)
