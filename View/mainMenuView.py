import pygame as pg
import constants as c
from View.baseView import BaseView
from .button import Button

class MainMenuView (BaseView):
    def draw_main_menu (self):
        main_menu = pg.Surface([c.WIDTH, c.HEIGHT])
        main_menu.fill(c.BLACK)
        self.screen.blit(main_menu,(0,0))
        # Tetris Title
        thisfont = pg.font.SysFont("Lucida Console", 70)
        tetris_text_width = thisfont.size("TETRIS")[0] / 2
        tetris_text_height = thisfont.size("TETRIS")[1] / 2
        self.draw_label(thisfont, "TETRIS", c.WIDTH/2 - tetris_text_width,
                                c.HEIGHT/4)
        # Start button
        start_game_button = Button(self.screen, "Start_Game","Start_Game_H")
        start_game_pos = start_game_button.button_center(self.screen, 0, 175)
        self.draw_button(self.screen, start_game_button.button,
                            start_game_button.button_h, start_game_pos)
        # Settings button
        settings_button = Button(self.screen, "Settings","Settings_H")
        settings_pos = settings_button.button_center(self.screen, 0, 250)
        self.draw_button(self.screen, settings_button.button, settings_button.button_h,
                        settings_pos)
        # Quit button
        quit_button = Button(self.screen, "Quit","Quit_H")
        quit_pos = quit_button.button_center(self.screen, 0, 325)
        self.draw_button(self.screen, quit_button.button, quit_button.button_h,
                        quit_pos)

        return start_game_pos, settings_pos, quit_pos
