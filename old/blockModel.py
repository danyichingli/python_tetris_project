import pygame as pg
from blockController import BlockController
from constants import *

# Block class
class Block(pg.sprite.Sprite):
    def __init__ (self, block):
        super().__init__()
        self.movex = 0                              # X movement
        self.movey = 0                              # Y movement
        self.image = block                          # Sprite image for block
        self.frame = 0                              # Frame counter
        self.rect = self.image.get_rect()           # Get xy dimensions of image
        self.rect.center = (WIDTH / 2, HEIGHT / 2)  # FOR TESTING PURPOSES
        self.finish = False


    def update (self):
        # Get movement
        BlockController(self).control(20)
        # Drop (Down) movement
        # TODO: Change for condition for dropping on top of other blocks
        if self.rect.bottom == HEIGHT:
            self.finish = True

        # Left/Right movement
        # TODO: Rotate (Up) movement
        else:
            self.rect.x += self.movex
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0
            self.rect.y += self.movey
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT
        # Reset movement
        self.movex = self.movey = 0
