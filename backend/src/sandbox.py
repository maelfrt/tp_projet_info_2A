from business_object.game import Game
from business_object.player import Player

p1 = Player(1, "mael", 2900, "aa")
p2 = Player(2, "Simon", 900, "ba")
g = Game(74, p1, p2, "Dice", p1, "ss")
print(g)
