import pygame as pg
import constants as c

class BaseView:
    def __init__ (self):
        self.screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))

    def draw_label (self, myfont, text, xpos, ypos):
        label = myfont.render(text, 1, c.WHITE)
        self.screen.blit(label, (xpos, ypos))

    def draw_button (self, screen, button, button_h, button_pos):
        screen.blit(button, button_pos)
        if button_pos.collidepoint(pg.mouse.get_pos()):
            screen.blit(button_h, button_pos)
