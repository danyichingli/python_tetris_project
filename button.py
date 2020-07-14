import pygame as pg

class Button:
    def __init__ (self, screen, image, image_h):
        self.button = pg.image.load("Images/" + image + ".png").convert()
        self.button_h = pg.image.load("Images/" + image_h + ".png").convert()
        self.rect = self.button.get_rect(center = screen.get_rect().center)

    def button_center (self, screen, center_offset):
        self.rect.centery += center_offset
        return self.rect
