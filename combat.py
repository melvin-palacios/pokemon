import random
class Combat():
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.pokemon1_turn = True
        self.pokemon2_turn = False
        self.POKEMON_TYPES = {
            'Normal': ['Combat'],
            'Combat': ['Vol', 'Poison', 'Insecte', 'Psy', 'Fee'],
            'Vol': ['Combat', 'Insecte'],
            'Poison': ['Sol', 'Psy'],
            'Sol': ['Eau', 'Plante', 'Glace'],
            'Roche': ['Combat', 'Sol', 'Eau', 'Plante', 'Normal'],
            'Insecte': ['Vol', 'Roche', 'Feu'],
            'Spectre': ['Spectre', 'Psy'],
            'Acier': ['Combat', 'Feu', 'Sol'],
            'Feu': ['Roche', 'Sol', 'Eau'],
            'Eau': ['Electrique', 'Herbe'],
            'Plante': ['Insecte', 'Sol', 'Eau'],
            'Electrique': ['Sol'],
            'Psy': ['Spectre', 'Combat'],
            'Glace': ['Combat', 'Feu', 'Roche', 'Acier']}

    def is_alive(self):
        if self.pokemon1.get_pv() > 0 and self.pokemon2.get_pv() > 0:
            return True
        else:
            self.who_is_alive()

    def who_is_alive(self):
        if self.pokemon1.get_pv() > 0:
            return self.pokemon1
        else:
            return self.pokemon2

    def is_miss(self):
        miss = random.randint(0, 1)
        if miss == 0:
            return True
        else:
            return False

    def calculate_damage(self, pokemon1, pokemon2):
        if self.pokemon1_turn:
            if self.is_miss():
                if pokemon1.get_attack_1() in self.POKEMON_TYPES[pokemon2.type]:
                    pokemon2.get_damage(pokemon1.attacks[0] * 2)
                    return True
            else:
                return False
        else:
            if self.is_miss():
                pokemon1.get_damage(pokemon2.attacks)
                return True
            else:
                return False




