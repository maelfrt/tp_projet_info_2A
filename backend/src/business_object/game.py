from datetime import datetime

from player import Player


class Game:
    def __init__(
        self,
        id_game: None,
        player1: Player,
        player2: Player,
        game_mode: str,
        winner: Player | None,
        description: str,
        timestamp: datetime):
        self.id_game = id_game
        self.player1 = player1
        self.player2 = player2
        self.game_mode = game_mode
        self.winner = winner
        self.description = description
        self.timestamp = timestamp

    def __str__(self):
        return f"{self.game_mode} between {self.player1} and {self.player2}. Winner : {self.winner}"


#game1 = Game(
#    None,
#    Player("mathis", 1000, "mathis@gmail.com"),
#    Player("arthur", 1000, "arthur@ensai.fr"),
#    "dice",
#    None,
#    "essai",
#    datetime(2026, 9, 4, 10, 30)
#)
#print(game1)