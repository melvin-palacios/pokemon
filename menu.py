import pygame as pg
from start import Start
class Menu:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Pokemon - Menu')
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
        self.start_rect = pg.Rect(self.W // 2 - 100, self.H // 2, 200, 40)
        self.option_rect = pg.Rect(self.W // 2 - 120, self.H // 2 + 140, 240, 40)
        self.nouvelle_partie_rect = pg.Rect(self.W // 2 - 290, self.H // 2 + 70, 580, 40)
        self.exit_rect = pg.Rect(self.W // 2 - 80, self.H // 2 + 210, 160, 40)
        self.fadeout = pg.Surface((self.W, self.H))
        self.fadeout.fill((0, 0, 0))
        self.font_color = (90, 90, 90)
    def update(self):
        pg.display.flip()

    def draw(self):
        self.screen.blit(self.bg_menu, (0, 0))
        self.screen.blit(self.pokemon, (self.W // 2 - 540, 20))
        self.screen.blit(self.font.render("Start", True, self.font_color), (self.W // 2 - 100, self.H // 2))
        self.screen.blit(self.font.render("Nouvelle partie", True, self.font_color), (self.W // 2 - 290, self.H // 2 + 70))
        self.screen.blit(self.font.render("Option", True, self.font_color), (self.W // 2 -120, self.H // 2 + 140))
        self.screen.blit(self.font.render("Exit", True, self.font_color), (self.W // 2 - 80, self.H // 2 + 210))

    def fade_in(self):
        i = 255
        while i > 0:
            self.fadeout.set_alpha(i)
            self.screen.blit(self.fadeout, (0, 0))
            pg.display.update()
            i -= 5
            pg.time.delay(8)
            self.draw()

    def fade_out(self):
        i = 0
        while i < 255:
            self.fadeout.set_alpha(i)
            self.screen.blit(self.fadeout, (0, 0))
            pg.display.update()
            i += 5
            pg.time.delay(8)
    def run(self):
        self.fade_in()
        while self.running:
            self.draw()
            self.update()
            for event in pg.event.get():
                mouse = pg.mouse.get_pos()
                if event.type == pg.QUIT:
                    pg.quit()
                    self.running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.start_rect.collidepoint(mouse):
                        self.fade_out()
                        self.running = False
                        start = Start()
                        start.run()
                    if self.nouvelle_partie_rect.collidepoint(mouse):
                        print("Nouvelle partie")
                    if self.option_rect.collidepoint(mouse):
                        print("Option")
                    if self.exit_rect.collidepoint(mouse):
                        pg.quit()
                        self.running = False
            self.clock.tick(60)