from Controller.mainMenuController import MainMenuController

class MainMenu:
    def run (self):
        # Objects
        control = MainMenuController()
        # Game start
        control.main_menu_event_listener()
        return control.signal