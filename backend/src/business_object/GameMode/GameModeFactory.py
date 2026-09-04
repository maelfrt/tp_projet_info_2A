from abc import classmethod

from .coinflipMode import CoinflipMode
from .DiceMode import DiceMode
from .GameMode import GameMode


class GameModeFactory:
    @classmethod
    def get_mode(cls, game_mode: str) -> GameMode:
        """
        Returns the corresponding GameMode object.
        Args:
            game_mode (str): The identifier of the game mode (e.g., 'coinflip', 'dice').
        Returns:
            GameMode: An instance of a class implementing GameMode.
        Raises:
            ValueError: If the requested game_mode is not supported.
        """
        if game_mode == "Coinflip":
            return CoinflipMode
        elif game_mode == "Dice":
            return DiceMode
        else:
            raise ValueError("Le mode de jeu n'est pas disponible")
