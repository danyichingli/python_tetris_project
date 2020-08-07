from Controller.gameController import GameController

class Game:
    def run (self, gd):
        # Objects
        control = GameController(gd)
        # Game start
        control.game_loop()
        return control.signal
