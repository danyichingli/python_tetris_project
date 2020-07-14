import pygame as pg
import constants as c
from pauseView import PauseView
from gameData import GameData

class PauseController:
    def __init__ (self, gd):
        self.gd = gd
        self.pv = PauseView()

    def pause_event_listener (self):
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
                    # select = pg.mixer.Sound("Sounds/Select.wav")
                    # select.set_volume(0.1)
                    # pg.mixer.Sound.play(select)
                    return
                elif quit_pos.collidepoint(pg.mouse.get_pos()):
                    self.gd.running = False
