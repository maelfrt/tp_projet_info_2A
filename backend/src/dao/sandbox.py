# uv run --project backend python backend/src/sandbox.py
from business_object.game import Game
from business_object.player import Player
from dao.game_dao import GameDao
from utils.env_variables import load_environment_variables
from datetime import datetime

load_environment_variables()   # Required to load the variables needed (env) to connect to the database 

p1 = Player(10, "am", "1961b6dd3ede3cb8ecbacbd68de040cd78eb2ed5889130cceb4c49268ea4d506", 1200, "am@ensai.fr", True, None)
p2 = Player(41, "batriciat", "5e99bf7ce2b5216ff811d3518cfe4499ddb9cb398e01600046a8f556d3e0b358", 1500, "batt@project.io", False, None)
now = datetime.now()
millisecondes = now.microsecond // 1000
game = Game(10, 10, 41, "dice", 10, "am beat batriciat easily", now.strftime("%Y-%m-%d %H:%M:%S") + f".{millisecondes:03d}")

id = GameDao().create(game)
print(id)
game2 = GameDao().find_by_id(10)
