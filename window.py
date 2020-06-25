import pygame as pg
import sys
from gameData import GameData
from constants import *

class Window:
    def __init__ (self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.is_running = True

    def draw (self, gd):
        for col in range(COLUMN_COUNT):
            for row in range(ROW_COUNT):
                color = GREY
                if gd.grid[row][col] > 0:
                    color = self.color(gd.grid[row][col])
                rect = pg.Rect(GRID_BLOCK * col + GRID_BLOCK_MARGIN,
                               GRID_BLOCK * row + GRID_BLOCK_MARGIN,
                                GRID_BLOCK_SIZE, GRID_BLOCK_SIZE)
                pg.draw.rect(self.screen, color, rect)

    def color (self, val):
        if val == 1:
            return YELLOW
        elif val == 2:
            return CYAN
        elif val == 3:
            return ORANGE
        elif val == 4:
            return BLUE
        elif val == 5:
            return PURPLE
        elif val == 6:
            return GREEN
        else:
            return RED
