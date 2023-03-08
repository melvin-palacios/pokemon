import pygame as pg
import time

class Game:

    def __init__(self, pokemon):
        self.pokemon = pokemon
        pg.init()
        pg.display.set_caption('Pokemon - game')
        self.BG = (81, 216, 60)
        self.H = 800
        self.W = 1500
