from .context import tcg
from tcg.models import Deck, Card


class TestDeck:
    def test_deck_starts_with_20_cards(self):
        deck = Deck()
        assert len(deck.cards) == 20

    def test_deck_starts_with_specific_cards(self):
        deck = Deck()
        card_list = (
            Card(0),
            Card(0),
            Card(1),
            Card(1),
            Card(2),
            Card(2),
            Card(2),
            Card(3),
            Card(3),
            Card(3),
            Card(3),
            Card(4),
            Card(4),
            Card(4),
            Card(5),
            Card(5),
            Card(6),
            Card(6),
            Card(7),
            Card(8),
        )
        assert deck.cards == card_list
