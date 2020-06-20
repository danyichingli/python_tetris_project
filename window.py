import pygame as pg
import sys
import gameData as gd
import keyboardListener as kl
from block import Block
from constants import *

def new_board (screen, columns, rows, grid):
    for column in range(columns):
        for row in range(rows):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            # rect = pg.Rect(column*blockSize, row*blockSize,
            #                 blockSize, blockSize)
            rect = pg.Rect((GRID_BLOCK_SIZE + GRID_BLOCK_MARGIN)
                                * column + GRID_BLOCK_MARGIN,
                           (GRID_BLOCK_SIZE + GRID_BLOCK_MARGIN)
                                * row + GRID_BLOCK_MARGIN,
                            GRID_BLOCK_SIZE,
                            GRID_BLOCK_SIZE)
            pg.draw.rect(screen, color, rect)

def new_grid ():
    # Create board of 0's with the same shape as the grid.
    grid = [[0 for column in range(COLUMN_COUNT)] for row in range(ROW_COUNT)]
    # Bottom border for collision check.
    grid += [[1 for column in range(COLUMN_COUNT)]]
    return grid

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
    # Window size based on grid
    grid_block = GRID_BLOCK_SIZE + GRID_BLOCK_MARGIN
    width = grid_block * COLUMN_COUNT + GRID_BLOCK_MARGIN
    height = grid_block * ROW_COUNT + GRID_BLOCK_MARGIN
    screen = pg.display.set_mode((width, height))
    block_queue = gd.block_queue([None, None])
    grid = new_grid()

    #testing
    grid = gd.block_load(grid)

    new_board(screen, COLUMN_COUNT, ROW_COUNT, grid)

    # Block queue
    curr_block = block_queue[0]
    next_block = block_queue[1]
    block = Block(curr_block)

    while not done:
        # Pygame loop speed
        clock.tick(FPS)

        screen.fill(BLACK)

        # Block movement, record position
        val = kl.listener(grid, block.x, block.y)
        block.set_x(val[1])
        block.set_y(val[2])
        new_board(screen, COLUMN_COUNT, ROW_COUNT, grid)

        # Events
        for event in pg.event.get():

            # Quit
            if event.type == pg.QUIT:
                done = True
        pg.display.flip()
    pg.quit()
main()
