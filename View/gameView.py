import pygame as pg
import sys
import constants as c
from View.baseView import BaseView
from square import Square

class GameView(BaseView):
    def draw_grid (self, gd):
        for row in range(c.ROW_COUNT):
            for col in range(c.COLUMN_COUNT):
                color = gd.grid[row][col].get_color()
                rect = pg.Rect(c.SQUARE * col + (c.SIDE_SCREEN/2) + c.SQUARE_MARGIN,
                               c.SQUARE * row + c.HEADER/2 + c.SQUARE_MARGIN,
                                c.SQUARE_SIZE, c.SQUARE_SIZE)
                pg.draw.rect(self.screen, color, rect)

    def draw_mini_grid (self, gd, block, xpos, ypos):
        mini_grid = [[Square(c.GREY, "EMPTY") for column in range(4)] for row in range(4)]
        if block != None:
            block_shape = block.shape
            for i in range(len(block_shape)):
                row = block_shape[i][0]
                col = block_shape[i][1]
                mini_grid[row][col] = Square(block.get_color(), "BLOCK")
        for row in range(4):
            for col in range(4):
                color = mini_grid[row][col].get_color()
                rect = pg.Rect(c.SQUARE * col + xpos + c.SQUARE_MARGIN,
                               c.SQUARE * row + ypos + c.SQUARE_MARGIN,
                                c.SQUARE_SIZE, c.SQUARE_SIZE)
                pg.draw.rect(self.screen, color, rect)

    def draw_tetris_UI (self, gd):
        tetris_font = pg.font.SysFont("Lucida Console", 28)
        # Hold
        self.draw_label(tetris_font, "HOLD", 65, 25)
        self.draw_mini_grid(gd, gd.get_hold_block(), 30, 60)
        # Next
        self.draw_label(tetris_font, "NEXT", 615, 25)
        self.draw_mini_grid(gd, gd.get_next_block(), 580, 60)
        # Level
        self.draw_label(tetris_font, "LEVEL", 604, 210)
        self.draw_label(tetris_font, str(gd.get_level()), 604, 245)
        # Score
        self.draw_label(tetris_font, "SCORE", 603, 325)
        self.draw_label(tetris_font, str(gd.get_score()).zfill(6), 603, 360)
        # Pause
        self.draw_label(tetris_font, "Press 'P'", 603, 440)
        self.draw_label(tetris_font, "to pause", 603, 475)

    def draw_game_over (self):
        return
