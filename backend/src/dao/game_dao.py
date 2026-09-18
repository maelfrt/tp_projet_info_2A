from business_object.game import Game
from dao.db_connection import DBConnection
from utils.log_utils import get_logger, log
from utils.singleton import Singleton

logger = get_logger(__name__)


class GameDao(metaclass=Singleton):
    """
    Data Access Object for Game-related operations.
    Implements the Singleton pattern to ensure a single DAO instance.
    """

    @log
    def create(self, game: Game) -> bool:
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO player(username, password, elo, email, pokemon_fan) VALUES "
                        "(%(username)s, %(password)s, %(elo)s, %(email)s, %(pokemon_fan)s) "
                        "RETURNING id_player;",
                        {
                            "id_game": game.id_game,
                            "id_player1": game.id_player1,
                            "id_player2": game.id_player2,
                            "game_mode": game.game_mode,
                            "id_winner": game.id_winner,
                            "detail": game.detail,
                            "timestamp": game.timestamp
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logger.error(e)
            raise

        created = False
        if res:
            game.id_game = res["id_game"]
            created = True

        return created

    @log
    def find_by_id(self, id_game: int) -> Game:
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                            "
                        "  FROM game                       "
                        " WHERE id_game = %(id_game)s;   ",
                        {"id_game": id_game},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logger.error(e)
            raise

        game = None
        if res:
            game = Game(
                id_game=res["id_game"],
                id_player1=res["id_player1"],
                id_player2=res["id_player2"],
                game_mode=res["game_mode"],
                id_winner=res["id_winner"],
                detail=res["detail"],
                timestamp=res["timestamp"]
            )

        return game


