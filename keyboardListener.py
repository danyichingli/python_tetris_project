import pygame as pg
import random as rand
import sys

class KeyboardListener:
    def listener (self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return "quit"
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    return "left"
                elif event.key == pg.K_RIGHT:
                    return "right"
                elif event.key == pg.K_DOWN:
                    return "down"
                elif event.key == pg.K_UP:
                    return "up"
                elif event.key == pg.K_ESCAPE:
                    return "quit"
        return ""
