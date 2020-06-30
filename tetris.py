import pygame as pg
import sys
import constants as c
from window import Window
from gameData import GameData

class Tetris:
    def run (self):
        # Objects
        window = Window()
        gd = GameData()
        # Pygame
        window.pygame_init()
        # Grid
        gd.grid_generate()
        # Blocks
        gd.block_load()

        while window.is_running:
            # Pygame loop speed
            pg.time.Clock().tick(c.FPS)
            window.screen.fill(c.BLACK)

            # Update
            gd.get_events()

            # Draw
            window.draw(gd)
            pg.display.flip()
        pg.quit()
