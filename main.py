import sys
import pygame as pg
import time
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
        self.fade_surface = pg.Surface((self.W, self.H))
        self.fade_surface.set_alpha(0)  # Définition de l'opacité initiale
        self.fade_surface.fill((0, 0, 0, 10))

    def update(self):
        pass

    def draw(self):
        self.screen.fill(self.BG)
        self.screen.blit(self.bg_menu, (0, 0))
        self.screen.blit(self.pokemon, (self.W // 2 - 540, 40))
        self.screen.blit(self.font.render("Click anywhere to start", True, (110, 110, 110)), (self.W // 5 - 40, self.H // 2 + 150))

        pg.display.flip()

    def run(self):
        while self.running:
            self.draw()
            self.clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    self.running = False
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    i = 0
                    while i < 255:
                        self.fade_surface.set_alpha(i)
                        self.screen.blit(self.fade_surface, (0, 0))
                        i += 5
                        pg.display.update()
                        time.sleep(0.014)
                    self.running = False
                    menu = Menu()
                    menu.run()

if __name__ == '__main__':
    app = App()
    app.run()