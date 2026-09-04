from abc import ABC, abstractmethod


class GameMode(ABC):
    ""
    @abstractmethod
    def play(
        self,
        player_id,
        opponent_id,
        game_mode,
        **kwargs
        ):
        pass
