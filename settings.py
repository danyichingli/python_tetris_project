from Controller.settingsController import SettingsController

class Settings:
    def run (self, sd):
        # Objects
        control = SettingsController(sd)
        # Game start
        control.settings_event_listener()
        return control.signal
