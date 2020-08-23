from __future__ import annotations
from dataclasses import dataclass, field
from typing import Tuple
import random



@dataclass(frozen=True)
class Card:
    cost: int


def make_default_deck() -> Tuple:
    costs = (0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 8)
    return tuple([Card(cost) for cost in costs])

def new_default_deck() -> Deck:
    return Deck()


@dataclass(frozen=True)
class Deck:
    cards: Tuple[Card, ...] = field(default_factory=make_default_deck)

    def draw(self, count: int=1) -> Tuple[Tuple[Card, ...], Deck]:
        return self.cards[:count], Deck(self.cards[count:])

    def shuffle(self) -> Deck:
        cards = list(self.cards)
        random.shuffle(cards)
        return Deck(tuple(cards))

@dataclass(frozen=True)
class Player:
    health: int = 30
    mana: int = 0
    hand: Tuple = ()
    is_active: bool = False
    deck: Deck = field(default_factory=new_default_deck)

    def draw(self, count: int=1) -> Player:
        hand, deck = self.deck.draw(count)
        return Player(
            self.health,
            self.mana,
            self.hand + hand,
            self.is_active,
            deck
        )

@dataclass(frozen=True)
class GameState:
    player: Player
    opponent: Player


def new_game() -> GameState:
    first_player = random.choice((0, 1))
    player = Player(is_active=(first_player==0))
    opponent = Player(is_active=(first_player==1))

    player = player.draw(3 if player.is_active else 4)
    opponent = opponent.draw(3 if opponent.is_active else 4)

    return GameState(
        player,
        opponent
    )