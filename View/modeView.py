import pygame as pg
import constants as c
from View.baseView import BaseView
from .button import Button

class ModeView (BaseView):
    def draw_mode (self):
        mode = pg.Surface([c.WIDTH, c.HEIGHT])
        mode.fill(c.BLACK)
        self.screen.blit(mode,(0,0))
        tetris_button = Button(self.screen, "Tetris","Tetris_H")
        tetris_pos = tetris_button.button_center(self.screen, 0, 100)
        self.draw_button(self.screen, tetris_button.button, tetris_button.button_h,
                        tetris_pos)
        pentris_button = Button(self.screen, "Pentris","Pentris_H")
        pentris_pos = pentris_button.button_center(self.screen, 0, 200)
        self.draw_button(self.screen, pentris_button.button, pentris_button.button_h,
                        pentris_pos)
        back_button = Button(self.screen, "Back","Back_H")
        back_pos = back_button.button_center(self.screen, 0, 300)
        self.draw_button(self.screen, back_button.button, back_button.button_h,
                        back_pos)
        return tetris_pos, pentris_pos, back_pos
