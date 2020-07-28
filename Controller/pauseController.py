import pygame as pg
import constants as c
from View.pauseView import PauseView

class PauseController:
    def __init__ (self, gd):
        self.gd = gd
        self.pv = PauseView()
        self.signal = "pause"

    def pause_event_listener (self):
        # TODO: Find a way to switch in and out of setttings
        while self.signal == "pause":
            pg.time.Clock().tick(c.FPS)
            self.pv.screen.fill(c.BLACK)
            settings_pos, quit_pos = self.pv.draw_pause()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.signal = "quit"
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_p:
                        self.signal = "game"
                    elif event.key == pg.K_ESCAPE:
                        self.signal = "quit"
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if settings_pos.collidepoint(pg.mouse.get_pos()):
                        self.signal = "settings"
                    elif quit_pos.collidepoint(pg.mouse.get_pos()):
                        self.signal = "quit"
            pg.display.flip()
        return self.signal
