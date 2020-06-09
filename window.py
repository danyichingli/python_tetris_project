# Removes "Hello from the pygame community" message.
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame as pg
import sys

# Global Variables
FPS = 15
WIDTH = 480
HEIGHT = 640

# RGB
BLACK = (0, 0, 0)

# Window class
class Window:
    def __init__ (self, w, h):
        self.w = w
        self.h = h

    # Display window interface with window's width and height.
    def window_display (self):
        return pg.display.set_mode((self.w, self.h))

# Block class
class Block(pg.sprite.Sprite):
    def __init__ (self, block):
        super().__init__()
        self.movex = 0                              # X movement
        self.movey = 0                              # Y movement
        self.image = block                          # Sprite image for block
        self.frame = 0                              # Frame counter
        self.rect = self.image.get_rect()           # Get xy dimensions of image
        self.rect.center = (WIDTH / 2, HEIGHT / 2)  # FOR TESTING PURPOSES
        self.finish = False

    def control (self):
        keyval = pg.key.get_pressed()
        if keyval[pg.K_LEFT] or keyval[pg.K_a]:
            print("left")
            self.movex = -20
        if keyval[pg.K_RIGHT] or keyval[pg.K_d]:
            print("right")
            self.movex = 20
        if keyval[pg.K_UP] or keyval[pg.K_w]:
            # TODO: Change for rotation
            print("up")
            self.movey = -20
        if keyval[pg.K_DOWN] or keyval[pg.K_s]:
            print("down")
            self.movey = HEIGHT

    def update (self):
        # Get movement
        self.control()

        # Drop (Down) movement
        # TODO: Change for condition for dropping on top of other blocks
        if self.rect.bottom == HEIGHT:
            self.finish = True

        # Left/Right movement
        # TODO: Rotate (Up) movement
        else:
            print(self.rect.bottom, HEIGHT)
            self.rect.x += self.movex
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0
            self.rect.y += self.movey
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT
        # Reset movement
        self.movex = self.movey = 0

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
