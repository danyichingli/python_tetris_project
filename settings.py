from Controller.settingsController import SettingsController

class Settings:
    def run (self, sd, prev_signal):
        # Objects
        control = SettingsController(sd, prev_signal)
        # Game start
        control.settings_event_listener()
        return control.curr_signal
