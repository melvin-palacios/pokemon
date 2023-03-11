import pygame as pg
import random
from pokemon import Pokemon

class Game:

    def __init__(self, pokemon):
        pg.init()
        pg.display.set_caption('Pokemon - fight')
        self.pokemon = Pokemon(pokemon)
        self.pokemon_list = ["Salameche", "Bulbizarre", "Carapuce"]
        self.pokemon_enemy = random.choice(self.pokemon_list)
        self.pokemon_enemy = Pokemon(self.pokemon_enemy)
        self.BG = (81, 216, 60)
        self.H = 800
        self.W = 1500
        bg = pg.image.load('img/decor/bg_fight.png')
        rect_img = bg.get_rect()
        width = rect_img.width // 3
        self.piece1_rect = pg.Rect(rect_img.left, rect_img.top, width, rect_img.height)
        self.piece2_rect = pg.Rect(rect_img.left + width, rect_img.top, width, rect_img.height)
        self.piece3_rect = pg.Rect(rect_img.right - width, rect_img.top, width, rect_img.height)
        self.bg_1 = bg.subsurface(self.piece1_rect)
        self.bg_2 = bg.subsurface(self.piece2_rect)
        self.bg_3 = bg.subsurface(self.piece3_rect)
        self.bg_1 = pg.transform.scale(self.bg_1, (self.W, self.H))
        self.bg_2 = pg.transform.scale(self.bg_2, (self.W, self.H))
        self.bg_3 = pg.transform.scale(self.bg_3, (self.W, self.H))
        self.bg = [self.bg_1, self.bg_2, self.bg_3]
        self.bg_choice = random.choice(self.bg)
        self.icon = pg.image.load('img/icon.png')
        pg.display.set_icon(self.icon)
        self.screen = pg.display.set_mode((self.W, self.H))
        self.clock = pg.time.Clock()
        self.running = True
        self.font = pg.font.Font("font/font.ttf", 30)
        self.font_big = pg.font.Font("font/font.ttf", 44)
        self.font_small = pg.font.Font("font/font.ttf", 24)
        self.font_color = (0, 0, 0)
        self.fadeout = pg.Surface((self.W, self.H))
        self.fadeout = self.fadeout.convert()
        self.fadeout.fill((0, 0, 0))
        self.pokemon_enemy_cor = (self.W // 2 + 230, self.H // 2 - 300)
        self.pokemon_cor = (self.W // 2 - 500, self.H // 2 - 50)
        self.fight_bar = pg.image.load('img/battle_bar.png')
        self.fight_bar = pg.transform.scale(self.fight_bar,(self.W,230))
        self.fight_menu = pg.image.load('img/battle_menu.png')
        self.fight_menu = pg.transform.scale(self.fight_menu,(self.W // 3 + 150,230))
        self.choice_menu = pg.image.load('img/choice.png')
        self.choice_menu = pg.transform.scale(self.choice_menu,(24,40))
        self.choice_menu_cor = (self.W // 2 + 150, self.H // 2 + 235)
        self.chatbox = pg.image.load('img/chatbox.png')
        self.box_cor_1 = (self.W // 3, self.H // 6)
        self.chatbox = pg.transform.scale(self.chatbox, (self.W // 3.5, self.H // 7))
        self.chatbox_bg = pg.surface.Surface((self.W // 3.5 - 13, self.H // 7 - 8))
        self.chatbox_bg.fill((255, 255, 255))

    def update(self):
        pg.display.update()

    def fade_in(self):
        i = 255
        while i > 0:
            self.fadeout.set_alpha(i)
            self.screen.blit(self.fadeout, (0, 0))
            pg.display.update()
            i -= 5
            pg.time.delay(8)
            self.draw()
    def draw(self):
        self.screen.fill(self.BG)
        self.screen.blit(self.bg_choice, (0, 0))
        self.draw_pokemon()
        self.draw_pokemon_enemy()
        self.screen.blit(self.fight_bar,(0,self.H - 230))
        self.screen.blit(self.fight_menu,(self.W - self.W//3 - 150,self.H - 230))
        self.screen.blit(self.font_big.render("What will", True, (255,255,255)), (self.W // 2 - 690, self.H // 2 + 230))
        self.screen.blit(self.font_big.render(f"{self.pokemon.get_name()} do ?", True, (255,255,255)), (self.W // 2 - 690, self.H // 2 + 290))
        self.screen.blit(self.choice_menu, self.choice_menu_cor)


    def draw_pokemon(self):
        self.screen.blit(self.chatbox_bg, (self.W // 2 + 100, self.H // 2 + 50))
        self.screen.blit(self.chatbox, (self.W // 2 + 100 - 8, self.H // 2 + 50 - 6))
        self.screen.blit(self.font.render(str(self.pokemon_enemy.get_name()), True, self.font_color),
                         (self.W // 2 + 110, self.H // 2 + 63))
        self.screen.blit(self.font_small.render("PV:" + str(self.pokemon_enemy.get_pv()) + "/" + str(self.pokemon_enemy.get_pv_max()), True, self.font_color),
                         (self.W // 2 + 113, self.H // 2 + 110))
        self.screen.blit(self.font_small.render("LV:" + str(self.pokemon_enemy.level), True, self.font_color),
                         (self.W // 2 + 353, self.H // 2 + 110))
        self.screen.blit((self.pokemon.get_pokemon_image_back()),self.pokemon_cor)

    def draw_pokemon_enemy(self):
        self.screen.blit(self.chatbox_bg, (self.W // 2 - 460, self.H // 2 - 250))
        self.screen.blit(self.chatbox, (self.W // 2 - 460 - 8, self.H // 2 - 250 - 6))
        self.screen.blit(self.font.render(str(self.pokemon.get_name()), True, self.font_color),
                         (self.W // 2 - 450, self.H // 2 - 237))
        self.screen.blit(self.font_small.render("PV:" + str(self.pokemon.get_pv()) + "/" + str(self.pokemon.get_pv_max()), True, self.font_color),
                         (self.W // 2 - 447, self.H // 2 - 190))
        self.screen.blit(self.font_small.render("LV:" + str(self.pokemon.level), True, self.font_color),
                         (self.W // 2 - 210, self.H // 2 - 190))
        self.screen.blit((self.pokemon_enemy.get_pokemon_image_front()), self.pokemon_enemy_cor)

    def run(self):
        self.fade_in()
        while self.running:
            self.draw()
            self.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
