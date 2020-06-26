import pygame as pg
import random as rand
import sys
from constants import *

class KeyboardListener:
    def listener (self):
        # keyval = pg.key.get_pressed()
        # if keyval[pg.K_LEFT] or keyval[pg.K_a]:
        #     return "left"
        #
        # if keyval[pg.K_RIGHT] or keyval[pg.K_d]:
        #     return "right"
        #
        # if keyval[pg.K_UP] or keyval[pg.K_w]:
        #     return "up"
        #
        # if keyval[pg.K_DOWN] or keyval[pg.K_s]:
        #     return "down"

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return "quit"
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    return "left"
                elif event.key == pg.K_RIGHT:
                    return "right"
                elif event.key == pg.K_DOWN:
                    return "down"
                elif event.key == pg.K_UP:
                    return "up"
        return ""
