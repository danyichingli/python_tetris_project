import pygame as pg
import constants as c
from View.modeView import ModeView

class ModeController:
    def __init__(self, gd):
        self.gd = gd
        self.mv = ModeView()
        self.signal = "mode"

    def mode_event_listener(self):
        while self.signal == "mode":
            pg.time.Clock().tick(c.FPS)
            self.mv.screen.fill(c.BLACK)
            tetris_pos, pentris_pos, back_pos = self.mv.draw_mode()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.signal = "quit"
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.signal = "quit"
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if back_pos.collidepoint(pg.mouse.get_pos()):
                        self.signal = "main_menu"
                    elif tetris_pos.collidepoint(pg.mouse.get_pos()):
                        self.signal = "tetris"
                        self.gd.set_signal("tetris")
                    elif pentris_pos.collidepoint(pg.mouse.get_pos()):
                        self.signal = "pentris"
                        self.gd.set_signal("pentris")
            pg.display.flip()
        return self.signal
