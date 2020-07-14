import pygame as pg
from settingsData import SettingsData
from settingsView import SettingsView

class SettingsController:
    def __init__ (self, sd, sounds, music):
        self.sd = sd # SettingsData object
        self.sv = SettingsView()
        self.sounds = sounds
        self.music = music

    def increase_sound_volume (self):
        if self.sd.get_sounds_vol() < 1:
            for sound in self.sounds:
                sound.set_volume(sound.get_volume() + 0.1)

    def decrease_sound_volume (self):
        if self.sd.get_sounds_vol() > 0:
            for sound in self.sounds:
                sound.set_volume(sound.get_volume() - 0.1)

    def increase_music_volume (self):
        if self.sd.get_music_vol() < 1:
            self.music.set_volume(self.sd.get_music_vol() + 0.1)

    def decrease_music_volume (self):
        if self.sd.get_music_vol() > 0:
            self.music.set_volume(self.sd.get_music_vol() - 0.1)
