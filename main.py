from Controller.mainMenuController import MainMenuController

class Main:
    def run (self):
        # Objects
        control = MainMenuController()
        # Game start
        return control.main_menu_event_listener()
