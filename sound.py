import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sounds/'
        self.sound = pg.mixer.Sound(self.path + '123.mp3')