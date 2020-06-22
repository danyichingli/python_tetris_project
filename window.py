import pygame as pg
import sys
from constants import *

class Window:
    def __init__ (self):
        # Grid properties
        self.gbs = GRID_BLOCK_SIZE
        self.gbm = GRID_BLOCK_MARGIN
        self.gb = self.gbs + self.gbm
        # Board properties
        self.cols = COLUMN_COUNT
        self.rows = ROW_COUNT
        # Pygame window dimensions
        self.width = self.gb * self.cols + self.gbm
        self.height = self.gb * self.rows + self.gbm
        # Pygame window properties
        self.screen = pg.display.set_mode((self.width, self.height))
        self.is_running = True

    def new_board (self, grid, block_color):
        for column in range(self.cols):
            for row in range(self.rows):
                color = WHITE
                if grid[row][column] == 1:
                    color = block_color
                rect = pg.Rect(self.gb * column + self.gbm,
                               self.gb * row + self.gbm,
                                self.gbs, self.gbs)
                pg.draw.rect(self.screen, color, rect)

    def new_grid (self):
        # Create board of 0's with the same shape as the grid.
        grid = [[0 for column in range(self.cols)] for row in range(self.rows)]
        # Bottom border for collision check.
        grid += [[1 for column in range(self.cols)]]
        return grid

    # Remove row from grid if filled. Move everything above row down by 1 row.
    def remove_row (self):
        return
