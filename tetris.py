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
            gd.get_events()

            # Draw
            window.draw(gd)
            pg.display.flip()
        pg.quit()
