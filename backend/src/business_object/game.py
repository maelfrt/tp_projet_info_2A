from business_object.player import Player
from datetime import datetime
 
class Game:
 
    def __init__(self, player1 :Player, player2 :Player, game_mode :str,
    winner_name :Player, description :str,
    timestamp :datetime, id_game: int = None):
        self.id = None
        self.player1 = player1
        self.player2 = player2
        self.game_mode = game_mode
        self.winner_name = winner_name
        self.description = description
        self.timestamp = timestamp
 
    def __str__(self):
        return f"{self.game_mode} between {self.player1.username} and {self.player2.username}. Winner: {self.winner_name}"
 
#game1 = Game(Player("arthur",1000,"arthur@ensai.fr"), Player("mathis",900,"mathis@ensai.fr"),"dice",Player("arthur",1000,"arthur@ensai.fr"),"TP 2",datetime.now(),None)
#print(game1)