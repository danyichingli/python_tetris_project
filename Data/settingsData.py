import pygame as pg

class SettingsData:
    def __init__ (self):
        self.music_vol = .1

    def get_music_vol (self):
        return self.music_vol

    def set_music_vol (self, vol):
        self.music_vol = vol
