from random import randint

from ..game import Game


class CoinflipMode:
    def play(self, p1, p2, choice):
        result = randint(["heads", "tails"])
        winner = p1 if result == choice else p2
        return Game(player1=p1, player2=p2, winner=winner, game_mode="Dice", description="a")
