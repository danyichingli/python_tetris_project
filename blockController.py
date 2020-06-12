import pygame as pg
from blockModel import Block

class BlockController:
    def __init__ (self, model, view):
        self.model = model
        self.view = view


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

    def update (self):
        # Get movement
        self.control(20)

        # Drop (Down) movement
        # TODO: Change for condition for dropping on top of other blocks
        if self.model.rect.bottom == HEIGHT:
            self.model.finish = True

        # Left/Right movement
        # TODO: Rotate (Up) movement
        else:
            self.model.rect.x += self.model.movex
            if self.model.rect.right > WIDTH:
                self.model.rect.right = WIDTH
            if self.model.rect.left < 0:
                self.model.rect.left = 0
            self.model.rect.y += self.model.movey
            if self.model.rect.bottom > HEIGHT:
                self.model.rect.bottom = HEIGHT
        # Reset movement
        self.model.movex = self.model.movey = 0
