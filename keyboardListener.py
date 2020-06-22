import pygame as pg
import random as rand
import sys
from constants import *

class KeyboardListener:
    def listener (self):
        keyval = pg.key.get_pressed()
        if keyval[pg.K_LEFT] or keyval[pg.K_a]:
            return "left"

        if keyval[pg.K_RIGHT] or keyval[pg.K_d]:
            return "right"

        if keyval[pg.K_DOWN] or keyval[pg.K_s]:
            return "up"

        if keyval[pg.K_DOWN] or keyval[pg.K_s]:
            return "down"
