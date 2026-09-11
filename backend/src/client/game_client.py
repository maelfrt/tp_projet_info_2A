
from datetime import datetime

import requests

from business_object.game import Game
from business_object.player import Player


def get_games():
    """Get all games from the API and convert them into Game objects."""

    # Call the endpoint
    r = requests.get("http://localhost:5000/games")

    # Check response
    r.raise_for_status()

    # Get JSON
    data = r.json()

    # Convert JSON into a list of Game
    games = []

    for game_data in data:

        # Create Player 1
        player1 = Player(
            username=game_data["player1"]["username"]
        )

        # Create Player 2
        player2 = Player(
            username=game_data["player2"]["username"]
        )

        # Create winner
        if game_data["winner"] is not None:
            winner = Player(
                username=game_data["winner"]["username"]
            )
        else:
            winner = None

        # Convert timestamp from string to datetime
        timestamp = datetime.fromisoformat(
            game_data["timestamp"]
        )

        # Create Game
        game = Game(
            player1=player1,
            player2=player2,
            game_mode=game_data["game_mode"],
            winner=winner,
            description=game_data["description"],
            timestamp=timestamp,
            id_game=game_data["id_game"]
        )

        games.append(game)

    return games
