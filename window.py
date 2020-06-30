import pygame as pg
import sys
from gameData import GameData
from constants import *

class Window:
    def __init__ (self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.is_running = True

    def draw (self, gd):
        for column in range(COLUMN_COUNT):
            for row in range(ROW_COUNT):
                color = GREY
                if gd.grid[row][column] > 0:
                    color = gd.curr_block.get_color()
                rect = pg.Rect(GRID_BLOCK * column + GRID_BLOCK_MARGIN,
                               GRID_BLOCK * row + GRID_BLOCK_MARGIN,
                                GRID_BLOCK_SIZE, GRID_BLOCK_SIZE)
                pg.draw.rect(self.screen, color, rect)
