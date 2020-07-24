import pygame as pg
from mainMenu import MainMenu
from game import Game
from pause import Pause
#from pause import Pause
from Data.gameData import GameData
from Data.settingsData import SettingsData
from Controller.mainMenuController import MainMenuController

# Initialize Pygame stuff
def game_init ():
    pg.mixer.pre_init(44100)
    pg.init()
    pg.mixer.init(44100)
    # Display init
    pg.display.set_caption('Tetris')
    icon = pg.image.load('Images/icon.png')
    pg.display.set_icon(icon)
    # Text init
    pg.font.init()
    # Mixer init
    pg.mixer.music.load('Music/Tetris.mp3')
    pg.mixer.music.set_volume(0.1)

# Execute game from here
def execute ():
    # Initialize Data
    gd = GameData()
    sd = SettingsData()
    signal = "main_menu"
    # Initialize Objects
    main_menu = MainMenu()
    game = Game()
    pause = Pause()
    settings = None
    game_init()
    # Begin
    while signal != "quit":
        if signal == "main_menu":
            # Reset if there was an instance of game
            gd.new_game = True
            pg.mixer.music.stop()
            pg.mixer.music.rewind()
            signal = main_menu.run(sd)
        if signal == "game":
            pg.mixer.music.play(-1)
            signal = game.run(gd)
        if signal == "pause":
            signal = pause.run(gd, sd)
        # if signal == "settings":
        #     signal =
    pg.quit()

execute()
