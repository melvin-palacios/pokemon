import pygame as pg
import sys
import time
from game import Game

class Start:

    def __init__(self):
        pg.init()
        pg.display.set_caption('Pokemon')
        self.BG = (140, 140, 140)
        self.H = 800
        self.W = 1500
        self.screen = pg.display.set_mode((self.W, self.H))
        self.clock = pg.time.Clock()
        self.running = True
        self.font = pg.font.Font("font/font.ttf", 44)
        self.icon = pg.image.load('img/icon.png')
        pg.display.set_icon(self.icon)
        self.fade_surface = pg.Surface((self.W, self.H))
        self.fade_surface.set_alpha(0)  # Définition de l'opacité initiale
        self.fade_surface.fill((0, 0, 0, 10))
        # img
        self.chatbox = pg.image.load('img/chatbox.png')
        self.chatbox = pg.transform.scale(self.chatbox, (self.H // 3 * 3.234, self.H // 3))
        self.chatbox_bg = pg.surface.Surface((self.H // 3 * 3.234 - 17, self.H // 3- 14))
        self.chatbox_bg.fill((255, 255, 255))

        self.salameche_img = pg.image.load('img/pokemon/sala_front_1.png')
        self.salameche_img = pg.transform.scale(self.salameche_img, (self.H // 4, self.H // 4))
        self.salameche_rect = self.salameche_img.get_rect()
        self.salameche_rect.x = self.W // 2 - 100
        self.salameche_rect.y = self.H // 2 - 150

        self.carapuce_img = pg.image.load('img/pokemon/cara_front_1.png')
        self.carapuce_img = pg.transform.scale(self.carapuce_img, (self.H // 4, self.H // 4))
        self.carapuce_rect = self.carapuce_img.get_rect()
        self.carapuce_rect.x = self.W // 2 - 400
        self.carapuce_rect.y = self.H // 2 - 150

        self.bulbizarre_img = pg.image.load('img/pokemon/bulbi_front_1.png')
        self.bulbizarre_img = pg.transform.scale(self.bulbizarre_img, (self.H // 4, self.H // 4))
        self.bulbizarre_rect = self.bulbizarre_img.get_rect()
        self.bulbizarre_rect.x = self.W // 2 + 200
        self.bulbizarre_rect.y = self.H // 2 - 150

        # decor

        self.decor = pg.image.load('img/decor/bg_labo.png')
        self.decor = pg.transform.scale(self.decor, (self.W, self.H + 100))
        self.chen_img = pg.image.load('img/decor/chen_front.png')
        self.chen_img = pg.transform.scale(self.chen_img, (200, 300))

        self.shadow = pg.image.load('img/decor/shadow.png')
        self.shadow = pg.transform.scale(self.shadow, (687//2,179//2))
        self.check()

    def check (self):
        pass

    def update(self):
        pass

    def draw(self):
        self.screen.fill(self.BG)
        self.screen.blit(self.decor, (0, 0))
        self.screen.blit(self.chatbox_bg, (self.W // 3 - 170, self.H // 2 + 107))
        self.screen.blit(self.chatbox, (self.W // 3 - 170 - 10, self.H // 2 + 100))
        self.screen.blit(self.font.render("Choose a pokemon", True, (0, 0, 0)), (self.W // 3 - 160 + 20, self.H // 2 + 100 + 50))
        self.screen.blit(self.font.render("to start!", True, (0, 0, 0)), (self.W // 3 - 160 + 20, self.H // 2 + 100 + 130))
        self.screen.blit(self.chen_img, (self.W // 2 + 100, 40))
        self.screen.blit(self.shadow, (self.salameche_rect.x - 90, self.salameche_rect.y + 155))
        self.screen.blit(self.salameche_img, self.salameche_rect)
        self.screen.blit(self.shadow, (self.carapuce_rect.x - 90, self.carapuce_rect.y + 155))
        self.screen.blit(self.carapuce_img, self.carapuce_rect)
        self.screen.blit(self.shadow, (self.bulbizarre_rect.x - 70, self.bulbizarre_rect.y + 155))
        self.screen.blit(self.bulbizarre_img, self.bulbizarre_rect)
        pg.display.flip()

    def start(self, pokemon):
        i = 0
        while i < 255:
            self.fade_surface.set_alpha(i)
            self.screen.blit(self.fade_surface, (0, 0))
            i += 5
            pg.display.update()
            time.sleep(0.014)
        self.running = False
        start = Game(pokemon)
        start.run()
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
                    if self.salameche_rect.collidepoint(event.pos):
                        self.start("Salameche")
                    if self.carapuce_rect.collidepoint(event.pos):
                        self.start("Carapuce")
                    if self.bulbizarre_rect.collidepoint(event.pos):
                        self.start("Bulbizarre")
