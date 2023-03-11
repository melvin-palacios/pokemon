import pygame as pg
import json
class Pokemon:
    def __init__(self, nom):

        with open('data/pokemon.json', 'r') as f:
            data = json.load(f)

            self.__nom = data[nom]["name"]
            self.__pv_max = data[nom]["pv"]
            self.__pv = data[nom]["pv"]
            self.attacks = data[nom]["attack"]
            self.attack_1 = data[nom]["moves"][0]["name"]
            self.attack_2 = data[nom]["moves"][1]["name"]
            self.defense = data[nom]["defense"]
            self.level = data[nom]["level"]
            self.type = data[nom]["type"]
            self.evolution = data[nom]["evolution"]
            self.pokemon_res = (300, 300)
            self.image_front = pg.image.load(data[nom]["front_img"])
            self.image_front = pg.transform.scale(self.image_front, self.pokemon_res)
            self.image_back = pg.image.load(data[nom]["back_img"])
            self.image_back = pg.transform.scale(self.image_back, self.pokemon_res)
    def get_name(self):
        return self.__nom

    def get_pv(self):
        return self.__pv

    def get_pv_max(self):
        return self.__pv_max

    def get_pokemon_image_front(self):
        return self.image_front
    def get_pokemon_image_back(self):
        return self.image_back

    def get_attack_1(self):
        return self.attack_1

    def get_attack_2(self):
        return self.attack_2

