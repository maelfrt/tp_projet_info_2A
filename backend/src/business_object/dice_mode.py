import secrets
from datetime import datetime

from business_object.game_mode import GameMode
from business_object.player import Player
from business_object.game import Game

class DiceMode(GameMode):
    """Concrete implementation of a dice-roll game.
 
    Both players roll a die (1-6). The highest roll wins.
    In case of a tie, the game is a draw.
    """
 
    def play(self, p1: Player, p2: Player) -> Game:
        """Plays a dice-roll round between two players.
 
        Args:
            p1 (Player): The first player.
            p2 (Player): The second player.
 
        Returns:
            Game: The resulting Game object, with the winner set (or None if draw).
        """
        d1 = secrets.choice(range(1, 7))
        d2 = secrets.choice(range(1, 7))
 
        if d1 > d2:
            winner = p1
        elif d1 < d2:
            winner = p2
        else:
            winner = None
 
        return Game(
            player1=p1,
            player2=p2,
            game_mode="dice",
            winner_name=winner,
            description=f"{p1.username} rolled {d1}, {p2.username} rolled {d2}",
            timestamp=datetime.now(),
        )


#p1 = Player("arthur", 1000, "arthur@ensai.fr")
#p2 = Player("mathis", 900, "mathis@ensai.fr")

#mode = DiceMode()
#game = mode.play(p1, p2)
#print(game)