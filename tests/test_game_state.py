from .context import tcg
from tcg.models import GameState

class TestGameState:

    def test_player_starting_hand_sizes(self):
        game = GameState().start()
        assert len(game.player.hand) + len(game.opponent.hand) == 7
        assert len(game.player.hand) == 3 if game.player.is_active else 4
        assert len(game.opponent.hand) == 3 if game.opponent.is_active else 4