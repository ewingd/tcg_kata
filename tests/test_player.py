from .context import tcg
from tcg.models import Player


class TestPlayer:
    def test_players_start_with_30_health(self):
        player = Player()
        assert player.health == 30

    def test_players_start_with_0_mana(self):
        player = Player()
        assert player.mana == 0
