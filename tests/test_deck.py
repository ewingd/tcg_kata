from .context import tcg
from tcg.models import Deck, Card


class TestDeck:
    def test_deck_starts_with_20_cards(self):
        deck = Deck()
        assert len(deck.cards) == 20

    def test_deck_starts_with_specific_cards(self):
        deck = Deck()
        card_list = self._get_default_deck()
        assert deck.cards == card_list

    def test_drawing_a_card_removes_it_from_the_deck(self):
        deck = Deck()
        card_list = self._get_default_deck()
        card, deck = deck.draw()

        assert len(deck.cards) == 19
        assert card + deck.cards == card_list

    def test_a_deck_can_be_shuffled(self):
        deck = Deck()
        card_list = self._get_default_deck()
        deck = deck.shuffle()

        assert len(deck.cards) == 20
        # Decks should only match if the cards are in the same order
        assert card_list != deck.cards

    def _get_default_deck(self):
        return (
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
