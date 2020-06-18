# Removes "Hello from the pygame community" message.
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame as pg
import sys
from constants import *

class Block (object):

    def __init__ (self, template):
        self.template = template            # 'O', 'I', 'L', 'J', 'T', 'S', 'Z'
        self.shape = templates[template][0] # Shape
        self.color = templates[template][1] # Color asssociated with shape
