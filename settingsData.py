import pygame as pg

class SettingsData:
    def __init__ (self):
        self.sounds_vol = 1
        self.music_vol = 1

    def get_sounds_vol (self):
        return self.sounds_vol

    def set_sounds_vol (self, vol):
        self.sounds_vol = vol

    def get_music_vol (self):
        return self.music_vol

    def set_music_vol (self, vol):
        self.music_vol = vol
        
