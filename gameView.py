import pygame as pg
import sys
import constants as c
from gameData import GameData

class GameView:
    def __init__ (self):
        self.screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))

    def draw (self, gd):
        for row in range(c.ROW_COUNT):
            for col in range(c.COLUMN_COUNT):
                color = gd.grid[row][col]
                rect = pg.Rect(c.SQUARE * col + (c.SIDE_SCREEN/2) + c.SQUARE_MARGIN,
                               c.SQUARE * row + c.HEADER/2 + c.SQUARE_MARGIN,
                                c.SQUARE_SIZE, c.SQUARE_SIZE)
                pg.draw.rect(self.screen, color, rect)

    def draw_label (self, myfont, text, xpos, ypos):
        label = myfont.render(text, 1, c.WHITE)
        self.screen.blit(label, (xpos, ypos))


    def draw_mini_grid (self, gd, block, xpos, ypos):
        mini_grid = [[c.GREY for column in range(4)] for row in range(4)]
        if block != None:
            block_shape = block.shape
            for i in range(len(block_shape)):
                row = block_shape[i][0]
                col = block_shape[i][1]
                mini_grid[row][col] = block.get_color()
        for row in range(4):
            for col in range(4):
                color = mini_grid[row][col]
                rect = pg.Rect(c.SQUARE * col + xpos + c.SQUARE_MARGIN,
                               c.SQUARE * row + ypos + c.SQUARE_MARGIN,
                                c.SQUARE_SIZE, c.SQUARE_SIZE)
                pg.draw.rect(self.screen, color, rect)

    def draw_tetris_UI (self, gd):
        tetris_font = pg.font.Font("Font/modern-tetris.ttf", 20)
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

    def pause_screen (self):
        pause = pg.Surface([c.WIDTH, c.HEIGHT])
        pause.set_alpha(35)
        pause.fill((255,255,255))
        self.screen.blit(pause,(0,0))
        temp_height = 25
        help_font = pg.font.SysFont("Lucida Console", 35)
        instruction_font = pg.font.SysFont("Lucida Console", 20)
        self.draw_label(help_font, "HELP", 333, temp_height)
        for instruction in c.INSTRUCTIONS:
            temp_height += 45
            self.draw_label(instruction_font, instruction, 125, temp_height)
