import secrets
from abc import ABC, abstractmethod

from fastapi import HTTPException

from dao.player_dao import PlayerDao


class GameMode(ABC):

    @abstractmethod
    def play(self, p1: int, p2: int):
        pass


class DiceMode(GameMode):
    def play(self, id_player: int, id_opponent: int):
        """Executes a single round of a dice game between two players.
        Args:
            id_player (int): The unique identifier of the first player.
            id_opponent (int): The unique identifier of the opponent.
        Returns:
            dict: A dictionary containing the match details and new elo
        Raises:
            HTTPException: 400 if the two players are the same.
            HTTPException: 404 if one or both players are not found in the database.
        """
        if id_player == id_opponent:
            raise HTTPException(status_code=400, detail="Two different players required")

        p1 = PlayerDao().find_by_id(id_player)
        p2 = PlayerDao().find_by_id(id_opponent)

        if not p1 or not p2:
            raise HTTPException(status_code=404, detail="Player not found")

        d1 = secrets.choice(range(1, 7))
        d2 = secrets.choice(range(1, 7))
        if d1 > d2:
            winner = p1
        elif d1 < d2:
            winner = p2
        else:
            winner = None

        self.update_player_ratings(p1, p2, winner)

        PlayerDao().update(p1)
        PlayerDao().update(p2)

        return {
            "player1": p1.username,
            "player2": p2.username,
            "description": f"{d1} vs {d2}",
            "winner": winner.username,
            "new_elo1": p1.elo,
            "new_elo2": p2.elo,
        }


class CoinFlipMode(GameMode):
    def play(self, id_player: int, id_opponent: int, choice="heads"):
        """Executes a single round of a coin-flip game between two players.
        Args:
            id_player (int): The unique identifier of the first player.
            id_opponent (int): The unique identifier of the opponent.
            choice (str, optional): The player's choice ('heads' or 'tails'). Defaults to "heads".
        Returns:
            dict: A dictionary containing the match details and new elo
        Raises:
            HTTPException: 400 if the two players are the same.
            HTTPException: 404 if one or both players are not found in the database.
        """
        if id_player == id_opponent:
            raise HTTPException(status_code=400, detail="Two different players required")

        p1 = PlayerDao().find_by_id(id_player)
        p2 = PlayerDao().find_by_id(id_opponent)

        if not p1 or not p2:
            raise HTTPException(status_code=404, detail="Player not found")

        result = secrets.choice(["heads", "tails"])
        winner = p1 if result == choice else p2

        self.update_player_ratings(p1, p2, winner)

        PlayerDao().update(p1)
        PlayerDao().update(p2)

        return {
            "player1": p1.username,
            "player2": p2.username,
            "description": result,
            "winner": winner.username,
            "new_elo1": p1.elo,
            "new_elo2": p2.elo,
        }


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

        if game_mode == "dice":
            return DiceMode
        elif game_mode == "coinflip":
            return CoinFlipMode
        else:
            raise ValueError(f"Unsupported game mode: {game_mode}")