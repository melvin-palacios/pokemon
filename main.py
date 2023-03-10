import sys
import pygame as pg
from menu import Menu


class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Pokemon')
        self.BG = (255, 255, 255)
        self.H = 800
        self.W = 1500
        self.bg_menu = pg.image.load('img/bg_pokemon.png')
        self.pokemon = pg.image.load('img/pokemon.png')
        self.icon = pg.image.load('img/icon.png')
        pg.display.set_icon(self.icon)
        self.bg_menu = pg.transform.scale(self.bg_menu, (self.W, self.H))
        self.screen = pg.display.set_mode((self.W, self.H))
        self.clock = pg.time.Clock()
        self.running = True
        self.font = pg.font.Font("font/font.ttf", 44)
        self.fadeout = pg.Surface((self.W, self.H))
        self.fadeout = self.fadeout.convert()
        self.fadeout.fill((0, 0, 0))
        self.font_color = (90, 90, 90)

    def update(self):
        pg.display.update()

    def draw(self):
        self.screen.blit(self.bg_menu, (0, 0))
        self.screen.blit(self.pokemon, (self.W // 2 - 540, 20))
        self.screen.blit(self.font.render("Click anywhere to start", True, self.font_color), (self.W // 5 - 40, self.H // 2 + 150))

    def fade(self):
        for i in range(255):
            self.fadeout.set_alpha(i)
            self.screen.blit(self.fadeout, (0, 0))
            pg.display.update()
            pg.time.delay(3)
    def run(self):
        while self.running:
            self.draw()
            self.update()
            self.clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    self.running = False
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.fade()
                    self.running = False
                    menu = Menu()
                    menu.run()

if __name__ == '__main__':
    app = App()
    app.run()