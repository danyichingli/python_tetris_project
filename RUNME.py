import pygame as pg
from game import Game
from main import Main
#from pause import Pause
from Data.gameData import GameData
from Data.settingsData import SettingsData
from Controller.mainMenuController import MainMenuController

# Run from here
def main ():
    # Initialize Data
    gd = GameData()
    sd = None
    signal = "main_menu"
    # Initialize Objects
    main_menu = Main()
    game = Game()
    pause = None
    settings = None
    objects =   {"main_menu":   main_menu,
                 "game":        game,
                 "pause":       pause,
                 "settings":    settings}
    # Begin
    # TODO: Find a way to not make it run infinitely.
    while signal != "quit":
        if signal == "main_menu":
            signal = main_menu.run()
    pg.quit
main()
