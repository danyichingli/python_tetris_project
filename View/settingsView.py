import pygame as pg
import constants as c
from View.baseView import BaseView
from .button import Button

class SettingsView (BaseView):
    def draw_settings (self, sd):
        volume = sd.music_vol * 100
        settings = pg.Surface([c.WIDTH, c.HEIGHT])
        settings.fill(c.BLACK)
        self.screen.blit(settings,(0,0))

        # Change music volume
        self.draw_arrows (str(volume), 300)

    def draw_arrows (self, label, y_offset):
        left_button = Button(self.screen, "Left_Arrow","Left_Arrow_H")
        right_button = Button(self.screen, "Right_Arrow","Right_Arrow_H")
        left_button.button_center(self.screen, 300, y_offset)
        right_button.button_center(self.screen, 400, y_offset)
        thisfont = pg.font.SysFont("Lucida Console", 35)
        # Label
        self.draw_label(thisfont, label, 333, left_button.rect.centery)
        # Volume
        self.draw_label(thisfont, label, 333, left_button.rect.centery)
