from gameController import GameController

class Tetris:
    def run (self):
        # Objects
        control = GameController()
        # Game start
        control.game_loop()
