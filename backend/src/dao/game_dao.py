import sqlite3

from business_object.game_mode.game import Game

from utils.singleton import Singleton


class GameDao(metaclass=Singleton):

    def __init__(self):
        self.connection = sqlite3.connect("game.db")
        self.connection.row_factory = sqlite3.Row

    def create(self, game: Game) -> bool:
        try:
            cursor = self.connection.cursor()

            cursor.execute(
                """
                INSERT INTO game (name, description)
                VALUES (?, ?)
                """,
                (game.name, game.description)
            )

            # Récupère l'identifiant généré par la base de données
            game.id_game = cursor.lastrowid

            self.connection.commit()

            return True

        except sqlite3.Error:
            self.connection.rollback()
            return False
    
    def find_by_id(self, id: int) -> Game:
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT id_game, name, description
            FROM game
            WHERE id_game = ?
            """,
            (id,)
        )

        row = cursor.fetchone()

        if row is None:
            return None

        # Conversion de la ligne SQL en objet Game
        return Game(
            id_game=row["id_game"],
            name=row["name"],
            description=row["description"]
        )

    def find_all_by_player(self, id_player: int) -> list[Game]:
        cursor = self.connection.cursor()

        cursor.execute(
        """
        SELECT g.id_game, g.name, g.description
        FROM game g
        INNER JOIN player_game pg ON g.id_game = pg.id_game
        WHERE pg.id_player = ?
        """,
            (id_player,)
        )

        rows = cursor.fetchall()

        games = []

        for row in rows:
            game = Game(
            id_game=row["id_game"],
            name=row["name"],
            description=row["description"]
            )
            games.append(game)

        return games