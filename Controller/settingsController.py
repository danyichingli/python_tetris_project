import pygame as pg
from Data.settingsData import SettingsData
from View.settingsView import SettingsView

class SettingsController:
    def __init__ (self, sd, prev_signal):
        self.sd = sd # SettingsData object
        self.curr_signal = "settings"
        self.prev_signal = prev_signal
        self.sv = SettingsView()

    # TODO
    def settings_event_listener (self):
        while self.curr_signal == "settings":
            back_pos, left_arrow_pos, right_arrow_pos = self.sv.draw_settings(self.sd)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.curr_signal = "quit"
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.curr_signal = "quit"
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if back_pos.collidepoint(pg.mouse.get_pos()):
                        self.curr_signal = self.prev_signal
                    elif right_arrow_pos.collidepoint(pg.mouse.get_pos()):
                        self.increase_music_volume()
                    elif left_arrow_pos.collidepoint(pg.mouse.get_pos()):
                        self.decrease_music_volume()
            pg.display.flip()
        return self.curr_signal

    def increase_music_volume (self):
        if self.sd.get_music_vol() < 1:
            self.music.set_volume(self.sd.get_music_vol() + 0.1)

    def decrease_music_volume (self):
        if self.sd.get_music_vol() > 0:
            self.music.set_volume(self.sd.get_music_vol() - 0.1)
