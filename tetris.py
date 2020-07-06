from gameController import Controller

class Tetris:
    def run (self):
        # Objects
        control = Controller()
        # Game start
        control.game_loop()
