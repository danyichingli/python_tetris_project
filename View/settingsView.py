import pygame as pg
import constants as c
from View.baseView import BaseView
from .button import Button

class SettingsView (BaseView):
    def draw_settings (self, sd):
        volume = str(int(sd.music_vol))
        settings = pg.Surface([c.WIDTH, c.HEIGHT])
        settings.fill(c.BLACK)
        self.screen.blit(settings,(0,0))
        # Settings Label
        thisfont = pg.font.SysFont("Lucida Console", 70)
        settings_text_width = thisfont.size("SETTINGS")[0] / 2
        settings_text_height = thisfont.size("SETTINGS")[1] / 2
        self.draw_label(thisfont, "SETTINGS", c.WIDTH/2 - settings_text_width,
                                c.HEIGHT/4)
        # Change music volume
        left_arrow_button = Button(self.screen, "Left_Arrow","Left_Arrow_H")
        left_arrow_pos = left_arrow_button.button_center(self.screen,
                                                        -75, 100)
        self.draw_button(self.screen, left_arrow_button.button,
                        left_arrow_button.button_h, left_arrow_pos)
        right_arrow_button = Button(self.screen, "Right_Arrow","Right_Arrow_H")
        right_arrow_pos = right_arrow_button.button_center(self.screen,
                                                        75, 100)
        self.draw_button(self.screen, right_arrow_button.button,
                        right_arrow_button.button_h, right_arrow_pos)
        # Music Volume Label
        thisfont = pg.font.SysFont("Lucida Console", 70)
        vol_text_width = thisfont.size(volume)[0] / 2
        self.draw_label(thisfont, volume, c.WIDTH/2 - vol_text_width,
                        left_arrow_button.rect.top)
        # Music Label
        vol_text_width = thisfont.size("Music")[0] / 2
        vol_text_height = thisfont.size("Music")[1] / 2
        self.draw_label(thisfont, "Music", c.WIDTH/2 - vol_text_width,
                        left_arrow_button.rect.top - vol_text_height * 2)
        # Back button
        back_button = Button(self.screen, "Back","Back_H")
        back_pos = back_button.button_center(self.screen, 0, 325)
        self.draw_button(self.screen, back_button.button, back_button.button_h,
                        back_pos)
        return back_pos, left_arrow_pos, right_arrow_pos
