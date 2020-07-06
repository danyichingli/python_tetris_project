import pygame as pg
import sys
import constants as c
from gameData import GameData

class Window:
    def __init__ (self):
        self.screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))

    def draw (self, gd):
        for row in range(c.ROW_COUNT):
            for col in range(c.COLUMN_COUNT):
                color = gd.grid[row][col]
                rect = pg.Rect(c.SQUARE * col + c.SQUARE_MARGIN,
                               c.SQUARE * row + c.SQUARE_MARGIN,
                                c.SQUARE_SIZE, c.SQUARE_SIZE)
                pg.draw.rect(self.screen, color, rect)

    def pygame_init (self):
        pg.display.set_caption('Tetris')
        icon = pg.image.load('Images/icon.png')
        pg.display.set_icon(icon)
