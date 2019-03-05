import game_characters as game
import random
communaute = []
kammelot = []

gandalf = game.Wizard("Gandalf")
gimli = game.Warrior("Gimli")
legolas = game.Archer("Legolas")
saroumane = game.Wizard("Saroumane")
aragorn = game.Warrior("Aragorn")
galadriel = game.Archer("Galadriel")
communaute.append(gandalf)
communaute.append(gimli)
communaute.append(legolas)
communaute.append(saroumane)
communaute.append(aragorn)
communaute.append(galadriel)

arthur = game.Warrior("Arthur")
merlin = game.Wizard("Merlin")
perceval = game.Archer("Perceval")
lancelot = game.Warrior("Lancelot")
olivier = game.Wizard("Olivier")
caradoc = game.Archer("Caradoc")
kammelot.append(arthur)
kammelot.append(merlin)
kammelot.append(perceval)
kammelot.append(lancelot)
kammelot.append(olivier)
kammelot.append(caradoc)

while len(communaute) != 0 or len(kammelot) != 0:
    for player_communaute, player_kammelot in zip(random.sample(communaute, 1), random.sample(kammelot, 1)):
        arm, points = player_communaute.attack()
        print(player_communaute, arm, points)
        player_kammelot.defend(arm, points)
        print(player_kammelot, player_kammelot.current_life_point)
        if player_kammelot.current_life_point <= 0:
            kammelot.remove(player_kammelot)
            print(f"{player_kammelot} est mort")
    for player_communaute, player_kammelot in zip(random.sample(communaute, 1), random.sample(kammelot, 1)):
        arm, points = player_kammelot.attack()
        print(player_kammelot, arm, points)
        player_communaute.defend(arm, points)
        print(player_communaute, player_communaute.current_life_point)
        if player_communaute.current_life_point <= 0:
            communaute.remove(player_communaute)
            print(f"{player_communaute} est mort")
    print(communaute)
    print(kammelot)


