import json
import random
class Combat():
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

        self.current_turn = self.pokemon1

        with open('data/types.json', 'r') as f:
            data = json.load(f)
            self.pokemon_type = data


    def is_alive(self):
        if self.pokemon1.get_pv() > 0 and self.pokemon2.get_pv() > 0:
            return True
        else:
            return False

    def who_is_alive(self):
        if self.pokemon1.get_pv() > 0:
            return self.pokemon1
        else:
            return self.pokemon2

    def is_miss(self):
        miss = random.randint(0, 4)
        if miss == 0:
            return True
        else:
            return False

    def calculate_damage(self, pokemon1, pokemon2, attack):
        if self.is_miss():
            return 0
        if pokemon1 == self.pokemon1:
            if attack == "Charge" or attack == "Griffe":
                efficacite = self.pokemon_type['normal'][pokemon2.type]
            else:
                efficacite = self.pokemon_type[pokemon1.type][pokemon2.type]
            lvl_coef = 0.5
            attack_coef = self.pokemon1.get_attacks() / self.pokemon2.defense
            attack = self.pokemon1.get_attacks()
            damage = int((lvl_coef * attack * attack_coef + 2) * efficacite)
            self.current_turn = self.pokemon2
            print(damage)
            return damage
        else:
            if attack == "Charge" or attack == "Griffe":
                efficacite = self.pokemon_type['normal'][pokemon1.type]
            else:
                efficacite = self.pokemon_type[pokemon2.type][pokemon1.type]
            lvl_coef = 0.5
            attack_coef = self.pokemon2.get_attacks() / self.pokemon1.defense
            attack = self.pokemon2.get_attacks()
            damage = int((lvl_coef * attack * attack_coef + 2) * efficacite)
            self.current_turn = self.pokemon1
            print(damage)
            return damage







