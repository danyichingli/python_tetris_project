# Removes "Hello from the pygame community" message.
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame as pg
import sys

# Global Variables
FPS = 30
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
        self.movex = 0                      # X movement
        self.movey = 0                      # Y movement
        self.image = block                  # Sprite image
        self.frame = 0                      # Frame counter
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def control (self, x, y):
        self.movex += x
        self.movey += y

    def update (self):
        # Left/Right movement
        self.rect.x += self.movex
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        # Up/Down movement
        self.rect.y += self.movey
        self.rect.y += 10
        print(self.rect.y)
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

        # Move left

# Main
win = Window(WIDTH, HEIGHT)
screen = win.window_display()
image = pg.image.load(os.path.join('sprites', 'o-block.png')).convert_alpha()
pg.display.flip()
block = Block(image)
blocks = pg.sprite.Group()
blocks.add(block)
clock =  pg.time.Clock()
running = True
while running:
    clock.tick(FPS)

    # Events
    for event in pg.event.get():

        # Quit
        if event.type == pg.QUIT:
            running = False

        # Movement (print statements for testing)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT or event.key == ord('a'):
                print('left')
            if event.key == pg.K_RIGHT or event.key == ord('d'):
                print('right')
            if event.key == pg.K_UP or event.key == ord('w'):
                print('up')
            if event.key == pg.K_DOWN or event.key == ord('s'):
                print('down')

        if event.type == pg.KEYUP:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
                running = False
    # Update
    blocks.update()

    # Draw/Render
    screen.fill(BLACK)
    blocks.draw(screen)

    pg.display.flip()
