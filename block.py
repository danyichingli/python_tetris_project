import pygame as pg
import sys
from constants import *

class Block:

    def __init__ (self, template):
        self.template = template            # 'O', 'I', 'L', 'J', 'T', 'S', 'Z'
        self.shape = templates[template][0] # Shape
        self.color = templates[template][1] # Color asssociated with shape
        self.x = 0
        self.y = 4

    def get_color(self):
        return self.color

    def get_x (self):
        return self.x

    def set_x (self, x):
        self.x = x

    def get_y (self):
        return self.y

    def set_y (self, y):
        self.y = y
