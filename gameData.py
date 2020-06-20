import pygame as pg
import random as rand
import sys
import block
from constants import *

def block_queue(old_queue):
    new_queue = [None, None]
    block_list = ['O', 'I', 'L', 'J', 'T', 'S', 'Z']
    # Current block
    if old_queue[0] == None:
        new_queue[0] = rand.choice(block_list)
    else:
        new_queue[0] = old_queue[1]
    # Next block
    new_queue[1] = rand.choice(block_list)
    return new_queue

def block_load(grid):
    new_grid = grid
    new_grid[0][4] = 1
    return new_grid
