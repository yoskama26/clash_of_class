class Perso:
    pv = 12


class Wizard(Perso):
    def __init__(self):
        self.arme = "magic"
        self.nb_point = 12



p = Wizard()
print(p.arme)
