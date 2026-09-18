from business_object.game import Game
from dao.db_connection import DBConnection
from utils.log_utils import get_logger, log
from utils.singleton import Singleton
from dao.player_dao import PlayerDao

logger = get_logger(__name__)


class GameDao(metaclass=Singleton):
    """Class containing methods to access Games in the database."""

    @log
    def create(self, game) -> bool:
        """Create a game in the database.
        Args:
            Game to create
        Returns:
            True if creation is successful, False otherwise
        """
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO game(id_game, id_player1, id_player2, game_mode, id_winner, detail, timestamp) VALUES "
                        "(%(id_game)s, %(id_player1)s, %(id_player2)s, %(game_mode)s, %(id_winner)s, %(detail)s, %(timestamp)s) "
                        "RETURNING id_game;",
                        {
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
        """Find a game by their id.
        Args:
            id_game (int): The ID of the game to find
        Returns:
            Game matching the given id
        """
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
                id_player1=res["id_player1"],
                id_player2=res["id_player2"],
                game_mode=res["game_mode"],
                id_winner=res["id_winner"],
                id_game=res["id_game"],
                detail=res["detail"],
                timestamp=res["timestamp"]
            )

        return game

    @log
    def find_all_by_player(self, id_player: int) -> list[Game]:
        """Find all the games played by one player.
        Args:
            id_player (int): The ID of the player
        Returns:
            Games played by the player
        """
        res = []
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                            "
                        "FROM game g "
                        "WHERE g.id_player1 = %(id_player)s OR g.id_player2 = %(id_player)s;   ",
                        {"id_player": id_player},
                    )
                    rows = cursor.fetchall()
        except Exception as e:
            logger.error(e)
            raise

        if rows:
            for row in rows:
                p1 = PlayerDao().find_by_id(row["id_player1"])
                p2 = PlayerDao().find_by_id(row["id_player2"])
                winner = PlayerDao().find_by_id(row["id_winner"]) if row["id_winner"] else None
                res.append(
                    Game(
                        id_game=row["id_game"],
                        game_mode=row["game_mode"],
                        player1=p1,
                        player2=p2,
                        winner=winner,
                        detail=row["detail"],
                    )
                )
        return res
