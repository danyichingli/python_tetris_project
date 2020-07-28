import pygame as pg
import constants as c
from View.baseView import BaseView
from .button import Button

class PauseView (BaseView):
    def draw_pause (self):
        pause = pg.Surface([c.WIDTH, c.HEIGHT])
        pause.fill(c.BLACK)
        self.screen.blit(pause,(0,0))
        self.draw_help()
        settings_button = Button(self.screen, "Settings","Settings_H")
        settings_pos = settings_button.button_center(self.screen, 0, 200)
        self.draw_button(self.screen, settings_button.button, settings_button.button_h,
                        settings_pos)
        quit_button = Button(self.screen, "Quit","Quit_H")
        quit_pos = quit_button.button_center(self.screen, 0, 300)
        self.draw_button(self.screen, quit_button.button, quit_button.button_h,
                        quit_pos)
        return settings_pos, quit_pos

    def draw_help (self):
        temp_height = 25
        help_font = pg.font.SysFont("Lucida Console", 35)
        instruction_font = pg.font.SysFont("Lucida Console", 20)
        self.draw_label(help_font, "HELP", 333, temp_height)
        for instruction in c.INSTRUCTIONS:
            temp_height += 45
            self.draw_label(instruction_font, instruction, 125, temp_height)
