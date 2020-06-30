import pygame as pg
import sys
import constants as c
from gameData import GameData

class Window:
    def __init__ (self):
        self.screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))
        self.is_running = True

    def draw (self, gd):
        for row in range(c.ROW_COUNT):
            for col in range(c.COLUMN_COUNT):
                color = self.color(gd.grid[row][col])
                rect = pg.Rect(c.GRID_BLOCK * col + c.GRID_BLOCK_MARGIN,
                               c.GRID_BLOCK * row + c.GRID_BLOCK_MARGIN,
                                c.GRID_BLOCK_SIZE, c.GRID_BLOCK_SIZE)
                pg.draw.rect(self.screen, color, rect)

    def pygame_init (self):
        pg.display.set_caption('Tetris')
        icon = pg.image.load('Images/icon.png')
        pg.display.set_icon(icon)

    def color (self, val):
        if val == -1:
            return c.WHITE
        elif val == 0:
            return c.GREY
        elif val == 1:
            return c.YELLOW
        elif val == 2:
            return c.CYAN
        elif val == 3:
            return c.ORANGE
        elif val == 4:
            return c.BLUE
        elif val == 5:
            return c.PURPLE
        elif val == 6:
            return c.GREEN
        else: # val == 7
            return c.RED
