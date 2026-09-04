from abc import ABC, abstractmethod
from business_object.game import Game
from business_object.player import Player
 
 
class GameMode(ABC):
    """Abstract base class defining the contract for a game mode."""
 
    @abstractmethod
    def play(self, p1: Player, p2: Player) -> Game:
        """Plays a round of the game between two players.
 
        Arguments:
            p1 (Player): The first player.
            p2 (Player): The second player.
 
        Returns:
            Game: The resulting Game object, with the winner set (or None if draw).
        """
        pass