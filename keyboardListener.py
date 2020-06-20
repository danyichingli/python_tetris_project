import pygame as pg
import random as rand
import sys
import controller as control
from constants import *

def listener (grid, row, col):
    keyval = pg.key.get_pressed()
    if keyval[pg.K_LEFT] or keyval[pg.K_a]:
        if col > 0:
            #print("left")
            return control.move_left(grid, row, col)
        else:
            #print("wall hit")
            return grid, row, col
    if keyval[pg.K_RIGHT] or keyval[pg.K_d]:
        if col < 9:
            #print("right")
            return control.move_right(grid, row, col)
        else:
            #print("wall hit")
            return grid, row, col
    # if keyval[pg.K_UP] or keyval[pg.K_w]:
    #     # TODO: Change for rotation
    #     print("up")
    #     self.model.movey = -pixels
    # if keyval[pg.K_DOWN] or keyval[pg.K_s]:
    #     print("down")
    #     self.model.movey = HEIGHT
    return grid, row, col
