import pygame as pg
import random
import json
from pokemon import Pokemon
from combat import Combat

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
        self.font_medium = pg.font.Font("font/font.ttf", 38)
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
        self.attack_bar = pg.image.load('img/attack_bar.png')
        self.attack_bar = pg.transform.scale(self.attack_bar,(self.W,230))
        self.choice1_cor = (self.W // 2 + 150, self.H // 2 + 235)
        self.choice2_cor = (self.W // 2 + 450, self.H // 2 + 235)
        self.choice3_cor = (self.W // 2 + 150, self.H // 2 + 310)
        self.choice4_cor = (self.W // 2 + 450, self.H // 2 + 310)
        self.choice_attack_1_cor = (self.W * 0.08 - 35, self.H // 2 + 230)
        self.choice_attack_2_cor = (self.W * 0.08 - 35, self.H // 2 + 300)
        self.choice_menu_cor = self.choice1_cor
        self.chatbox = pg.image.load('img/chatbox.png')
        self.box_cor_1 = (self.W // 3, self.H // 6)
        self.chatbox = pg.transform.scale(self.chatbox, (self.W // 3.5, self.H // 7))
        self.chatbox_bg = pg.surface.Surface((self.W // 3.5 - 13, self.H // 7 - 8))
        self.chatbox_bg.fill((255, 255, 255))
        self.is_fight_menu = False
        self.is_choice_menu = True
        self.combat = Combat(self.pokemon, self.pokemon_enemy)
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
        if self.is_fight_menu:
            self.draw_fight_menu()
        else:
            self.screen.blit(self.font_big.render("What will", True, (255,255,255)), (self.W // 2 - 690, self.H // 2 + 230))
            self.screen.blit(self.font_big.render(f"{self.pokemon.get_name()} do ?", True, (255,255,255)), (self.W // 2 - 690, self.H // 2 + 290))
            self.screen.blit(self.choice_menu, self.choice_menu_cor)

    def draw_fight_menu(self):
        self.screen.blit(self.attack_bar,(0,self.H - 230))
        self.screen.blit(self.choice_menu, self.choice_menu_cor)
        self.screen.blit(self.font_big.render(self.pokemon.get_attack_1(), True, (54, 54, 53)),(self.W * 0.08,self.H - 170))
        self.screen.blit(self.font_big.render(self.pokemon.get_attack_2(), True, (54, 54, 53)),(self.W * 0.08,self.H - 100))
        self.screen.blit(self.font_big.render("15", True, (30, 30, 30)),(self.W - 250,self.H - 170))
        self.screen.blit(self.font_big.render("15", True, (30, 30, 30)), (self.W - 130, self.H - 170))
        if self.choice_menu_cor == self.choice_attack_1_cor:
            if self.pokemon.get_attack_1() != "Charge" and self.pokemon.get_attack_1() != "Griffe":
                self.screen.blit(self.font_medium.render(self.pokemon.type, True, (54, 54, 53)), (self.W - 290, self.H - 85))
            else:
                self.screen.blit(self.font_medium.render("Normal", True, (54, 54, 53)), (self.W - 290, self.H - 85))
        elif self.choice_menu_cor == self.choice_attack_2_cor:
            if self.pokemon.get_attack_2() != "Charge" and self.pokemon.get_attack_2() != "Griffe":
                self.screen.blit(self.font_medium.render(self.pokemon.type, True, (54, 54, 53)), (self.W - 290, self.H - 85))
            else:
                self.screen.blit(self.font_medium.render("Normal", True, (54, 54, 53)), (self.W - 290, self.H - 85))
        self.update()


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

    def fade_out(self):
        i = 0
        while i < 255:
            self.fadeout.set_alpha(i)
            self.screen.blit(self.fadeout, (0, 0))
            pg.display.update()
            i += 5
            pg.time.delay(8)


    def attack_animation(self, joueur , attaque):
        if self.combat.current_turn == self.pokemon:
            for i in range(0, 50):
                if i == 25:
                    self.pokemon_enemy.get_damage(self.combat.calculate_damage(joueur, self.pokemon_enemy, attaque))
                    for i in range(0,20):
                        if i < 10:
                            self.pokemon_enemy_cor = (self.pokemon_enemy_cor[0] + 5, self.pokemon_enemy_cor[1])
                        else:
                            self.pokemon_enemy_cor = (self.pokemon_enemy_cor[0] - 5, self.pokemon_enemy_cor[1])
                        self.screen.blit(self.pokemon.get_pokemon_image_back(), self.pokemon_cor)
                        self.draw()
                        pg.time.delay(3)
                if i < 24:
                    self.pokemon_cor = (self.pokemon_cor[0] + 5, self.pokemon_cor[1])
                else:
                    self.pokemon_cor = (self.pokemon_cor[0] - 5, self.pokemon_cor[1])
                self.screen.blit(self.pokemon.get_pokemon_image_back(), self.pokemon_cor)
                self.draw()
                i += 5
                pg.time.delay(3)
        self.combat.current_turn = self.pokemon_enemy
        if self.combat.current_turn == self.pokemon_enemy:
            pg.time.delay(1000)
            for i in range(0, 50):
                if i == 25:
                    self.pokemon.get_damage(self.combat.calculate_damage(self.pokemon_enemy, self.pokemon, self.pokemon_enemy.get_attack_1()))
                    for i in range(0,20):
                        if i < 10:
                            self.pokemon_cor = (self.pokemon_cor[0] - 5, self.pokemon_cor[1])
                        else:
                            self.pokemon_cor = (self.pokemon_cor[0] + 5, self.pokemon_cor[1])
                        self.screen.blit(self.pokemon_enemy.get_pokemon_image_front(), self.pokemon_enemy_cor)
                        self.draw()
                        pg.time.delay(3)
                if i < 24:
                    self.pokemon_enemy_cor = (self.pokemon_enemy_cor[0] - 5, self.pokemon_enemy_cor[1])
                else:
                    self.pokemon_enemy_cor = (self.pokemon_enemy_cor[0] + 5, self.pokemon_enemy_cor[1])
                self.screen.blit(self.pokemon_enemy.get_pokemon_image_front(), self.pokemon_enemy_cor)
                self.draw()
                i += 5
                pg.time.delay(3)

    def run(self):
        self.fade_in()
        while self.running:
            if self.is_fight_menu:
                self.draw_fight_menu()
            else:
                self.draw()
            self.update()
            if self.combat.is_alive() == False:
                if self.combat.who_is_alive() == self.pokemon:
                    self.screen.blit(self.font_big.render("Vous avez gagné", True, (20, 200, 20)),
                                     (self.W // 2 - 100, self.H // 2 - 100))
                    pg.display.update()
                    with open("data/pokemon.json", "w") as f:
                        data = json.load(f)
                        data[self.pokemon.get_name()]["level"] = self.pokemon.level
                        data[self.pokemon_enemy.get_name()]["discovered"] = True
                else:
                    self.screen.blit(self.font_big.render("Vous avez perdu", True, (200, 20, 20)),
                                 (self.W // 2 - 100, self.H // 2 - 100))
                    pg.display.update()
                    pg.time.delay(3000)
                    self.fade_out()
                    self.running = False
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.is_fight_menu = False
                        self.choice_menu_cor = self.choice1_cor
                    if event.key == pg.K_LEFT:
                        if self.choice_menu_cor == self.choice2_cor:
                            self.choice_menu_cor = self.choice1_cor
                        elif self.choice_menu_cor == self.choice4_cor:
                            self.choice_menu_cor = self.choice3_cor

                    if event.key == pg.K_RIGHT:
                        if self.choice_menu_cor == self.choice1_cor:
                            self.choice_menu_cor = self.choice2_cor
                        elif self.choice_menu_cor == self.choice3_cor:
                            self.choice_menu_cor = self.choice4_cor
                    if event.key == pg.K_UP:
                        if self.choice_menu_cor == self.choice3_cor:
                            self.choice_menu_cor = self.choice1_cor
                        elif self.choice_menu_cor == self.choice4_cor:
                            self.choice_menu_cor = self.choice2_cor
                        elif self.choice_menu_cor == self.choice_attack_2_cor:
                            self.choice_menu_cor = self.choice_attack_1_cor
                    if event.key == pg.K_DOWN:
                        if self.choice_menu_cor == self.choice1_cor:
                            self.choice_menu_cor = self.choice3_cor
                        elif self.choice_menu_cor == self.choice2_cor:
                            self.choice_menu_cor = self.choice4_cor
                        elif self.choice_menu_cor == self.choice_attack_1_cor:
                            self.choice_menu_cor = self.choice_attack_2_cor
                    if event.key == pg.K_RETURN:
                        if self.choice_menu_cor == self.choice1_cor:
                            self.choice_menu_cor = self.choice_attack_1_cor
                            self.is_fight_menu = True
                        elif self.choice_menu_cor == self.choice2_cor:
                            print("bag")
                        elif self.choice_menu_cor == self.choice3_cor:
                            print("pokemon")
                        elif self.choice_menu_cor == self.choice4_cor:
                            if self.combat.is_miss():
                                self.attack_animation(self.pokemon_enemy, self.pokemon_enemy.get_attack_1())
                            else:
                                print("fuite")
                        elif self.choice_menu_cor == self.choice_attack_1_cor:
                            self.attack_animation(self.pokemon, self.pokemon.get_attack_1())
                        elif self.choice_menu_cor == self.choice_attack_2_cor:
                            self.attack_animation(self.pokemon, self.pokemon.get_attack_2())
