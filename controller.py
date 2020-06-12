# Removes "Hello from the pygame community" message.
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame as pg
import sys
from constants import *
from blockModel import Block
from blockController import BlockController
from window import Window

# Main
def main ():
    win = Window(WIDTH, HEIGHT)
    screen = win.window_display()
    image = pg.image.load(os.path.join('sprites', 'o-block.png')).convert_alpha()

    block = Block(image)
    blocks = pg.sprite.Group()
    blocks.add(block)

    clock =  pg.time.Clock()
    done = False

    while not done:
        # Pygame loop speed
        clock.tick(FPS)

        # Events
        for event in pg.event.get():

            # Quit
            if event.type == pg.QUIT:
                done = True

        # Update
        blocks.update()

        # Draw/Render
        screen.fill(BLACK)
        blocks.draw(screen)

        pg.display.flip()
    pg.quit()
main()
