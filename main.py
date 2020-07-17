from game import Game
#from pause import Pause
from Data.gameData import GameData
from Data.settingsData import SettingsData

# Run from here
def main ():
    # Initialize Data
    gd = GameData()
    sd = None
    # Initialize Objects
    main_menu = None
    game = Game()
    pause = None
    settings = None
    objects =   {"main_menu":   main_menu,
                 "game":        game,
                 "pause":       pause,
                 "settings":    settings}
    # Current Active Object
    game.run(gd)
main()
