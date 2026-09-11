import requests

from business_object.game import Game
from business_object.player import Player


class GameClient:
    BASE_URL = "http://localhost:5555"

    def get_games(self) -> list[Game]:
        r = requests.get(f"{self.BASE_URL}/")
        r.raise_for_status()  # lève une exception si status >= 400

        data = r.json()  # liste de dicts

        games = []
        for item in data:
            players = item.get("players_list", [])
            player1 = Player(username=players[0], elo=0, email=None) if len(players) > 0 else None
            player2 = Player(username=players[1], elo=0, email=None) if len(players) > 1 else None

            winner_name = item.get("winner_name")
            winner = None
            if player1 and winner_name == player1.username:
                winner = player1
            elif player2 and winner_name == player2.username:
                winner = player2

            game = Game(
                id_game=item.get("id"),
                player1=player1,
                player2=player2,
                game_mode=item.get("mode_type"),
                winner=winner,
                description=item.get("details", ""),
                timestamp=None,
            )
            games.append(game)

        return games