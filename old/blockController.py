import pygame as pg
from constants import *

class BlockController:
    def __init__ (self, model):
        self.model = model


    def control (self, pixels):
        keyval = pg.key.get_pressed()
        if keyval[pg.K_LEFT] or keyval[pg.K_a]:
            print("left")
            self.model.movex = -pixels
        if keyval[pg.K_RIGHT] or keyval[pg.K_d]:
            print("right")
            self.model.movex = pixels
        if keyval[pg.K_UP] or keyval[pg.K_w]:
            # TODO: Change for rotation
            print("up")
            self.model.movey = -pixels
        if keyval[pg.K_DOWN] or keyval[pg.K_s]:
            print("down")
            self.model.movey = HEIGHT
