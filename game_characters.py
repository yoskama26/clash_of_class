import random


class Perso:

    def __init__(self, name):
        self.current_life_point = self.max_life_point
        self.name = name

    def __repr__(self):
        return "{} the {}. ".format(self.name, self.__class__.__name__)

    def attack(self):
        magic_d = random.randrange(1, self.magic)
        bow_d = random.randrange(1, self.bow)
        sword_d = random.randrange(1, self.sword)
        if magic_d >= bow_d and magic_d >= sword_d:
            arm = "magic"
            attack_point = magic_d
        elif bow_d >= magic_d and bow_d >= sword_d:
            arm = "bow"
            attack_point = bow_d
        elif sword_d >= magic_d and sword_d >= bow_d:
            arm = "sword"
            attack_point = sword_d
        return arm, attack_point

    def defend(self, weapon, attack_point):
        if weapon == "magic":
            result = random.randrange(1, self.magic)
            if result < attack_point:
                self.current_life_point -= attack_point
        elif weapon == "bow":
            result = random.randrange(1, self.bow)
            if result < attack_point:
                self.current_life_point -= attack_point
        elif weapon == "sword":
            result = random.randrange(1, self.sword)
            if result < attack_point:
                self.current_life_point -= attack_point


class Wizard(Perso):
    max_life_point = 12
    magic = 12
    bow = 10
    sword = 8

    def attack(self):
        arm_2, attack_2 = super(Wizard, self).attack()
        attack_1 = random.randrange(1, self.magic)
        attack_point = max(attack_1, attack_2)
        if attack_point == attack_1:
            return "magic", attack_1
        else:
            return arm_2, attack_2


class Archer(Perso):
    max_life_point = 12
    magic = 10
    bow = 12
    sword = 8

    def attack(self):
        arm, attack_point = super(Archer, self).attack()
        if arm == "bow" or arm == "magic":
            attack_point += 1
        return arm, attack_point


class Warrior(Perso):
    max_life_point = 16
    magic = 8
    bow = 10
    sword = 12



# gandalf = Wizard("gandalf")
# gimli = Warrior("gimli")
#
# arthur = Warrior("Arthur")
# merlin = Wizard("Merlin")
#
#
# #Attack 1 gandalf attack arthur:
# arm, points = gandalf.attack()
# print(gandalf, arm, points)
# arthur.defend(arm, points)
# print(arthur, arthur.current_life_point)