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
        gd.block_generate()
        # Grid
        gd.grid_generate()
        gd.block_load()

        while window.is_running:
            # Pygame loop speed
            pg.time.Clock().tick(FPS)
            window.screen.fill(BLACK)

            # Update
            if gd.curr_block.dropped:
                gd.block_generate()
                gd.block_load()
            gd.block_move()

            # Draw
            window.draw(gd)

            # Events
            for event in pg.event.get():

                # Quit
                if event.type == pg.QUIT:
                    window.is_running = False
            pg.display.flip()
        pg.quit()
