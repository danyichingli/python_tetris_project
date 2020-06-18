# Removes "Hello from the pygame community" message.
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame as pg
import sys
from constants import *

def new_grid (screen, columns, rows, blockSize):
    for column in range(columns):
        for row in range(rows):
            rect = pg.Rect(column*blockSize, row*blockSize,
                            blockSize, blockSize)
            pg.draw.rect(screen, WHITE, rect, 1)
def new_board ():
    # Create board of 0's with the same shape as the grid.
    board = [[0 for column in range(COLUMN_COUNT)] for row in range(ROW_COUNT)]
    # Bottom border for collision check.
    board += [[1 for column in range(COLUMN_COUNT)]]
    return board

# Check collision between blocks. This should signal game over if True.
def check_collision ():
    return

# Drop block down on top of bottom or another block (matrix).
def drop_block ():
    return

# Rotate block counter or clockwise. If it collides, then don't rotate.
def rotate_block ():
    return

# Move block left or right. Block should be bounded within grid.
def move_block ():
    return

# Remove row from grid if filled. Move everything above row down by 1 row.
def remove_row ():
    return

# Main
def main ():
    clock =  pg.time.Clock()
    done = False
    screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.fill(BLACK)
    new_grid(screen, COLUMN_COUNT, ROW_COUNT, 30)
    while not done:
        # Pygame loop speed
        clock.tick(FPS)

        new_grid(screen, COLUMN_COUNT, ROW_COUNT, 30)

        # Events
        for event in pg.event.get():

            # Quit
            if event.type == pg.QUIT:
                done = True


        pg.display.update()
    pg.quit()
main()
