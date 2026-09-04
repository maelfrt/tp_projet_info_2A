import datetime

from buisness_object.player import Player


class Game:
    """
    Class representing the game.
    Attributes:
        id_game (int): The unique identifier for the game.
        player1 (str): The first player.
        player2 (Player): The second player
        game_mode (str): the game mode
        winner (Player): who win the game betxeen player1 et player2
        description (str): description du jeux
        timestamp (datetime): temps en jeux
    """

    def __init__(
        self,
        game_mode: str,
        timestamp: datetime,
        winner: Player or None,
        player1: Player,
        player2: Player,
        description: str,
    ):
        """Constructor"""
        self.id_game = None
        self.player1 = player1
        self.player2 = player2
        self.game_mode = game_mode
        self.winner = winner
        self.timestamp = timestamp
        self.description = description

    def __str__(self):
        """Returns a string representation of the Game.
        Returns:
            str: A string containing the gamr information and the player who play.
        """
        return f"({self.game_mode} between {self.player1} and {self.player2}. Winner: {self.winner} )"
