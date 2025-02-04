import random


class Perso:

    def __init__(self, name):
        self.max_life_point = 12
        self.name = name

    def attack_gen(self):
        magic_d = random.randrange(1, self.magic)
        bow_d = random.randrange(1, self.bow)
        sword_d = random.randrange(1, self.sword)
        if magic_d >= bow_d and magic_d >= sword_d:
            arm = "magic"
            return arm, magic_d
        elif bow_d >= magic_d and bow_d >= sword_d:
            arm = "bow"
            return arm, bow_d
        elif sword_d >= magic_d and sword_d >= bow_d:
            arm = "sword"
            return arm, sword_d

    def defend_gen(self, weapon, points):
        if weapon == "magic":
            self.magic = random.randrange(1, self.magic)
            result = self.magic
            if result < attack_point:
                self.max_life_point -= attack_point
        elif weapon == "bow":
            self.bow = random.randrange(1, self.bow)
            result = self.bow
            if result < attack_point:
                self.max_life_point -= attack_point
        elif weapon == "sword":
            self.sword = random.randrange(1, self.sword)
            result = self.sword
            if result < attack_point:
                self.max_life_point -= attack_point


class Wizard(Perso):
    magic = 12
    bow = 10
    sword = 8

    def attack(self):
        self.attack_gen()

    def defend(self):
        self.defend_gen(self.attack_gen, self.attack_gen)


class Archer(Perso):
    magic = 10
    bow = 12
    sword = 8

    def attack(self):
        self.attack_gen()

    def defend(self):
        self.defend_gen(self.attack_gen, self.attack_gen)


class Warrior(Perso):
    magic = 8
    bow = 10
    sword = 12

    def attack(self):
        self.attack_gen()

    def defend(self):
        self.defend_gen(self.attack_gen, self.attack_gen)


olivier = Warrior("olivier")
legolas = Archer("Legolas")

arm, attack_point = olivier.attack()

legolas.defend(arm, attack_point)
