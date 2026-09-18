# uv run --project backend python backend/src/sandbox.py

from datetime import datetime

from business_object.game import Game
from business_object.player import Player
from dao.game_dao import GameDao
from dao.player_dao import PlayerDao
from utils.env_variables import display_values, load_environment_variables
from utils.log_utils import initialize_logs

load_environment_variables()
initialize_logs("Webservice")
display_values()

# 1. Create two players in the database
p1 = Player(username="gilbert", password="pwd123", elo=1000, email="gilbert@test.com", pokemon_fan=True)
p2 = Player(username="maurice", password="pwd123", elo=1200, email="maurice@test.com", pokemon_fan=False)

PlayerDao().create(p1)
PlayerDao().create(p2)

print("p1 id:", p1.id_player)
print("p2 id:", p2.id_player)

# 2. Create a game between them
game = Game(
    player1=p1,
    player2=p2,
    game_mode="coinflip",
    winner=p1,
    description="Gilbert chose heads, result was heads",
    timestamp=datetime.now(),
)

# 3. Save the game in the database
created = GameDao().create(game)
print("created:",)

