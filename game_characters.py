import random


class Perso:

    def __init__(self, name):
        self.current_life_point = self.max_life_point
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

    def defend_gen(self, weapon, attack_point):
        if weapon == "magic":
            self.magic = random.randrange(1, self.magic)
            result = self.magic
            if result < attack_point:
                self.current_life_point -= attack_point
        elif weapon == "bow":
            self.bow = random.randrange(1, self.bow)
            result = self.bow
            if result < attack_point:
                self.current_life_point -= attack_point
        elif weapon == "sword":
            self.sword = random.randrange(1, self.sword)
            result = self.sword
            if result < attack_point:
                self.current_life_point -= attack_point


class Wizard(Perso):
    max_life_point = 12
    magic = 12
    bow = 10
    sword = 8

    def attack(self):
        return self.attack_gen()

    def defend(self, weapon, attack_point):
        self.defend_gen(weapon, attack_point)


class Archer(Perso):
    max_life_point = 12
    magic = 10
    bow = 12
    sword = 8

    def attack(self):
        return self.attack_gen()

    def defend(self, weapon, attack_point):
        self.defend_gen(weapon, attack_point)


class Warrior(Perso):
    max_life_point = 12
    magic = 8
    bow = 10
    sword = 12

    def attack(self):
        return self.attack_gen()

    def defend(self, weapon, attack_point):
        self.defend_gen(weapon, attack_point)


gandalf = Wizard("gandalf")
gimli = Warrior("gimli")

arthur = Warrior("Arthur")
merlin = Wizard("Merlin")


#Attack 1 gandalf attack arthur:
arm, points = gandalf.attack()
print(gandalf, arm, points)
arthur.defend(arm, points)
print(arthur, arthur.current_life_point)
