import pygame as pg
import constants as c
from View.mainMenuView import MainMenuView

class MainMenuController:
    def __init__ (self):
        self.mmv = MainMenuView()
        self.signal = "main_menu"

    def main_menu_event_listener (self):
        while self.signal == "main_menu":
            pg.time.Clock().tick(c.FPS)
            start_game_pos, settings_pos, quit_pos = self.mmv.draw_main_menu()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.signal = "quit"
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.signal = "quit"
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if start_game_pos.collidepoint(pg.mouse.get_pos()):
                        self.signal = "game"
                    elif settings_pos.collidepoint(pg.mouse.get_pos()):
                        self.signal = "settings"
                    elif quit_pos.collidepoint(pg.mouse.get_pos()):
                        self.signal = "quit"
            pg.display.flip()
        return self.signal
