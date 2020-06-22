import pygame as pg
import sys
from window import Window
from gameData import GameData
from constants import *

class Tetris:
    def run (self):
        # Objects
        window = Window()
        gd = GameData()
        # Blocks
        block_queue = gd.block_queue([None, None])
        curr_block = block_queue[0]
        next_block = block_queue[1]
        # Grid
        grid = window.new_grid()
        grid = gd.block_load(grid)

        while window.is_running:
            # Pygame loop speed
            pg.time.Clock().tick(FPS)
            window.screen.fill(BLACK)

            # Update block position on board
            val = gd.block_move(grid, curr_block.x, curr_block.y)
            new_grid = val[0]
            curr_block.set_x(val[1])
            curr_block.set_y(val[2])
            window.new_board(new_grid, curr_block.color)

            # Events
            for event in pg.event.get():

                # Quit
                if event.type == pg.QUIT:
                    window.is_running = False
            pg.display.flip()
        pg.quit()
