import pygame as pg
from mainMenu import MainMenu
from game import Game
from pause import Pause
from settings import Settings
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
    curr_signal = "main_menu"
    prev_signal = ""
    # Initialize Objects
    main_menu = MainMenu()
    game = Game()
    pause = Pause()
    settings = Settings()
    game_init()
    # Begin
    while curr_signal != "quit":
        if curr_signal == "main_menu":
            # Reset if there was an instance of game
            gd.new_game = True
            pg.mixer.music.stop()
            pg.mixer.music.rewind()
            curr_signal = main_menu.run()
            prev_signal = "main_menu"
        if curr_signal == "game":
            pg.mixer.music.play(-1)
            curr_signal = game.run(gd)
        if curr_signal == "pause":
            curr_signal = pause.run(gd)
            prev_signal = "pause"
        if curr_signal == "settings":
            curr_signal = settings.run(sd, prev_signal)
    pg.quit()

execute()
