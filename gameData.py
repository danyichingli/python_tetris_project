import pygame as pg
import random as rand
import sys
from block import Block
from controller import Controller
from constants import *

class GameData:

    # Initialially 2 random blocks are chosen. After the current block has been
    # cemented, the next block becomes the current, and a randomly chosen block
    # becomes the next.
    def block_queue (self, old_queue):
        new_queue = [None, None]
        block_list = ['O', 'I', 'L', 'J', 'T', 'S', 'Z']
        # Current block
        if old_queue[0] == None:
            new_queue[0] = Block(rand.choice(block_list))
        else:
            new_queue[0] = old_queue[1]
        # Next block
        new_queue[1] = Block(rand.choice(block_list))
        return new_queue

    # Load block into game where the top-left part of block is placed at (0,4)
    def block_load (self, grid):
        new_grid = grid
        # Testing. Also representing top-left placement for block.
        new_grid[0][4] = 1
        return new_grid

    # Block will move left, move right, drop, or rotate
    def block_move (self, grid, row, col):
        control = Controller(grid, row, col)
        return control.movement()
