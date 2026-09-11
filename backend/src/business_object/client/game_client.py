import requests

from business_object.game import Game

r = requests.get('http://localhost:5555/')


def get_games() -> list[Game]:
    r = requests.get("http://localhost:5555/")

    r.raise_for_status()

    data = r.json()

    games = []

    for game_data in data:
        game = Game(
            game_data["id"],
            game_data["players_list"],
            game_data["winner_name"],
            game_data["location_name"],
            game_data["duration_seconds"],
            game_data["mode_type"]
        )

        games.append(game)

    return games


data = r.json()
