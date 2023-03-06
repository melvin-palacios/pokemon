import pygame as pg

class Menu:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Pokemon - Menu')
        self.BG = (81, 216, 60)
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
        self.start_rect = pg.Rect(self.W // 2 - 100, self.H // 2 + 60, 200, 40)
        self.option_rect = pg.Rect(self.W // 2 - 120, self.H // 2 + 130, 240, 40)
        self.exit_rect = pg.Rect(self.W // 2 - 80, self.H // 2 + 200, 160, 40)

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.bg_menu, (0, 0))
        self.screen.blit(self.pokemon, (self.W // 2 - 540, 40))
        self.screen.blit(self.font.render("Start", True, (110, 110, 110)), (self.W // 2 - 100, self.H // 2 + 60))
        self.screen.blit(self.font.render("Option", True, (110, 110, 110)), (self.W // 2 -120, self.H // 2 + 130))
        self.screen.blit(self.font.render("Exit", True, (110, 110, 110)), (self.W // 2 - 80, self.H // 2 + 200))
        pg.display.flip()

    def run(self):
        while self.running:
            self.draw()
            for event in pg.event.get():
                mouse = pg.mouse.get_pos()
                if event.type == pg.QUIT:
                    pg.quit()
                    self.running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.start_rect.collidepoint(mouse):
                        print("Start")
                    if self.option_rect.collidepoint(mouse):
                        print("Option")
                    if self.exit_rect.collidepoint(mouse):
                        pg.quit()
                        self.running = False
            self.clock.tick(60)

