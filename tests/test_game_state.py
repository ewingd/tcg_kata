from .context import tcg
from tcg.models import new_game, GameState

class TestGameState:
    def test_starting_player_is_randomly_determined(self):
        game = new_game()
        # XOR the active flags together
        # This ensures there is only one active player at a time.
        assert game.player.is_active ^ game.opponent.is_active



    def test_player_starting_hand_sizes(self):
        game = new_game()
        assert len(game.player.hand) == 3 if game.player.is_active else 4
        assert len(game.opponent.hand) == 3 if game.opponent.is_active else 4