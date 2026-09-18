from fastapi import HTTPException

from business_object.game_mode.game_mode_factory import GameModeFactory
from business_object.scoring_strategy import ScoringStrategy
from business_object.game import Game
from dao.game_dao import GameDao
from dao.player_dao import PlayerDao
from utils.log_utils import log


class GameService:
    """Service that manages games."""

    @log
    def play(self, id_player: int, id_opponent: int, game_mode: str, **kwargs):
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

        mode = GameModeFactory.get_mode(game_mode)

        game = mode.play(p1, p2, **kwargs)

        ScoringStrategy.update_player_ratings(game)

        PlayerDao().update(p1)
        PlayerDao().update(p2)

        GameDao().create(game)

        return game

    @log
    def find_by_id(self, id_game: int) -> Game:
        """Retrieves a game by its id.
        Args:
            id_game (int): The unique identifier of the game.
        Returns:
            Game: the game matching the given id, or None if not found.
        """
        return GameDao().find_by_id(id_game)

    @log
    def find_all_by_player(self, id_player: int, game_mode: str = None) -> list[Game]:
        """Retrieves all games played by a specific player, optionally
        filtered by game mode.
        Args:
            id_player (int): The unique identifier of the player.
            game_mode (str, optional): If provided, only games of this mode
                are returned. If None, all games are returned regardless of mode.
        Returns:
            list[Game]: games involving this player.
        """
        games = GameDao().find_all_by_player(id_player)

        if game_mode is not None:
            games = [g for g in games if g.game_mode == game_mode]

        return games