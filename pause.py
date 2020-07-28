from Controller.pauseController import PauseController

class Pause:
    def run (self, gd):
        # Objects
        control = PauseController(gd)
        # Game start
        control.pause_event_listener()
        return control.signal
