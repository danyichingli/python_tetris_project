import pygame as pg
import constants as c
from baseView import BaseView
from button import Button

class SettingsView (BaseView):
    def draw_settings (self):
        settings = pg.Surface([c.WIDTH, c.HEIGHT])
        settings.fill(c.BLACK)
        self.screen.blit(settings,(0,0))
