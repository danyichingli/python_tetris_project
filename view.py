# Removes "Hello from the pygame community" message.
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame as pg
import sys
from constants import *

def grid (screen):
    blockSize = 30 # Set the size of the grid block
    for x in range(10):
        for y in range(20):
            rect = pg.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            pg.draw.rect(screen, WHITE, rect, 1)

# Main
def main ():
    clock =  pg.time.Clock()
    done = False
    screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.fill(BLACK)
    while not done:
        # Pygame loop speed
        clock.tick(FPS)

        grid(screen)

        # Events
        for event in pg.event.get():

            # Quit
            if event.type == pg.QUIT:
                done = True


        pg.display.update()
    pg.quit()
main()
