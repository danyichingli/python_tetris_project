import pygame as pg
from Data.settingsData import SettingsData
from View.settingsView import SettingsView

class SettingsController:
    def __init__ (self, sd, sounds, music):
        self.sd = sd # SettingsData object
        self.sv = SettingsView()
        self.sounds = sounds
        self.music = music

    # TODO
    def settings_event_listener (self):
        while self.signal == "settings":
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

    def increase_music_volume (self):
        if self.sd.get_music_vol() < 1:
            self.music.set_volume(self.sd.get_music_vol() + 0.1)

    def decrease_music_volume (self):
        if self.sd.get_music_vol() > 0:
            self.music.set_volume(self.sd.get_music_vol() - 0.1)
