import pygame as pg
import constants as c
from View.pauseView import PauseView
from Controller.settingsController import SettingsController

class PauseController:
    def __init__ (self, gd):
        self.gd = gd
        self.pv = PauseView()
        self.in_settings = False

    def pause_event_listener (self):
        # TODO: Find a way to switch in and out of setttings
        settings_pos, quit_pos = self.pv.draw_pause()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.gd.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    self.gd.paused = not self.gd.paused
                elif event.key == pg.K_ESCAPE:
                    self.gd.running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if settings_pos.collidepoint(pg.mouse.get_pos()):
                    self.in_settings = True
                elif quit_pos.collidepoint(pg.mouse.get_pos()):
                    self.gd.running = False
