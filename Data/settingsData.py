import pygame as pg

class SettingsData:
    def __init__ (self, music_vol):
        self.music_vol = music_vol

    def get_music_vol (self):
        return self.music_vol

    def set_music_vol (self, vol):
        self.music_vol = vol
