import random


class Perso:

    def __init__(self, name):
        self.max_life_point = 12
        self.name = name

    def attack_gen(self, magic, bow, sword):
        self.magic = random.randrange(1, magic)
        self.bow = random.randrange(1, bow)
        self.sword = random.randrange(1, sword)
        print(f"magic = {self.magic}, bow = {self.bow}, sword = {self.sword}")
        weapon = input("Choisissez votre arme 1 = magic, 2 = bow, 3 = sword:")
        if weapon == "1":
            attack_point = self.magic
        elif weapon == "2":
            attack_point = self.bow
        else:
            attack_point = self.sword
        return attack_point

    def defend_gen(self,weapon, magic, bow, sword, attack_point):
        self.magic = random.randrange(1, magic)
        self.bow = random.randrange(1, bow)
        self.sword = random.randrange(1, sword)
        armes = weapon
        if armes == magic:
            result = self.magic
        elif armes == bow:
            result == self.bow
        else:
            result == self.sword

        if result < attack_point:
            current_life_point_gen -= attack_point


class Wizard(Perso):

    current_life_point = Perso.max_life_point
    magic = 12
    bow = 10
    sword = 8

    def attack(self):
        self.attack_gen(self.magic, self.bow, self.sword)

    def defend(self):
        self.defend_gen(self.attack, self.current_life_point)


class Archer(Perso):

    current_life_point = Perso.max_life_point
    magic = 10
    bow = 12
    sword = 8

    def attack(self):
        self.attack_gen(self.magic, self.bow, self.sword)

    def defend(self):
        self.defend_gen(self.attack, self.current_life_point)


class Warrior(Perso):

    current_life_point = 12
    magic = 8
    bow = 10
    sword = 12

    def attack(self):
        self.attack_gen(self.magic, self.bow, self.sword)

    def defend(self):
        self.defend_gen(self.attack, self.current_life_point)

olivier = Wizard("olivier")
print(olivier.name)

