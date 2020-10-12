import pygame as pg
from Objects.mainMenu import MainMenu
from Objects.game import Game
from Objects.pause import Pause
from Objects.settings import Settings
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
    pg.mixer.music.set_volume(1)

# Execute game from here
def execute ():
    # Initialize Data
    gd = GameData()
    sd = SettingsData(100)
    curr_signal = "pentris"
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
            pg.mixer.music.set_volume(sd.get_music_vol()  * 0.01)
            gd.new_game = True
            pg.mixer.music.stop()
            pg.mixer.music.rewind()
            curr_signal = main_menu.run()
            prev_signal = "main_menu"
        if curr_signal == "tetris" or curr_signal == "pentris":
            if prev_signal == "main_menu":
                pg.mixer.music.play(-1)

            gd.set_signal(curr_signal)

            curr_signal = game.run(gd)
        if curr_signal == "pause":
            curr_signal = pause.run(gd)
            prev_signal = "pause"
        if curr_signal == "settings":
            curr_signal = settings.run(sd, prev_signal)
    pg.quit()

execute()
