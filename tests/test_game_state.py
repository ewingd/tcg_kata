from .context import tcg
from tcg.models import GameState


class TestGameState:
    def test_player_starting_hand_sizes(self):
        game = GameState().start()
        assert len(game.player.hand) + len(game.opponent.hand) == 7
        assert len(game.player.hand) == 3 if game.is_active(game.player) else 4
        assert len(game.opponent.hand) == 3 if game.is_active(game.opponent) else 4

    def test_mana_increases_at_start_of_turn_to_a_max_of_10(self):
        game = GameState().start()
        max_mana = 0
        assert game.current_player.max_mana == max_mana
        for _ in range(11):
            game = game.start_new_turn()
            max_mana += 1
            max_mana = min(max_mana, 10)  # Cap at 10 mana
            assert game.current_player.max_mana == max_mana

    def test_mana_is_filled_at_start_of_turn(self):
        game = GameState().start().start_new_turn().start_new_turn()

        assert game.current_player.max_mana == 2
        assert game.current_player.mana == 2

    def test_a_card_is_drawn_at_start_of_turn(self):
        game = GameState().start()

        assert len(game.current_player.hand) == 3
        game = game.start_new_turn()

        assert len(game.current_player.hand) == 4
