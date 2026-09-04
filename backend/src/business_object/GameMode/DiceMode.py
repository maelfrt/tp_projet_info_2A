from random import randint

from ..game import Game


class DiceMode:
    def play(self, p1, p2):
        d1 = randint(1, 6)
        d2 = randint(1, 6)
        if d1 > d2:
            winner = p1
        elif d1 < d2:
            winner = p2
        else:
            winner = None
        return Game(player1=p1, player2=p2, winner=winner, game_mode="Dice", description="a")
