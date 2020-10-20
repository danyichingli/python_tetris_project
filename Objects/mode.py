from Controller.modeController import ModeController

class Mode:
    def run (self, gd):
        # Objects
        control = ModeController(gd)
        # Game start
        control.mode_event_listener()
        return control.signal
