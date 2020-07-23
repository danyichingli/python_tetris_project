import pygame as pg
from main import Main
from game import Game
from pause import Pause
#from pause import Pause
from Data.gameData import GameData
from Data.settingsData import SettingsData
from Controller.mainMenuController import MainMenuController

# Initialize Pygame stuff
def game_init ():
    pg.mixer.pre_init(44100, -16,2,2048)
    pg.init()
    # Display init
    pg.display.set_caption('Tetris')
    icon = pg.image.load('Images/icon.png')
    pg.display.set_icon(icon)
    # Text init
    pg.font.init()
    # Mixer init
    pg.mixer.music.load('Music/Tetris.mp3')
    pg.mixer.music.set_volume(0.1)
    pg.mixer.music.play(-1)

# Execute game from here
def execute ():
    # Initialize Data
    gd = GameData()
    sd = None
    signal = "main_menu"
    # Initialize Objects
    main_menu = Main()
    game = Game()
    pause = Pause()
    settings = None
    objects =   {"main_menu":   main_menu,
                 "game":        game,
                 "pause":       pause,
                 "settings":    settings}
    game_init()
    # Begin
    # TODO: Find a way to not make it run infinitely.
    while signal != "quit":
        if signal == "main_menu":
            gd.new_game = True
            signal = main_menu.run()
        if signal == "game":
            signal = game.run(gd)
        if signal == "pause":
            signal = pause.run(gd)
    pg.quit()

execute()
