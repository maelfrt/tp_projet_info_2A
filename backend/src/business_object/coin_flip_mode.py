import secrets
from datetime import datetime
from business_object.game import Game
from business_object.game_mode import GameMode
from business_object.player import Player
 
 
class CoinFlipMode(GameMode):
    """Concrete implementation of a coin-toss game.
 
    The player picks "heads" or "tails". A coin is flipped:
    if the result matches the player's choice, player1 wins, otherwise player2 wins.
    """
 
    def play(self, p1: Player, p2: Player, choice: str = "heads") -> Game:
        """Plays a coin-flip round between two players.
 
        Args:
            p1 (Player): The first player (the one making the choice).
            p2 (Player): The second player.
            choice (str, optional): The player's choice ("heads" or "tails"). Defaults to "heads".
 
        Returns:
            Game: The resulting Game object, with the winner set.
        """
        result = secrets.choice(["heads", "tails"])
        winner = p1 if result == choice else p2
 
        return Game(
            player1=p1,
            player2=p2,
            game_mode="coinflip",
            winner_name=winner,
            description=f"Coin landed on {result} ({p1.username} chose {choice})",
            timestamp=datetime.now(),
        )